from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Question, Answer
from .forms import AskForm, AnswerForm
from django.urls import reverse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def view_database(request):
    return render(request, 'view_database.html', {
        'questions': Question.objects.new(),
    })


def view_page_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('page-question', args=[
                id,
            ]))
    else:
        form = AnswerForm()
    return render(request, 'view_page_question.html', {
        'question': question,
        'form': form,
    })


def view_new_questions(request):
    page = request.GET.get('page', 1)
    questions = Question.objects.new()
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'view_new_questions.html', {
        'page': page,
    })


def view_popular_questions(request):
    page = request.GET.get('page', 1)
    questions = Question.objects.popular()
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'view_popular_questions.html', {
        'page': page,
    })


def view_ask_form(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse('page-question', args=[
                question.id,
            ]))
    else:
        form = AskForm()
    return render(request, 'view_ask_form.html', {
        'form': form,
    })
