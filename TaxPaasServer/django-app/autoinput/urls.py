from django.conf.urls import url

from autoinput.views import W2TaskCreateView, W2CreateView, W2DetailView

urlpatterns = [
    url(r'w2/task/$', W2TaskCreateView.as_view(), name='w2_task_create'),
    url(r'w2/create/$', W2CreateView.as_view(), name='w2_create'),
    url(r'w2/(?P<category>\w+)/$', W2DetailView.as_view(), name='w2_detail'),

]