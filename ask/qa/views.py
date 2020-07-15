from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def view_database(request):
    return render(request, 'view_database.html', {
        "questions": Question.objects.new(),
    })


def view_page_question(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'view_page_question.html', {
        "question": question,
    })


def view_new_questions(request):
    page = request.GET.get('page', 1)
    questions = Question.objects.new()
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'view_new_questions.html', {
        "page": page,
    })


def view_popular_questions(request):
    page = request.GET.get('page', 1)
    questions = Question.objects.popular()
    limit = 10
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'view_popular_questions.html', {
        "page": page,
    })
