from django.conf.urls.defaults import patterns
from qna import views
from qna.models import Question
from voting.views import xmlhttprequest_vote_on_object

urlpatterns = patterns('',
    (r'^question/ask/$', views.ask),
    (r'^question/(\d+)/$', views.question),
    (r'^question/(\d+)/answer/$', views.answer),
    (r'^question/comment/(\d+)/$', views.comment),
    (r'^question/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/$',
        xmlhttprequest_vote_on_object, dict(model=Question)),
    (r'^$', views.question_list),
)
