from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.conf import settings
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from qna.models import Question, Answer
from qna.forms import QuestionForm, AnswerForm, CommentForm
from datetime import datetime

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    c = {}
    c["question"] = question
    return render(request, "qna/question.html", c)

def question_list(request):
    question_list = get_list_or_404(Question)
    c = {"question_list": question_list}
    return render(request, "qna/question_list.html", c)

@login_required
def ask(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        try:
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect(question)
        except ValueError:
            return render(request, "qna/ask.html", {"error": True})
    else:
        c = {}
        return render(request, "qna/ask.html", c)

@login_required
@require_POST
def answer(request, question_num):
    c = {}
    form = AnswerForm(request.POST)
    question = get_object_or_404(Question, pk=question_num)
    try:
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()
    except ValueError:
        c['answer_error'] = True
    return redirect(question)

@login_required
@require_POST
def comment(request, answer_num):
    c = {}
    form = CommentForm(request.POST)
    answer = get_object_or_404(Answer, pk=answer_num)
    site = get_object_or_404(Site, pk=settings.SITE_ID)
    try:
        comment = form.save(commit=False)
        comment.user = request.user
        comment.content_object = answer
        comment.submit_date = datetime.now()
        comment.site = site
        comment.save()
    except ValueError:
        c['comment_error'] = True
    return redirect(answer.question)
