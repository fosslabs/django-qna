from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField

class Question(models.Model):
    title = models.CharField(_("Title"), max_length=140)
    text = models.TextField(_("Question text"))
    correct_answer = models.OneToOneField('Answer', null=True, blank=True, verbose_name=_("Answer"), related_name="+")
    tags = TagField(_("Tags"))
    date = models.DateTimeField(_("Creation date"))
    user = models.ForeignKey(User, verbose_name=_("User"))

    @models.permalink
    def get_absolute_url(self):
        return ('qna.views.question', [self.id])

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

class Answer(models.Model):
    text = models.TextField(_("Answer text"))
    question = models.ForeignKey(Question, verbose_name=_("Question"))
    date = models.DateTimeField(_("Creation date"))
    user = models.ForeignKey(User, verbose_name=_("User"))

    def __unicode__(self):
        return self.text[0:20]

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
