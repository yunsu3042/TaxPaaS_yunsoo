__all__ = ('post_process1', 'post_process2')

# 데이터 정리 작업.
# 각각 데이터의 앞에 3글자를 통해 header를 만들고, header와 w2_dic을 연결
# 데이터 정리 작업.
# 각각 데이터의 앞에 3글자를 통해 header를 만들고, header와 w2_dic을 연결
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

def post_process2(result):
    print("post_process 2을 시작합니다.")
    rdbs = {}

    ssn = result["a Employee's social security number"][0]
    first_name = result["e Employee's Name, Address, and ZIP Code"][0].split(" ")[0]
    last_name = result["e Employee's Name, Address, and ZIP Code"][0].split(" ")[1]
    street = result["e Employee's Name, Address, and ZIP Code"][1]
    state_zip = result["e Employee's Name, Address, and ZIP Code"][2].split(",")[1].split(" ")
    for _ in range(10):
        if '' in state_zip:
            state_zip.remove('')
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

    wtc = result['1 Wages, tips, other compensation']
    fitw = result['2 Federal income tax withheld']
    ssw = result['3 Social security wages']
    sstw = result['4 Social security tax withheld']
    mwat = result['5 Medicare wages and tips']
    mtw = result['6 Medicare tax withheld']
    sst = result['7 Social security tips']
    at = result['8 Allocated tips']
    dcb = result['10 Dependent Care Benefits']
    if '11 Nonqualiﬁed plans' in result:
        np = result['11 Nonqualiﬁed plans']
    else:
        np = []
    if '12a See instructions for box 12' in result:
        bx_12a = result['12a See instructions for box 12'][0]
    else:
        bx_12a = result['12 See Instructions for box 12'][0]
    if '12b Not defined' in result:
        bx_12b = result['12b Not defined']
    else:
        bx_12b = []
    if '12c Not defined' in result:
        bx_12c = result['12c Not defined']
    else:
        bx_12c = []
    if '12d Not defined' in result:
        bx_12d = result['12d Not defined']
    else:
        bx_12d = []
    bx_13_se = result['Statutory employee']
    bx_13_rp = result['Retirement plan']
    bx_13_tpsp = result['Third-party sick pay']
    if len(result['14 Other']) != 0:
        bx_14_type = result['14 Other'][0].split(" ")[0]
        bx_14_amount = result['14 Other'][0].split(" ")[1]
    else:
        bx_14_type = []
        bx_14_amount = []
    if "|" in result['15 State Employer‘s state ID number'][0]:
        state = result['15 State Employer‘s state ID number'][0].split("|")[0]
        esin = result['15 State Employer‘s state ID number'][0].split("|")[1]
    else:
        state = result['15 State Employer‘s state ID number'][0]
        esin = result["Employer's State ID Number"][0]
    for _ in range(10):
        if ' ' in esin:
            if type(esin) != list:
                tmp = list(esin)
                tmp.remove(' ')
                esin = "".join(tmp)
            else:
                esin.remove(' ')
        else:
            break

    swte = result['16 State wages, tips, etc']
    sit = result['17 State income tax']
    ln = result['20 Locality name']
    lwte = result['18 Local wages, tips, etc']
    lit = result['19 Local income tax']

    rdbs['1'] = ssn
    rdbs['2'] = first_name
    rdbs['3'] = last_name
    rdbs['4'] = state_zip[1]
    rdbs['5'] = street
    rdbs['6'] = city
    rdbs['7'] = state_zip[0]
    rdbs['8'] = EIN
    rdbs['9'] = employer_name
    rdbs['10'] = employer_zip
    rdbs['11'] = employer_street
    rdbs['12'] = employer_city
    rdbs['13'] = employer_state
    rdbs['14'] = wtc
    rdbs['15'] = fitw
    rdbs['16'] = ssw
    rdbs['17'] = sstw
    rdbs['18'] = mwat
    rdbs['19'] = mtw
    rdbs['20'] = sst
    rdbs['21'] = at
    rdbs['22'] = dcb
    rdbs['23'] = np
    rdbs['24'] = bx_12a
    rdbs['25'] = bx_12b
    rdbs['26'] = bx_12c
    rdbs['27'] = bx_12d
    rdbs['28'] = bx_13_se
    rdbs['29'] = bx_13_rp
    rdbs['30'] = bx_13_tpsp
    rdbs['31'] = bx_14_type
    rdbs['32'] = bx_14_amount
    rdbs['33'] = state
    rdbs['34'] = esin
    rdbs['35'] = swte
    rdbs['36'] = sit
    rdbs['37'] = ln
    rdbs['38'] = lwte
    rdbs['39'] = lit
    return rdbs