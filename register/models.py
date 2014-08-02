from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
# Create your models here.

class Registration(Page,RichText):
    def __unicode__(self):
            return self.title
class RegisterInfo(models.Model):
    form = models.ForeignKey("Registration")
    date = models.DecimalField()
    name = models.CharField(max_length=50)
    workplace = models.CharField(max_length=200)
    jobtime = models.DecimalField()
    graduate = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.DecimalField()
    resume = models.TextField()
    separate = models.CharField(max_length=10)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    remark = models.CharField(max_length=10)
    invoice = models.CharField(max_length=100)
    referrer = models.CharField(max_length=100)
