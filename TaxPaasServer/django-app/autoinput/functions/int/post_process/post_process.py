import numpy as np
import cv2
from PIL import Image
from autoinput.functions.decorator import timeit
from autoinput.functions import capture_checkbox
__all__ = ('find_checkbox_index', 'post_process', 'make_int_dic')


# 데이터 정리 작업.
@timeit
def find_checkbox_index(start=None, end=None, checkbox_point=None):
    real_index = None
    ck_start, ck_end = checkbox_point[0], checkbox_point[1]
    for index in range(len(start)):
        left_up = start[index]
        right_down = end[index]
        if ck_start[0] > left_up[1] and ck_start[1] > left_up[0]:
            if ck_end[0] < right_down[1] and ck_end[1] < right_down[0]:
                # print("Index - {} True".format(index))
                real_index = index
    return real_index


@timeit
# mke int_dictionary - hard cording
def make_int_dic():
    reference_dic = {}
    reference_dic[
        "PAYER'S name, street address, city or town, state or province, country, ZIP or foreign postal code, and telephone no"] = "c"
    reference_dic["PAYER’s federal identification number"] = "d"
    reference_dic["RECIPIENT’S identification number"] = "e"
    reference_dic["RECIPIENT’S name"] = "f.1"
    reference_dic["Street address(including apt, no,)"] = "f.3"
    reference_dic[
        "City or town, state or province, country, and ZIP or foreign postal code"] = "f.4"
    reference_dic["FATCA filling requirement"] = "g"
    reference_dic["Account number See instructions"] = "h"
    reference_dic["Payer’s RTN(optional)"] = "i"

    reference_dic[""] = ""
    reference_dic["1"] = "interest_income"
    reference_dic["2"] = "early_withdrawal_penalty"
    reference_dic["3"] = "interest_us_saving_bonds"
    reference_dic["4"] = "federal_income_tax"
    reference_dic["5"] = "investment_expenses"
    reference_dic["6"] = "foreign_tax_paid"
    reference_dic["7"] = "foreign_country_us_possession"
    reference_dic["8"] = "tax_exempt_interest"
    reference_dic["9"] = "specified_private_bond"
    reference_dic["10"] = "market_discount"
    reference_dic["11"] = "bond_premium"
    reference_dic["12"] = ""
    reference_dic["13"] = "bond_premium_tax_exempt"
    reference_dic["14"] = "tax_exempt_tax_credit"
    reference_dic["15"] = "state_recheck"
    reference_dic["16"] = "state_in"
    reference_dic["17"] = "state_tax"

    return reference_dic


# checkbox 내부 값 추출하기
def extract_checkbox_data(img=None, check_box=None):
    ck_start, ck_end = check_box[0][0][0], check_box[0][2][0]
    checkbox_img = img.crop((ck_start[0], ck_start[1], ck_end[0], ck_end[1]))
    data = np.mean(np.array(checkbox_img))
    if data <= 252:
        return "Yes"
    else:
        return "No"


def post_process(page=None, reference_dic=None, img=None):
    filtered_page = [string.split("\n\n") for string in page]
    # 글자 오타 다듬기.
    doc_dict = {}
    for idx, string in enumerate(filtered_page):

        try:
            key = string[0]
            key = key.replace("\n", " ")
            key = key.replace(".", "")
        except:
            key = 'no_key'
        try:
            # 예외처리
            if key == "1 5 state":
                key = "15 state"
            if key == "RECIPIENT’S name":
                value = string[1]
                doc_dict[key] = value
                key2 = string[2]
                doc_dict[key2] = string[3]
                key3 = string[4]
                doc_dict[key3] = string[5]
            if key == "PAYE R’s federal identification number":
                key = "PAYER’s federal identification number"
            if key == 'Accou nt number See instructions':
                key = 'Account number See instructions'

            value = string[1:]
            value = [string.replace("\n", " ") for string in value]
            doc_dict[key] = value


        except IndexError:
            doc_dict[key] = 'no_value'

    print("int _ post_proces")
    ## Mapping
    rdbs = {}
    for key, val in doc_dict.items():
        try:
            int(key[:2])
            key_number = key[:2]
            key_number = key_number.strip()
            new_key = reference_dic[key_number]
            if len(val) == 1:
                new_val = val[0]
                new_val = new_val.replace("$", "")
                new_val = new_val.strip()
                rdbs[new_key] = new_val
            elif len(val) == 0:
                rdbs[new_key] = ""
            else:
                rdbs[new_key] = val

        except ValueError:
            if key in reference_dic.keys():
                new_key = reference_dic[key]
                rdbs[new_key] = val

    c_value = rdbs['c']
    rdbs["payer_name"] = c_value[0]
    rdbs["street_address"] = c_value[1]
    city_and_state = c_value[2].split(",")
    rdbs["city"] = city_and_state[0]
    rdbs["state"] = city_and_state[1].strip().split(" ")[0]
    rdbs["zip_code"] = city_and_state[1].strip().split(" ")[1]
    del (rdbs["c"])

    rdbs['payer_federal_in'] = rdbs["d"][0]
    del (rdbs["d"])

    rdbs["recipient_in"] = rdbs["e"][0].replace(" ", "")
    del (rdbs["e"])

    f1_value = rdbs['f.1']
    rdbs["recipient_first_name"] = f1_value[0].split(" ")[0]
    rdbs["recipient_last_name"] = " ".join(f1_value[0].split(" ")[1:])
    del (rdbs["f.1"])

    f3_value = rdbs["f.3"]
    rdbs["street_address"] = f3_value
    del (rdbs['f.3'])

    f4_value = rdbs['f.4']
    rdbs["city_check"] = f4_value.split(",")[0]
    rdbs["state_check"] = f4_value.split(",")[1].strip().split(" ")[0]
    rdbs["zip_code_check"] = f4_value.split(",")[1].strip().split(" ")[1]
    del (rdbs['f.4'])

    g_value = rdbs['g']
    src = np.array(img)
    check_box = [capture_checkbox(src=src)[0]]
    is_checked = extract_checkbox_data(img=img, check_box=check_box)
    rdbs['fatca_filling'] = is_checked
    del (rdbs['g'])

    h_value = rdbs['h']
    rdbs['account_number'] = h_value[0] if len(h_value) >= 1 else ''
    del (rdbs['h'])

    i_value = rdbs['i']
    rdbs['payer_rtn'] = i_value[0] if len(i_value) >= 1 else ''
    del (rdbs['i'])

    del (rdbs[""])
    return rdbs