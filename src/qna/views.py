from django.shortcuts import render, get_object_or_404, get_list_or_404
from qna.models import Question

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    c = {}
    c["question"] = question
    return render(request, "qna/question.html", c)

def question_list(request):
    question_list = get_list_or_404(Question)
    c = {"question_list": question_list}
    return render(request, "qna/question_list.html", c)

def ask(request):
    c = {}
    return render(request, "qna/ask.html", c)
