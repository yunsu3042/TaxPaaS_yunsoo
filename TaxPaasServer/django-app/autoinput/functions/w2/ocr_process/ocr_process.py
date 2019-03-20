import pytesseract
import cv2
import numpy as np
from autoinput.functions import *
from PIL import Image
from autoinput.functions.decorator import timeit

__all__ = ('ocr_process', 'solve_13box')

@timeit
# ocr Process
def ocr_process(img_list):
    page = []
    if len(pytesseract.image_to_string(img_list[0])) >= 3:
        #그렇다면 2016버전입니다.
        print("version for 2016")
        for idx, img in enumerate(img_list):
            if idx != 18:
                page.append(pytesseract.image_to_string(img))
            elif idx == 18:
                solved_box = solve_13box(img_list[18])
                # 리스트를 풀어서 각각 넣기.
                for data in solved_box:
                    page.append(data)
    else:
        # 그렇다면 2014 버전입니다.
        print('version for 2014')
        for img in img_list:
            page.append(pytesseract.image_to_string(img))
    return page

@timeit
def solve_13box(img, show=False):
    src = np.array(img)
    if img.mode != 'L':
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    else:
        gray = src
    img = Image.fromarray(gray)
    joints, mask, line_wit, v_size2, h_final, v_final = find_box_joints(img)
    one_line = make_points_list(joints=joints, line_wit=line_wit, v_size2=v_size2)
    points = align_small_box_points(one_line=one_line, joints=joints)
    if show == True:
        box = make_box(points, joints, v_size2, line_wit)
        show_box(box=box, mask=mask)
    c_points = give_conditions(points=points, mask=mask, v_size2=v_size2, line_wit=line_wit)
    is_st, is_bot, is_end, is_right = classify_points(c_points=c_points, joints=joints, v_size2=v_size2,
                                                      line_wit=line_wit, mask=mask, points=points)
    st, end = cut_points(joints=joints, is_st=is_st, is_bot=is_bot, is_end=is_end, is_right=is_right)
    fix_st_0 = fix_st_vertical(h_final, st=st)
    fix_st_1 = fix_st_horizontal(v_final, st=st)
    st = fix_st(st, fix_st_0=fix_st_0, fix_st_1=fix_st_1)

    img = Image.fromarray(gray)
    img_list = make_crack(ful_img=img, st=st, end=end)
    choice = ['Statutory Employee', 'Retirement Plan', 'Third-party sick pay']
    result = []
    for idx, image in enumerate(img_list):
        gr = np.array(image)
        ret, thresh = cv2.threshold(gr, 70 ,255, cv2.THRESH_BINARY_INV)
        print(np.sum(thresh)/thresh.size)
        if np.sum(thresh)/thresh.size > 5:
            result.append("{}\nY".format(choice[idx]))
        else:
            result.append("{}\nN".format(choice[idx]))
    return result