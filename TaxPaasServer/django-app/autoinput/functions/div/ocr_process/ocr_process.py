import pytesseract

from autoinput.functions.decorator import timeit

__all__ = ('ocr_process', )

@timeit
def ocr_process(img_list=None):
    print("div 페이지 ocr 진행")
    page = []

    for img in img_list:
        page.append(pytesseract.image_to_string(img))
    return page