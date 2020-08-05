from django.conf.urls import url

from .views import test, \
    view_database, view_page_question, view_new_questions, view_popular_questions, \
    view_ask_form, view_signup_form, view_login_form

urlpatterns = [
    url(r'^$', view_new_questions, name='main-page'),
    url(r'login/', view_login_form),
    url(r'signup/', view_signup_form),
    url(r'question/(?P<id>\d+)/', view_page_question, name='page-question'),
    url(r'ask/', view_ask_form),
    url(r'popular/', view_popular_questions),
    url(r'new/', test),
    url(r'test/', view_database)
]
