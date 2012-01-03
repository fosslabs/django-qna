from django.shortcuts import render, get_object_or_404
from qna.models import Question

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    c = {}
    c["question"] = question
    return render(request, "qna/question.html", c)
