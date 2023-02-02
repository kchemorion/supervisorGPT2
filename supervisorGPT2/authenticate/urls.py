from django.urls import path
from . import views
from .views import QuestionListView, AskQuestionView, UserQuestionListView, QuestionDetailApiView, QuestionAnswerApiView, QuestionDetailView


app_name = 'authenticate'

urlpatterns = [
    path('questions/', views.QuestionListView.as_view(), name='question_list'),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('questions/ask/', views.AskQuestionView.as_view(), name='ask_question'),
#    path('my-questions/', views.UserQuestionListView.as_view(), name='user_questions'),
    path('question-detail-api/', views.QuestionDetailApiView.as_view(), name='question_detail_api'),
    path('question-answer-api/', views.QuestionAnswerApiView.as_view(), name='question_answer_api'),
    path('', views.home, name='home'),



]
