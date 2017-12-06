import numpy as np

from autoinput.functions.decorator import timeit
from autoinput.functions import capture_checkbox
__all__ = ('post_process', 'make_div_dic')


# 데이터 정리 작업.
@timeit
def make_div_dic():
    reference_dic = {}
    reference_dic[
        'PAYER’S name, sweet address, city or town, state or province, country, ZIP or foreign postal code, and telephone n0'] = 'c'
    reference_dic["PAYER'S federal identification number"] = 'd'
    reference_dic['RECIPIENT”S identification number'] = 'e'
    reference_dic['RECIPIENT’S name'] = 'f.1'
    reference_dic['Street address (including a9tn0)'] = "f.3"
    reference_dic[
        'City or town, state or province, country, and ZIP or foreign postal code'] = "f.4"
    reference_dic['FATCA filing requirement'] = 'g'
    reference_dic['Account number (see instructions)'] = 'h'
    reference_dic['1a'] = 'total_ordinary_dividends'
    reference_dic['1b'] = 'qualified_dividends'
    reference_dic['2a'] = 'total_capital_gain_distr'
    reference_dic['2b'] = 'unrecap'
    reference_dic['2c'] = 'section_1202_gain'
    reference_dic['2d'] = 'collectibles_gain'
    reference_dic['3'] = 'nondividend_distributions'
    reference_dic['4'] = 'federal_income_tax'
    reference_dic['5'] = 'investment_expense'
    reference_dic['6'] = 'foreign_tax'
    reference_dic['7'] = 'foreign_country_possession'
    reference_dic['8'] = 'cash_liquidation_distributions'
    reference_dic['9'] = 'noncash_liquidation_distributions'
    reference_dic['10'] = 'exempt_interest_dividends'
    reference_dic['11'] = 'specified_private_activity_bond'
    reference_dic['12'] = 'state_recheck'
    reference_dic['13'] = 'state_in'
    reference_dic['14'] = 'state_tax'
    return reference_dic

@timeit
def int_possible_str(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


@timeit
# checkbox 내부 값 추출하기
def extract_checkbox_data(img=None, check_box=None):
    ck_start, ck_end = check_box[0][0][0], check_box[0][2][0]
    checkbox_img = img.crop((ck_start[0], ck_start[1], ck_end[0], ck_end[1]))
    data = np.mean(np.array(checkbox_img))
    if data <= 252:
        return "Yes"
    else:
        return "No"


@timeit
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
            for idx, val in enumerate(key):
                try:
                    if val == "O" and int_possible_str(prev):
                        temp = key[:idx] + "0"
                        if idx < len(key):
                            key = temp + key[idx + 1:]
                except NameError:
                    pass
                prev = val
            if key[:2] == "II":
                key = "11" + key[2:]
            if key[:2] == "lb":
                key = "1b" + key[2:]
            if key[:2] == "Ia":
                key = "1a" + key[2:]

            value = string[1:]
            value = [string.replace("\n", " ") for string in value]
            doc_dict[key] = value
        except IndexError:
            doc_dict[key] = 'no_value'

    # Mapping
    rdbs = {}
    for key, val in doc_dict.items():
        try:
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

        except KeyError:
            # Unnumbered Key Mapping 1 - hard cording
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

    f1_value = rdbs['f.1'][0]
    rdbs["recipient_first_name"] = f1_value.split(" ")[0]
    rdbs["recipient_last_name"] = " ".join(f1_value.split(" ")[1:])
    del (rdbs["f.1"])

    f3_value = rdbs["f.3"][0]
    rdbs["street_address_recheck"] = f3_value
    del (rdbs['f.3'])

    f4_value = rdbs['f.4'][0]
    print("=================================")
    print(f4_value)
    rdbs["city_check"] = " ".join(f4_value.split(" ")[0:2])
    rdbs["state_check"] = f4_value.split(" ")[2]
    rdbs["zip_code_check"] = f4_value.split(" ")[3]
    del (rdbs['f.4'])

    src = np.array(img)
    check_box = capture_checkbox(src=src)
    is_checked = extract_checkbox_data(img=img, check_box=check_box)
    rdbs['fatca_filling'] = is_checked
    del (rdbs['g'])

    h_value = rdbs['h']
    rdbs['account_number'] = h_value[0] if len(h_value) >= 1 else ''
    del (rdbs['h'])
    return rdbs
