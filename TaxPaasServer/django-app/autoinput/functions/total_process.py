from . import pre_process, ocr_process, post_process1, post_process2, insert_data
import pickle
from unipath import Path

dic_path = Path(__file__).ancestor(2).child('dictionary')
w2_path = dic_path.child('w2_dictionary.pk1')


def autocomplete(url=None):
    with open(w2_path, 'rb') as f:
        w2_dic = pickle.load(f)
    img_list = pre_process(url,show=False)
    page = ocr_process(img_list)
    result = post_process1(page=page, w2_dic=w2_dic)
    rdbs = post_process2(result=result)
    return rdbs