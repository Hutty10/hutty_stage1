from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class StageOneUser(models.Model):
    slackUsername = models.CharField(_("slack username"), max_length=50)
    backend = models.BooleanField(_("backend user"), default=True)
    age = models.PositiveSmallIntegerField(_("user age"))
    bio = models.TextField(_("description about yourself"))
