from django.http import HttpResponse, Http404
from django.shortcuts import render

from quiz.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-created_at')[:5]
    context = {
        'latest_question_list': latest_question_list,
        }
    return render(request, 'quiz/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Oh mince... Ce quiz n'existe pas !")
    return render(request, 'quiz/detail.html', {"question": question})

def results(request, question_id):
    return HttpResponse(f"Vous regardez les résultats de la question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Vous répondez à la question {question_id}")
