from django import forms
from django.contrib.comments.models import Comment
from qna.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text', 'tags')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
