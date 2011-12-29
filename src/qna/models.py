from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField

class Question(models.Model):
    title = models.CharField(_("Title"), max_length=140)
    text = models.TextField(_("Question text"))
    correct_answer = models.OneToOneField('Answer', null=True, blank=True, verbose_name=_("Answer"), related_name="+")
    tags = TagField(_("Tags"))
    date = models.DateTimeField(_("Creation date"))
    user = models.ForeignKey(User, verbose_name=_("User"))

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

class Comment(models.Model):
    text = models.TextField(_("Comment text"))
    date = models.DateTimeField(_("Creation date"))
    user = models.ForeignKey(User, verbose_name=_("User"))

    def __unicode__(self):
        return self.text[0:20]

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

class Rating(models.Model):
    positive = models.PositiveIntegerField()
    negative = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    user = models.ForeignKey(User)
