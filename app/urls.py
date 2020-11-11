from django.urls import path, include
from . import views
from .views import QuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', QuestionViewSet)

urlpatterns = [
    path('q/', include(router.urls)),
    # опросы
    path('poll/create/', views.poll_create, name='poll_create'),
    path('poll/update/<int:poll_id>/', views.poll_update, name='poll_update'),
    path('poll/view/', views.polls_view, name='polls_view'),
    path('poll/view/active/', views.active_polls_view, name='active_poll_view'),
    # вопрсы
    path('question/create/', views.question_create, name='question_create'),
    path('question/update/<int:question_id>/', views.question_update, name='question_update'),
    # выбор
    path('choice/create/', views.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', views.choice_update, name='choice_update'),
    # ответы
    path('answer/create/', views.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', views.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', views.answer_update, name='answer_update')
]
