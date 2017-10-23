from django.conf.urls import url

from autoinput.views import W2TaskCreateView, W2CreateView, W2CreateView2,\
    W2DetailView, W2DetailView2, SourceDocDetailView, SourceDocDetailView2, \
    W2TaskCreateView2

urlpatterns = [
    url(r'w2/task/(?P<category>\w+)/(?P<doc_order>\d+)/(?P<order>\d+)/$',
        W2TaskCreateView.as_view(), name='w2_task_create'),
    url(r'w2/create/(?P<category>\w+)/(?P<doc_order>\d+)/(?P<order>\d+)/$',
        W2CreateView.as_view(), name='w2_create'),
    url(r'w2/(?P<category>\w+)/(?P<doc_order>\d+)/(?P<order>\d+)/$',
        W2DetailView.as_view(), name='w2_detail'),
    url(r'source_doc/(?P<category>\w+)/(?P<doc_order>\d+)/$',
        SourceDocDetailView.as_view(), name='source_doc_detail'),

    url(r'source_doc/$',
        SourceDocDetailView2.as_view(), name='source_doc_detail'),
    url(r'w2/task/$',
        W2TaskCreateView2.as_view(), name='w2_task_create'),
    url(r'w2/create/$',
        W2CreateView2.as_view(), name='w2_create'),
    url(r'w2/(?P<pk>\d+)/$',
        W2DetailView2.as_view(), name='w2_detail'),
]

