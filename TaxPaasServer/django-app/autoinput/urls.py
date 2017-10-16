from django.conf.urls import url

from autoinput.views import W2TaskCreateView, W2CreateView, W2DetailView,\
    SourceDocDetailView

urlpatterns = [
    url(r'w2/task/(?P<category>\w+)/(?P<doc_order>\d+)/(?P<order>\d+)/$',
        W2TaskCreateView.as_view(), name='w2_task_create'),
    url(r'w2/create/(?P<category>\w+)/(?P<doc_order>\d+)/(?P<order>\d+)/$',
        W2CreateView.as_view(), name='w2_create'),
    url(r'w2/(?P<category>\w+)/(?P<doc_order>\d+)/(?P<order>\d+)/$',
        W2DetailView.as_view(), name='w2_detail'),
    url(r'source_doc/(?P<category>\w+)/(?P<doc_order>\d+)/$',
        SourceDocDetailView.as_view(), name='source_doc_detail'),
]

