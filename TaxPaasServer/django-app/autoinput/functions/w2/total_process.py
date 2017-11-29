import pickle

from unipath import Path

from . import pre_process, ocr_process, post_process1, post_process2
dic_path = Path(__file__).ancestor(3).child('dictionary')
w2_path = dic_path.child('w2_dictionary.pk1')

__all__ = ('w2_total_process', )


def w2_total_process(url=None, img=None):
    with open(w2_path, 'rb') as f:
        w2_dic = pickle.load(f)
    img_list, st, end = pre_process(url=url, img=img, show=False)
    page = ocr_process(img_list)
    result = post_process1(page=page, w2_dic=w2_dic)
    rdbs = post_process2(result=result)
    return rdbs, st, end