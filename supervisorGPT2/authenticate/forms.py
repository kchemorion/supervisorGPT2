from django import forms
from authenticate.models import Question, QuestionType

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'question_type', 'description']
        
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    question_type = forms.ModelChoiceField(queryset=QuestionType.objects.all(), empty_label='Select a category', widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description', 'rows': 4}))

class UpdateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'question_type', 'description']
        
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    question_type = forms.ModelChoiceField(queryset=QuestionType.objects.all(), empty_label='Select a category', widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description', 'rows': 4}))
