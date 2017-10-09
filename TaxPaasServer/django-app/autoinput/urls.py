from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from taxpaas import settings
from autoinput.views.w2_detail import W2TaskCreateView
urlpatterns = [
    url(r'w2/task/$', W2TaskCreateView.as_view(), name='w2_task_create'),

]