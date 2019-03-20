import copy
import math
import cv2
import numpy as np
import sys
import os
from PIL import Image
main_package = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))
sys.path.append(main_package)
from autoinput.functions.decorator import timeit, is_w2

__all__ = ('pre_process', 'find_joints', 'find_box_joints', 'check_line_wit',
           'check_max_line_wit', 'make_points_list', 'align_points',
           'make_box', 'make_crack', 'show_box', 'give_conditions',
           'classify_points', 'cut_points', 'fix_st', 'fix_st_vertical',
           'fix_st_horizontal', 'align_small_box_points', 'capture_checkbox')

@timeit
@is_w2
def find_joints(image=None):
    if image.mode != "L":
        gray = image.convert("L")
    else:
        gray = image
    gray = np.array(gray)

    # 이미지 전처리_ 잡티제거 및 색 진하게
    cleaned_img = cv2.adaptiveThreshold(~gray, 255,
                                        cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY,
                                        11,
                                        -2)
    horizontal = cleaned_img.copy()
    vertical = cleaned_img.copy()

    # v_size와 v_size2는 중요하다. v_size는 전체 이미지 높이의 1/20에 해당되는 길이의 수직선부터 테이블을 구성할 수 있다고 생각하는 것.
    # adjust_value는 수평선과 수직선의 교차점을 찾을 때 확실히 해주기 위해 도와주는 추가적인 코드다.
    v_size = vertical.shape[0] // 20
    adjust_value = max(1, vertical.shape[0] // 100)
    vertical_struct = cv2.getStructuringElement(cv2.MORPH_RECT, (1, v_size))
    vertical_adjust = cv2.getStructuringElement(cv2.MORPH_RECT,
                                                (1, adjust_value))
    v_final = cv2.erode(vertical, vertical_struct, iterations=1)


    h_size = horizontal.shape[1] // 20
    horizontal_struct = cv2.getStructuringElement(cv2.MORPH_RECT, (h_size, 1))
    horizontal_adjust = cv2.getStructuringElement(cv2.MORPH_RECT,
                                                  (adjust_value, 1))
    h_final = cv2.erode(horizontal, horizontal_struct, iterations=1)
    h_final = cv2.dilate(h_final, horizontal_struct, iterations=1)
    v_final = cv2.dilate(v_final, vertical_struct, iterations=1)


    for h in range(v_final.shape[0]):
        if 255 in v_final[h, :]:
            p_high = h
            print("가장 높은 점: {}".format(p_high))
            break

    for h in range(h_final.shape[0]):
        if 255 in h_final[h, :]:
            p_high_check = h
            print("가장 높은 점 체크: {}".format(p_high_check))
            break

    for h in range(v_final.shape[0]):
        if 255 in v_final[-h, :]:
            p_low = v_final.shape[0] - h
            print("가장 낮은 점: {}".format(p_low))
            break
    for w in range(h_final.shape[1]):
        if 255 in h_final[:, w]:
            p_left = w
            print("가장 왼쪽 점: {}".format(p_left))
            break
    for w in range(h_final.shape[1]):
        if 255 in h_final[:, -w]:
            p_right = v_final.shape[1] - w
            print("가장 오른쪽 점: {}".format(p_right))
            break
    # 열려있는 윤곽선을 닫아주는 기능.
    h_final[p_high, p_left:p_right] = 255
    h_final[p_low, p_left:p_right] = 255
    v_final[p_high:p_low, p_left] = 255
    v_final[p_high:p_low, p_right] = 255

    h_final = cv2.dilate(h_final, horizontal_adjust, iterations=1)
    v_final = cv2.dilate(v_final, vertical_adjust, iterations=1)

    line_wit = check_line_wit(h_final)
    joints = cv2.bitwise_and(v_final, h_final)
    mask = h_final + v_final
    return joints, mask, line_wit, adjust_value, h_final, v_final


@timeit
@is_w2
# 0.06797 sec
def check_line_wit(h_final):
    # linewit은 나중에 이미지 자를 때 중요한 값이다. 선분의 두께에 따라서 이미지에 선분이 잘려 나타날 수 있다.
    # h_final은 수평선을 이루는 픽셀만 제외하고 모두 0으로 처리되어 있는 벡터
    # 테이블을 이루는 선의 두께중 가장 두꺼운 선의 두께를 찾아주는 함수.
    # 수평선을 이루는 픽섹들 중 값이 200이 넘는 픽셀은 명확도를 위해서 255로
    h_final[h_final >= 200] = 255
    wit = 0
    wit_list = []
    width = h_final.shape[1]
    height = h_final.shape[0]

    # h_final의 모든 값을 다 다니지 않고, 수평길이를 5가지로 나누어 각 점을 지나는 수직선 중 가장 두꺼운 선분의 길이를 찾으려고 작성.
    # numpy에서 [y_start: y_end, x_start: x_end]은 수직으로 가져올 좌표 시작과 끝값과 수평으로 가져올 좌표 시작과 끝값을 의미한다.
    # 즉 사각형을 가져온다.
    for point in list(map(lambda x: x * width // 20, range(20))):
        for p in h_final[:, point]:
            if p == 255:
                wit += 1
            else:
                wit_list.append(wit)
                wit = 0

    for point in list(map(lambda x: x * height // 20, range(20))):
        for p in h_final[:, point]:
            if p == 255:
                wit += 1
            else:
                wit_list.append(wit)
                wit = 0

    line_wit = max(wit_list)
    return line_wit


# joints에는 한 리전에도 수 많은 점들이 있는데 한 리전당 하나의 포인트만 남기기 위해서 사용한다.
# 2번 도는 코드를 한번만 도도록 리펙토링
# 10 sec
@timeit
@is_w2
def make_points_list(line_wit, v_size2, joints):
    re_joints = joints.copy()
    one_line = []
    iran = joints.shape[0]
    jran = joints.shape[1]
    for i in range(iran):
        for j in range(jran):
            # 값이 0이 아닌 리전을 찾으면, 선 두께를 기준으로 모두 0으로 초기화해준다.
            # 초기화 시킬 기준을 선 두께로 사용해서 주위에 있을 또 다른 테이블을 이루는 리전에 영향을 주지 않게 한다.
            # 초기화 된 후에는 i,j값을 기준으로 하나의 점의 픽셀값만 255로 바꾸어준다.
            if re_joints[i][j] != 0:
                re_joints[max(0, i - line_wit * 2): min(i + line_wit * 2,
                                                        joints.shape[0] - 1),
                max(0, j - line_wit * 2): min(j + line_wit * 2,
                                              joints.shape[1] - 1)] = 0
                re_joints[i][j] = 255
                one_line.append((i, j))
    return one_line


# 0.0001sec
@timeit
@is_w2
def align_points(one_line, joints):
    points = {}
    tmp = []
    k = 0
    fst = one_line[0]
    for pos in one_line:
        plow = fst[0]
        # allow는 경험적 데이터로, 테이블이 비틀어졌을 때를 대비해 allow만큼 비틀린 테이블까지는 인식하겠다는 말이다.
        allow = int(joints.shape[0] * 0.03)
        rng = range(max(0, plow - allow),
                    min(joints.shape[0] - 1, plow + allow))
        if pos[0] in rng:
            tmp.append(pos)
        else:
            tmp = sorted(tmp, key=lambda x: x[1])
            k += 1
            points['line' + str(k)] = tmp
            tmp = []
            fst = pos
            tmp.append(pos)
    k += 1
    points['line' + str(k)] = tmp
    return points


@timeit
@is_w2
def make_box(points, joints, v_size2, line_wit):
    # 점 주위에 박스처리 해주는 기능
    away_distance = max(3, v_size2 + line_wit)
    box = np.zeros_like(joints)
    for i in range(1, len(points) + 1):
        line = points['line' + str(i)]
        for idx, p in enumerate(line):
            box[max(0, p[0] - away_distance),
            max(0, p[1] - away_distance): min(joints.shape[1] - 1, p[1] + away_distance)] = 255
            box[max(0, p[0] - away_distance): min(joints.shape[0] - 1, p[0] + away_distance),
            max(0, p[1] - away_distance)] = 255
            box[min(joints.shape[0] - 1, p[0] + away_distance),
            max(0, p[1] - away_distance): min(joints.shape[1] - 1, p[1] + away_distance)] = 255
            box[
            min(joints.shape[0] - 1, p[0] - away_distance): min(joints.shape[0] - 1,
                                                        p[0] + away_distance),
            min(joints.shape[1] - 1, p[1] + away_distance)] = 255
    return box


@timeit
@is_w2
def show_box(box, mask):
    boxed = box + mask
    cv2.imshow('boxed', boxed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    return None



@timeit
@is_w2
def give_conditions(points, mask, v_size2, line_wit):
    # 좌표에 컨디션을 부과해주는 함수
    mask[mask > 240] = 255
    away_distance = max(3, v_size2 + line_wit * 2)
    line_width_x2 = line_wit * 2
    c_points = copy.deepcopy(points)
    margin_top = 0
    margin_left = 0
    margin_right = mask.shape[1] - 1
    margin_bot = mask.shape[0] - 1
    for i in range(1, len(c_points) + 1):
        line = c_points['line' + str(i)]
        for idx, p in enumerate(line):
            tmp = ''
            c1 = 255 in mask[max(0, p[0] - away_distance),
                        max(0, p[1] - line_width_x2): min(margin_right,
                                                  p[1] + line_width_x2)]
            c2 = 255 in mask[max(0, p[0] - line_width_x2): min(margin_bot,
                                                       p[0] + line_width_x2),
                        max(0, p[1] - away_distance)]
            c3 = 255 in mask[min(margin_bot, p[0] + away_distance),
                        max(0, p[1] - line_width_x2): min(margin_right,
                                                  p[1] + line_width_x2)]
            c4 = 255 in mask[min(margin_bot, p[0] - line_width_x2): min(
                margin_bot, p[0] + line_width_x2),
                        min(margin_right, p[1] + away_distance)]
            if c1:
                tmp += 'c1'
            if c2:
                tmp += 'c2'
            if c3:
                tmp += 'c3'
            if c4:
                tmp += 'c4'
            line[idx] = (p, tmp)
    return c_points


@timeit
@is_w2
def classify_points(c_points, joints, v_size2, line_wit, mask, points):
    # 좌표를 각각 시작점, 보조점, 끝점으로 분류해주는 기능.
    for depth_bound in range(2, 5):
        allow = int(joints.shape[1] * 0.02)
        is_st = []
        is_end = []
        is_right = []
        is_bot = []
        for i in range(1, len(c_points) + 1):
            line = c_points['line' + str(i)]
            for idx, p in enumerate(line):
                if 'c3c4' in p[1]:
                    is_st.append(p[0])
                if 'c1c2' in p[1]:
                    is_end.append(p[0])
                if 'c2c3' in p[1]:
                    is_right.append(p[0])
                if 'c1' in p[1] and 'c4' in p[1]:
                    is_bot.append(p[0])
        if len(is_st) == len(is_right) == len(is_bot) == len(is_end):
            break
        else:
            print("시작점과 다른 점들의 수가 맞지 않습니다.")
            print("depth를 더 줄여 수정진행합니다.")
            # 점 주위에 박스처리 해주는 기능
            up_line_wit = line_wit // depth_bound
            box = make_box(points, joints, v_size2, up_line_wit)
            show_box(box, mask)

            # 좌표에 컨디션을 부과해주는 함수
            c_points = give_conditions(points, mask, v_size2, up_line_wit)
    return is_st, is_bot, is_end, is_right

    # 자를 좌표를 정해주는 기능


@timeit
@is_w2
def cut_points(joints, is_st, is_bot, is_end, is_right):
    st = []
    end = []
    allow = int(joints.shape[1] * 0.02)
    # 스타트 다음에 나오는 right 는 무조건 직전 스타트와 사각형을 이룬다.
    for idx, p in enumerate(is_st):
        st.append(p)
        rgt = is_right[idx]
        for thing in is_bot:
            if thing[1] in range(p[1] - allow, p[1] + allow):
                bot = thing
                is_bot.remove(thing)
                break
        for thing in is_end:
            if thing[0] in range(bot[0] - allow, bot[0] + allow) and thing[
                1] in range(rgt[1] - allow, rgt[1] + allow):
                end.append(thing)
                is_end.remove(thing)
                break
    return st, end


@timeit
@is_w2
def fix_st_horizontal(v_final, st):
    allow = 3
    certain = 50
    assume_wit = 15
    v_final[v_final > 240] = 255
    fix_st_1 = []
    for start in st:
        for move in range(assume_wit):
            if 255 in v_final[max(0, start[0] + certain - allow): min(
                            v_final.shape[0] - 1, start[0] + certain + allow),
                      start[1] + assume_wit - move]:
                fix_st_1.append(assume_wit - move + 1)
                break
            if move == assume_wit - 1:
                fix_st_1.append(0)
    return fix_st_1


@timeit
@is_w2
# 각 테이블 윤곽선 두께가 다를 수 있기때문에 두께를 고려해서 시작점의 vertical 좌표에 더하거나 뺄 값을 계산한다.
# 인자는 v_final이 아니라 h_final이 들어간다는 점에 유의해야한다.
def fix_st_vertical(h_final, st):
    allow = 3
    certain = 20
    assume_wit = 15
    h_final[h_final > 240] = 255
    fix_st_0 = []
    for start in st:
        for move in range(1, assume_wit):
            # 시작점이 좌상단에 있기 때문에 실제 테이블의 굵기가 아닌 옆 테이블의 굵기를 측정할 수 있다. width에만 해당된다. 따라서 certain 값을 더해
            # 자신 테이블의 윗 수평선 굵기를 잰다.
            # start[0] 좌표에서 assume_wit만큼 내려오면 흰 여백에 위치한다. 이 곳에서 위쪽으로 조금씩(move)하면서 테이블 검은 선과 만날 때
            # start[0] 에서부터의 검은선까지의 거리를 계산한다. 이렇게하지 않으면 테이블 선 내부에 흰 공간이 있는 경우 오류를 내게 되서 이런 코드를
            # 짜게 되었다.
            # certain은 오른쪽으로 이동하는 값인데, 오른쪽으로 이동하지 않으면 옆에 테이블 윤곽선의 두께에 영향을 받기 때문에, 영향을 최소화하기 위해
            # 확실히 옆테이블과 떨어진 위치에서 떨어져(certain) 계산한다.
            # allow는 예측하지못한 상황에서 대비하기 위해 작성했는데, 상황에 따라 없어야 하는 코드가 될 수 있다.!
            if 255 in h_final[start[0] + assume_wit - move,
                      max(0, start[1] + certain - allow): min(
                                  h_final.shape[1] - 1,
                                  start[1] + certain + allow)]:
                fix_st_0.append(assume_wit - move + 1)
                break
            if move == assume_wit - 1:
                fix_st_0.append(0)
    return fix_st_0


@timeit
@is_w2
def fix_st(st, fix_st_1, fix_st_0):
    for idx, add in enumerate(zip(fix_st_0, fix_st_1)):
        tmp = st[idx][0] + add[0], st[idx][1] + add[1]
        st[idx] = tmp
    return st


@timeit
@is_w2
def make_crack(ful_img, st, end):
    img_list = []

    for i in range(len(st)):
        # +1을 해주는 이유, img는 시작값이 0이아닌 1이기 때문에 배열의 모양과 맞추려면 +1이 맞음.
        tmp = ful_img.crop(
            (st[i][1] + 1, st[i][0] + 1, end[i][1] - 1, end[i][0] - 1))
        # 글자가 작은 경우 잘못 읽는 경우가 생겨, 시간 비용이 들더라도 정확도를 올려주기 위해 이미지 사이즈를 2배로 늘린다.
        size = (tmp.size[0] * 2, tmp.size[1] * 2)
        tmp = tmp.resize(size)
        img_list.append(tmp)
    return img_list


@timeit
@is_w2
# 13번 박스를 위한 코드
def align_small_box_points(one_line, joints):
    points = {}
    tmp = []
    k = 0
    fst = one_line[0]
    for pos in one_line:
        plow = fst[0]
        # allow는 경험적 데이터로, 테이블이 비틀어졌을 때를 대비해 allow만큼 비틀린 테이블까지는 인식하겠다는 말이다.
        # 전체 테이블의 크기가 작고, 그안에 박스 테이블이 상대적으로 클 경우에 경험적 데이터로 10픽셀을 준다.
        allow = 10
        rng = range(max(0, plow - allow),
                    min(joints.shape[0] - 1, plow + allow))
        if pos[0] in rng:
            tmp.append(pos)
        else:
            tmp = sorted(tmp, key=lambda x: x[1])
            k += 1
            points['line' + str(k)] = tmp
            tmp = []
            fst = pos
            tmp.append(pos)
    k += 1
    points['line' + str(k)] = tmp
    return points


@timeit
@is_w2
def check_max_line_wit(h_final):
    h_final[h_final >= 200] = 255
    wit = 0
    wit_candidate = []
    line_wit_list = []
    for i in range(h_final.shape[1]):
        for p in h_final[:, i]:
            if p == 255:
                wit += 1
            else:
                wit_candidate.append(wit)
                wit = 0
        line_wit_list.append(max(wit_candidate))
    line_wit = max(line_wit_list)
    return line_wit


@timeit
@is_w2
def find_box_joints(image):
    # 이미지를 읽는다.
    src = np.array(image)
    if image.mode != 'L':
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    else:
        gray = src
    # 이미지 전처리_ 잡티제거
    bw = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 15, -5)
    horizontal = bw.copy()
    vertical = bw.copy()
    # v_size와 adjust_value는 중요하다. v_size는 전체 이미지 높이의 1/20에 해당되는 길이의 수직선부터 테이블을 구성할 수 있다고 생각하는 것.
    # adjust_value는 수평선과 수직선의 교차점을 찾을 때 확실히 해주기 위해 도와주는 추가적인 코드다.
    v_size = vertical.shape[0] // 3
    adjust_value = max(1, vertical.shape[0] // 100)
    vertical_struct = cv2.getStructuringElement(cv2.MORPH_RECT, (1, v_size))
    vertical_adjust = cv2.getStructuringElement(cv2.MORPH_RECT,
                                                (1, adjust_value))
    v_final = cv2.erode(vertical, vertical_struct, iterations=1)
    v_final = cv2.dilate(v_final, vertical_struct, iterations=1)
    v_final = cv2.dilate(v_final, vertical_adjust, iterations=1)
    h_size = horizontal.shape[1] // 30
    h_struct = cv2.getStructuringElement(cv2.MORPH_RECT, (h_size, 1))
    h_struct2 = cv2.getStructuringElement(cv2.MORPH_RECT, (adjust_value, 1))
    h_final = cv2.erode(horizontal, h_struct, iterations=1)
    h_final = cv2.dilate(h_final, h_struct, iterations=1)
    h_final = cv2.dilate(h_final, h_struct2, iterations=1)
    line_wit = check_max_line_wit(h_final)
    joints = cv2.bitwise_and(v_final, h_final)
    mask = h_final + v_final
    return joints, mask, line_wit, adjust_value, h_final, v_final


@timeit
@is_w2
def pre_process(url=None, img=None, show=False):
    print("W2 Image 전처리")
    if url:
        src = cv2.imread(url)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        image = Image.fromarray(gray)
        if src.all():
            print("None Type Error : 이미지를 받아오지 못했습니다.")
    if img:
        if img.mode != "L":
            image = img.convert("L")
        else:
            image = img

    joints, mask, line_wit, v_size2, h_final, v_final = find_joints(image=image)
    one_line = make_points_list(
        joints=joints, line_wit=line_wit, v_size2=v_size2
    )
    points = align_points(one_line=one_line, joints=joints)
    if show == True:
        box = make_box(points, joints, v_size2, line_wit)
        show_box(box=box, mask=mask)
    c_points = give_conditions(
        points=points, mask=mask, v_size2=v_size2, line_wit=line_wit
    )
    is_st, is_bot, is_end, is_right = classify_points(
        c_points=c_points, joints=joints, v_size2=v_size2, line_wit=line_wit,
        mask=mask, points=points)
    st, end = cut_points(joints=joints, is_st=is_st, is_bot=is_bot,
                         is_end=is_end, is_right=is_right)
    fix_st_0 = fix_st_vertical(h_final, st=st)
    fix_st_1 = fix_st_horizontal(v_final, st=st)
    st = fix_st(st, fix_st_0=fix_st_0, fix_st_1=fix_st_1)
    img_list = make_crack(ful_img=image, st=st, end=end)
    return img_list, st, end


def get_all_contours(img):
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(ref_gray, 230, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def get_apex(contour):
    # 이 함수는 꼭지점만을 반환합니다.
    # arcLength는 둘레의 길이를 반환한다. closed = True라면 폐곡선의 둘레를, False라면 열려있는 곡선의 시작점에서 끝 점까지의 거리를 측정한다.
    perimeter = cv2.arcLength(contour, True)
    # approxPolyDP는 꼭지점의 수를 줄이는 데 사용된다. epsilon값만큼 오차를 허용해서 꼭지점을 추출한다.
    approx = cv2.approxPolyDP(contour, epsilon=perimeter * 0.02, closed=True)
    return approx


class Point(object):
    def __init__(self, args):
        x, y = args
        self.x = x
        self.y = y

    def __str__(self):
        return (self.x, self.y)

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    @property
    def length(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length


def dot(a, b):
    x = a.x * b.x
    y = a.y * b.y
    return x + y


def is_rectangle(apex):
    if len(apex) != 4:
        return False
    points = apex.reshape(-1, 2)
    for index in range(4):
        p1 = Point(points[index])
        p2 = Point(points[(index + 1) % 4])
        p3 = Point(points[(index + 2) % 4])
        plist = (p1, p2, p3)
        cosine_result = cal_cosine(plist)
        if abs(cosine_result) <= 0.3:
            pass
        else:
            return False
    return True


def is_regular(apex):
    points = apex.reshape(-1, 2)
    perimeter = cv2.arcLength(apex, True)
    try:
        p1, p2, p3, p4 = [Point(var) for var in points]
    except ValueError:
        print("꼭지점의 개수가 4개가 아닙니다. ")
        return False
    a = get_length(p1, p2)
    b = get_length(p2, p3)
    c = get_length(p3, p4)
    d = get_length(p4, p1)
    aver = np.average([a, b, c, d])
    for x in [a, b, c, d]:
        percent_error = ((aver - x) / aver) * 100
        print(percent_error)
        if abs(percent_error) >= 15:
            return False
    return True


def get_length(a, b):
    x_dis = a.x - b.x
    y_dis = a.y - b.y
    squared_dis = x_dis ** 2 + y_dis ** 2
    result = math.sqrt(squared_dis)
    return result


def cal_cosine(args, **kwargs):
    p1, p2, p3 = args
    vector_a = p1 - p2
    vector_b = p3 - p2
    vector_dot = dot(vector_a, vector_b)
    result = vector_dot / (vector_a.length * vector_b.length)
    return result


def get_distance(a, b):
    result = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return result


def capture_checkbox(src):
    in_counter = 0
    contours = get_all_contours(src)
    filtered_contours = []
    print(len(contours))
    img_area = src.shape[0] * src.shape[1]
    for i, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if 0.0001 < area / img_area < 0.0005:
            pass
        else:
            continue
        cnt_apex = get_apex(cnt)
        if is_rectangle(cnt_apex):
            print("pass")
            pass
        else:
            continue
        if is_regular(cnt_apex):
            pass
        else:
            continue

        if in_counter >= 1:
            dif_condition = is_different(new=cnt_apex,
                                         ex=filtered_contours[in_counter - 1],
                                         src=src)
            if dif_condition == True:
                filtered_contours.append(cnt_apex)
                in_counter += 1

        else:
            filtered_contours.append(cnt_apex)
            in_counter += 1
    return filtered_contours


def is_different(new, ex, src):
    new = new.reshape(-1, 2)
    ex = ex.reshape(-1, 2)
    for k in range(4):
        if get_distance(ex[k], new[k]) <= 0.012 * np.sqrt(
                                src.shape[0] ** 2 + src.shape[1] ** 2):
            return False
    return True