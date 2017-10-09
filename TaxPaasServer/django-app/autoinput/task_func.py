from autoinput.functions.w2 import autocomplete
import django_rq
from autoinput.models import Task
from django_rq import job
from rq import get_current_job
import requests
from PIL import Image

@job
# PIL Image객체가 Job decorator와 오류가 나는 경우가 발생해 img를 받지 않고 numpy를 넘겨준다
# 추가 시간 0.006 sec
# 나중에 name을 사용해서 my_source_dic인지 판별??
# user가 추가되면 source doc에 w2_autocomplete 함수에서 연결
def w2_autocomplete(np_arr, name):
    job = get_current_job()

    task = Task.objects.create(
        name=name,
        job_id=job.get_id()
    )
    img = Image.fromarray(np_arr)
    task.result = autocomplete(img=img)
    if task.result:
        # 완성 알림 보내기
        pass
    else:
        # 실패했을 경우 처리 규정 정하기
        pass
    task.save()
    return task.result
