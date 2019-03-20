import ast

from PIL import Image
from django_rq import job
from rq import get_current_job

from autoinput.functions.w2 import w2_total_process
from autoinput.functions.int import int_total_process
from autoinput.functions.div import div_total_process
from autoinput.models import Task, W2, Ten99INT, Ten99DIV
from autoinput.serializers import W2Serializer, Ten99INTSerializer,\
    Ten99DIVSerializer

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
        save_model(instance=w2, data=rdbs, st=st, end=end, serializer=W2Serializer)

        # 완성 알림 보내기
        pass
    else:
        # 실패했을 경우 처리 규정 정하기
        pass
    task.save()
    return task.result


def save_model(instance=None, data=None, st=None, end=None, serializer=None):
    data['cut_start_points'] = str(st)
    data['cut_end_points'] = str(end)
    serializer = serializer(instance, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()


@job
def int_autocomplete(np_arr, pk):
    job = get_current_job()

    task = Task.objects.create(
        job_id=job.get_id()
    )
    img = Image.fromarray(np_arr)
    task.result, st, end = int_total_process(img=img)

    if task.result:
        rdbs = task.result
        int_obj = Ten99INT.objects.filter(pk=pk)[0]
        save_model(instance=int_obj, data=rdbs, st=st, end=end,
                   serializer=Ten99INTSerializer)
        pass
    else:
        pass
    task.save()
    return task.result

@job
def div_autocomplete(np_arr, pk):
    job = get_current_job()

    task = Task.objects.create(
        job_id=job.get_id()
    )
    img = Image.fromarray(np_arr)
    task.result, st, end = div_total_process(img=img)

    if task.result:
        rdbs = task.result
        div = Ten99DIV.objects.filter(pk=pk)[0]
        save_model(instance=div, data=rdbs, st=st, end=end,
                   serializer=Ten99DIVSerializer)
        pass
    else:
        pass
    task.save()
    return task.result
