from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def save(self):
        question = Question.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            author=User.objects.get(pk=1),
        )
        return question


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def clean_question(self):
        question = self.cleaned_data['question']
        if question > Question.objects.count() or question < 1:
            raise forms.ValidationError('Invalid question number!')
        return question

    def save(self):
        answer = Answer.objects.create(
            text=self.cleaned_data['text'],
            question_id=self.cleaned_data['question'],
            author=User.objects.get(pk=1),
        )
