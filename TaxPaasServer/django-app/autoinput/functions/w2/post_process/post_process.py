from autoinput.functions.decorator import timeit
__all__ = ('post_process1', 'post_process2')

# 데이터 정리 작업.
# 각각 데이터의 앞에 3글자를 통해 header를 만들고, header와 w2_dic을 연결
# 데이터 정리 작업.
# 각각 데이터의 앞에 3글자를 통해 header를 만들고, header와 w2_dic을 연결

@timeit
def post_process1(page, w2_dic):
    print("post_process 1을 진행합니다.")
    word_list = ['number', 'it', '(ein)', 'other', 'compensation', 'etc', 'code', 'zip', 'wages', 'tax', 'tips',
            'benefits', 'state', 'name', 'plan', 'pay', 'employee']
    result = {}
    for _ in range(10):
        if '' in page:
            page.remove('')
        else:
            break
    for string in page:
        header = string[:3] if ' ' not in string[:3] else string[:2]
        if '.' in list(header):
            tmp = list(header)
            tmp.remove('.')
            header = str(''.join(tmp))
        if ' ' in list(header):
            tmp = list(header)
            tmp.remove(' ')
            header = str(''.join(tmp))
        ful_data = string.split("\n")
        for key in w2_dic:
            if header == key:
                exist = True
                break
        data = ful_data[1:]
        # data에 ''지우는 거, 최대 10개까지 지움.
        for _ in range(10):
            if '' in data:
                data.remove('')
            if '' not in data:
                break
        # exist란 ocr 결과물의 각 header와 w2_dic의 key가 일치하는 게 없는 상황.
        # 어디서부터가 유의미한 데이터인가 : W2 양식에서 맨 마지막 단어만 word_list 넣어준다.
        # word_dic을 for 구문으로 돌면서 data의 각 요소에 word가 있는지 파악한다.
        # 첫쨰로 W2_dic과 일치하는 key를 찾는다.
        # word_list에 있는 단어로 데이터와 제시문을 분리
        if exist == True:
            for word in word_list:
                for lump in data:
                    for split_lump in lump.split(" "):
                        if split_lump.lower() == word:
                            data.remove(lump)
            # 깨끗한 데이터
            if w2_dic[header] in result and len(data) == 0:
                pass
            else:
                result[w2_dic[header]] = data
        else:
            print("page와 일치하는 key가 존재하지 않습니다.{}".format(header))

    # 있다면 카피한 data_list에서 뺀다.
    # 데이터를 뽑는다.
    if '13 Statutory employee' in result:
        result['Statutory employee'] = result['13 Statutory employee']
        result.pop('13 Statutory employee', None)
    if 'Statutory Employee' in result:
        result['Statutory employee'] = result['Statutory Employee']
        result.pop('Statutory Employee')
    check_list = ['Retirement plan', 'Statutory employee', 'Third-party sick pay', 'Statutory Employee']
    for check in check_list:
        if check in result:
            tmp = result[check]
            if len(tmp) == 0:
                result[check] = 'N'
            elif tmp in [['N'], ['n']]:
                result[check] = 'N'
            elif tmp in [['Y'], ['y'], ['X']]:
                result[check] = 'Y'

    number_data = ['1 Wages, tips, other compensation', '16 State wages, tips, etc'
                  ,'17 State income tax', '18 Local wages, tips, etc', '19 Local income tax',
                   '2 Federal income tax withheld', '3 Social security wages', '4 Social security tax withheld',
                  '5 Medicare wages and tips', '6 Medicare tax withheld', '7 Social security tips',]
    for key in number_data:
        if key in result:
            if len(result[key]) == 0:
                pass
            elif len(result[key]) == 1:
                tmp = result[key][0]
                good = ''.join(tmp.split(" "))
                try:
                    result[key] = float(good)
                except ValueError:
                    # 잘못읽어 햇갈리기 쉬운 거 처리.
                    confused = [('l', '1'), ('o', '0'), ('O', '0')]
                    for x in confused:
                        if x[0] in good:
                            listed_good = list(good)
                            idx= listed_good.index(x[0])
                            listed_good[idx] = x[1]
                            good = ''.join(listed_good)
                            good = ''.join(good)
                    try:
                        result[key] = float(good)
                    except:
                        print("오류 {}는 숫자만 있어야 하는 데이터입니다. 다른 값이 들어가 있습니다.".format(key))
            else:
                print('오류 number_data: {} 는 하나의 데이터가 아닙니다. '.format(key) )

    key = 'c Employer’s Name, Address, and ZIP Code'
    return result

@timeit
def post_process2(result):
    print("post_process 2을 시작합니다.")
    rdbs = {}

    ssn = result["a Employee's social security number"][0]
    first_name = result["e Employee's Name, Address, and ZIP Code"][0].split(" ")[0]
    last_name = result["e Employee's Name, Address, and ZIP Code"][0].split(" ")[1]
    street = result["e Employee's Name, Address, and ZIP Code"][1]
    employee_state_zip_code = result["e Employee's Name, Address, and ZIP Code"][2].split(",")[1].split(" ")
    for _ in range(10):
        if '' in employee_state_zip_code:
            employee_state_zip_code.remove('')
        else:
            break
    city = result["e Employee's Name, Address, and ZIP Code"][2].split(",")[0]
    EIN = result['b Employer identiﬁcation number'][0]
    if "#" in result['c Employer’s Name, Address, and ZIP Code'][0]:
        employer_name = result['c Employer’s Name, Address, and ZIP Code'][0].split("#")[0]
    else:
        employer_name = result['c Employer’s Name, Address, and ZIP Code'][0]
    employer_street = result['c Employer’s Name, Address, and ZIP Code'][1]
    if ',' in result['c Employer’s Name, Address, and ZIP Code'][2]:
        employer_multi = result['c Employer’s Name, Address, and ZIP Code'][2].split(",")
    else:
        employer_multi = result['c Employer’s Name, Address, and ZIP Code'][2].split(" ")
    employer_city = employer_multi[0]
    if len(employer_multi[1:]) > 1:
        employer_state_zip = employer_multi[1:]
    else:
        employer_state_zip = employer_multi[1].split(" ")
        for _ in range(10):
            if '' in employer_state_zip:
                employer_state_zip.remove('')
            else:
                break
    employer_state = employer_state_zip[0]
    employer_zip = employer_state_zip[1]

    wage = result['1 Wages, tips, other compensation']
    federal_income = result['2 Federal income tax withheld']
    social_security_wages = result['3 Social security wages']
    social_security_tax = result['4 Social security tax withheld']
    medicare_wages = result['5 Medicare wages and tips']
    medicare_tax = result['6 Medicare tax withheld']
    social_security_tips = result['7 Social security tips']
    allocated_tips = result['8 Allocated tips']
    dependent_care_benefits = result['10 Dependent Care Benefits']
    if '11 Nonqualiﬁed plans' in result:
        non_qualified_plans = result['11 Nonqualiﬁed plans']
    else:
        non_qualified_plans = []
    if '12a See instructions for box 12' in result:
        box12a = result['12a See instructions for box 12'][0]
    else:
        box12a = result['12 See Instructions for box 12'][0]
    if '12b Not defined' in result:
        box12b = result['12b Not defined']
    else:
        box12b = []
    if '12c Not defined' in result:
        box12c = result['12c Not defined']
    else:
        box12c = []
    if '12d Not defined' in result:
        box12d = result['12d Not defined']
    else:
        box12d = []
    box13_se = result['Statutory employee']
    box13_rp = result['Retirement plan']
    box13_tpsp = result['Third-party sick pay']
    if len(result['14 Other']) != 0:
        box14_type = result['14 Other'][0].split(" ")[0]
        box14_amount = result['14 Other'][0].split(" ")[1]
    else:
        box14_type = []
        box14_amount = []
    if "|" in result['15 State Employer‘s state ID number'][0]:
        employer_state2 = result['15 State Employer‘s state ID number'][0].split("|")[0]
        employer_state_id = result['15 State Employer‘s state ID number'][0].split("|")[1]
    else:
        employer_state2 = result['15 State Employer‘s state ID number'][0]
        employer_state_id = result["Employer's State ID Number"][0]
    for _ in range(10):
        if ' ' in employer_state_id:
            if type(employer_state_id) != list:
                tmp = list(employer_state_id)
                tmp.remove(' ')
                employer_state_id = "".join(tmp)
            else:
                employer_state_id.remove(' ')
        else:
            break

    state_wages = result['16 State wages, tips, etc']
    state_tax = result['17 State income tax']
    locality_name = result['20 Locality name']
    local_wages = result['18 Local wages, tips, etc']
    local_tax = result['19 Local income tax']

    rdbs['ssn'] = ssn
    rdbs['employee_first_name'] = str(first_name)
    rdbs['employee_last_name'] = str(last_name)
    rdbs['employee_zip_code'] = str(employee_state_zip_code[1])
    rdbs['street'] = str(street)
    rdbs['employee_city'] = str(city)
    rdbs['employee_state'] = str(employee_state_zip_code[0])
    rdbs['ein'] = str(EIN)
    rdbs['employer_name'] = str(employer_name)
    rdbs['employer_zip'] = str(employer_zip)
    rdbs['employer_street'] = str(employer_street)
    rdbs['employer_city'] = str(employer_city)
    rdbs['employer_state'] = str(employer_state)
    rdbs['wage'] = str(wage)
    rdbs['federal_income'] = str(federal_income)
    rdbs['social_security_wages'] = str(social_security_wages)
    rdbs['social_security_tax'] = str(social_security_tax)
    rdbs['medicare_wages'] = str(medicare_wages)
    rdbs['medicare_tax'] = str(medicare_tax)
    rdbs['social_security_tips'] = str(social_security_tips)
    rdbs['allocated_tips'] = str(allocated_tips)
    rdbs['dependent_care_benefits'] = str(dependent_care_benefits)
    rdbs['non_qualified_plans'] = str(non_qualified_plans)
    rdbs['box12a'] = str(box12a)
    rdbs['box12b'] = str(box12b)
    rdbs['box12c'] = str(box12c)
    rdbs['box12d'] = str(box12d)
    rdbs['box13_se'] = str(box13_se)
    rdbs['box13_rp'] = str(box13_rp)
    rdbs['box13_tpsp'] = str(box13_tpsp)
    rdbs['box14_type'] = str(box14_type)
    rdbs['box14_amount'] = str(box14_amount)
    rdbs['employer_state2'] = str(employer_state2)
    rdbs['employer_state_id'] = str(employer_state_id)
    rdbs['state_wages'] = str(state_wages)
    rdbs['state_tax'] = str(state_tax)
    rdbs['locality_name'] = str(locality_name)
    rdbs['local_wages'] = str(local_wages)
    rdbs['local_tax'] = str(local_tax)
    return rdbs