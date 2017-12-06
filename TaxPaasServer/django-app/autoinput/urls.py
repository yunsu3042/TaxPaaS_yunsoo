from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from autoinput.views import W2CreateView2, \
    W2DetailView2, SourceDocDetailView, SourceDocDetailView2, \
    W2TaskCreateView2, IntCreateView2, IntDetailView2, IntTaskCreateView, \
    DivTaskCreateView, DivDetailView2, DivCreateView2

urlpatterns = [
    url(r'source_doc/(?P<category>\w+)/(?P<doc_order>\d+)/$',
        SourceDocDetailView.as_view(), name='source_doc_detail'),
    url(r'source_doc/$',
        SourceDocDetailView2.as_view(), name='source_doc_detail'),

    url(r'w2/task/$',
        W2TaskCreateView2.as_view(), name='w2_task_create'),
    url(r'w2/(?P<pk>\d+)/$',
        W2DetailView2.as_view(), name='w2_detail'),
    url(r'w2/create/$',
        csrf_exempt(W2CreateView2.as_view()), name='w2_create'),

    url(r'int/task/$',
        IntTaskCreateView.as_view(), name='int_task_create'),
    url(r'int/(?P<pk>\d+)/$',
        IntDetailView2.as_view(), name='int_detail'),
    url(r'int/create/$',
        csrf_exempt(IntCreateView2.as_view()), name='int_create'),

    url(r'div/(?P<pk>\d+)/$',
        DivDetailView2.as_view(), name='div_detail'),
    url(r'div/task/$',
        DivTaskCreateView.as_view(), name='div_task_create'),
    url(r'div/create/$',
        csrf_exempt(DivCreateView2.as_view()), name='div_create'),
]

