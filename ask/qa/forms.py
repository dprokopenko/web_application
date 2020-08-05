from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()

    def clean(self):
        if not self.user.is_authenticated:
            raise forms.ValidationError('Need to login')

    def save(self):
        question = Question.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            author=self.user,
        )
        return question


class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()

    def clean_question(self):
        question = self.cleaned_data['question']
        if question > Question.objects.count() or question < 1:
            raise forms.ValidationError('Invalid question number')
        return question

    def clean(self):
        if not self.user.is_authenticated:
            raise forms.ValidationError('Need to login')

    def save(self):
        answer = Answer.objects.create(
            text=self.cleaned_data['text'],
            question_id=self.cleaned_data['question'],
            author=self.user,
        )


class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('User with the same username already exists')
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise forms.ValidationError('User with the same email already exists')
        except User.DoesNotExist:
            return email

    def save(self):
        return User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError('Invalid username/password')
