from django.db import models

class QuestionType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    response = models.TextField()
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class User(models.Model):
    username = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question, through='UserQuestion')

    def __str__(self):
        return self.username

class UserQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date_answered = models.DateTimeField(auto_now_add=True)
