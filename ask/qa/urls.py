from django.conf.urls import url

from .views import test, view_database, view_page_question, view_new_questions, view_popular_questions

urlpatterns = [
    url(r'^$', view_new_questions),
    url(r'login/', test),
    url(r'signup/', test),
    url(r'question/(?P<id>\d+)/', view_page_question, name='page-question'),
    url(r'ask/', test),
    url(r'popular/', view_popular_questions),
    url(r'new/', test),
    url(r'test/', view_database)
]
