from django.conf.urls.defaults import patterns
from qna import views

urlpatterns = patterns('',
    (r'^question/(\d+)/$', views.question),
)
