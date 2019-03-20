from . import pre_process, ocr_process, make_int_dic, post_process

__all__ = ('int_total_process', )


def int_total_process(url=None, img=None):
    img_list, st, end = pre_process(url=url, img=img)
    page = ocr_process(img_list=img_list)
    reference_dic = make_int_dic()
    rdbs = post_process(page=page, reference_dic=reference_dic, img=img)
    return rdbs, st, end
