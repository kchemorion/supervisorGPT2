from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse
from authenticate.models import Question, Answer
from authenticate.forms import UpdateQuestionForm, AskQuestionForm
from django.shortcuts import render, get_object_or_404
from .models import Question, QuestionType, User, UserQuestion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from authenticate.models import Question, Answer
from .forms import AskQuestionForm
import openai 
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Question

def home(request):
    return render(request, 'main_page.html')

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_detail.html', {'question': question})

def user_questions(request, username):
    user = get_object_or_404(User, username=username)
    user_questions = user.questions.all()
    return render(request, 'user_questions.html', {'user_questions': user_questions})

def ask_question(request, pk):
    question_type = get_object_or_404(QuestionType, pk=pk)
    if request.method == 'POST':
        form = UserQuestionForm(request.POST)
        if form.is_valid():
            user_question = form.save(commit=False)
            user_question.question_type = question_type
            user_question.user = request.user
            user_question.save()
            response = get_answer_from_openai(user_question.question_text)
            return render(request, 'ask_question.html', {'response': response})
    else:
        form = UserQuestionForm()
    return render(request, 'ask_question.html', {'form': form})

def get_answer_from_openai(question):
    model_engine = "text-davinci-002"
    prompt = (f"{question}")
    completions = OpenAI.completion(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
    message = completions.choices[0].text
    return message

class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'

class AskQuestionView(View):
    template_name = 'ask_question.html'
    form_class = AskQuestionForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_list')
        return render(request, self.template_name, {'form': form})


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'

    def get_object(self, queryset=None):
        question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        return question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(question=self.object)
        return context

@login_required
class UserQuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'user_questions.html'
    context_object_name = 'user_questions'

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)

class QuestionDetailApiView(View):
    def get(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['pk'])
        return JsonResponse({'question': question.question_text})

class QuestionAnswerApiView(View):
    def post(self, request, *args, **kwargs):
        question = Question.objects.get(id=kwargs['pk'])
        answer = request.POST.get('answer')
        a = Answer(question=question, answer_text=answer)
        a.save()
        return JsonResponse({'answer': answer})
