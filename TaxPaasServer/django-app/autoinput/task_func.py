import ast

from PIL import Image
from django_rq import job
from rq import get_current_job

from autoinput.functions.w2 import w2_total_process
from autoinput.functions.int import int_total_proces
from autoinput.models import Task, W2
from autoinput.serializers import W2Serializer

ast.literal_eval("{'x':1, 'y':2}")


@job
# 나중에 name을 사용해서 my_source_dic인지 판별??
# user가 추가되면 source doc에 w2_autocomplete 함수에서 연결
def w2_autocomplete(np_arr, pk):
    job = get_current_job()

    task = Task.objects.create(
        job_id=job.get_id()
    )
    img = Image.fromarray(np_arr)
    task.result, st, end = w2_total_process(img=img)

    if task.result:
        rdbs = task.result
        w2 = W2.objects.filter(pk=pk)[0]
        save_model(instance=w2, data=rdbs, st=st, end=end)

        # 완성 알림 보내기
        pass
    else:
        # 실패했을 경우 처리 규정 정하기
        pass
    task.save()
    return task.result


def save_model(instance=None, data=None, st=None, end=None):
    data['cut_start_points'] = str(st)
    data['cut_end_points'] = str(end)
    serializer = W2Serializer(instance, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()


def int_autocomplete(np_arr, pk):
    job = get_current_job()

    task = Task.objects.create(
        job_id=job.get_id()
    )
    img = Image.fromarray(np_arr)
    task.result, st, end = int_total_proces(img=img)

    if task.result:
        rdbs = task.result
        pass
    return None

