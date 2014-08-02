# -*-coding:utf-8-*-
from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField
from django.core.validators import MaxValueValidator
# Create your models here.


class Registration(Page, RichText):
        response = RichTextField(verbose_name="Response")

        def __unicode__(self):
                return self.title


class RegisterInfo(models.Model):
    date = models.PositiveSmallIntegerField(verbose_name="希望开课月份", validators=[MaxValueValidator(12)])
    name = models.CharField(verbose_name="姓名", max_length=50)
    workplace = models.CharField(verbose_name="机构及职位", max_length=200)
    jobtime = models.PositiveSmallIntegerField(verbose_name="担任该职时间(年)")
    graduate = models.CharField(verbose_name="毕业院校,所获学位", max_length=100)
    email = models.EmailField(verbose_name="E-mail")
    phone = models.PositiveSmallIntegerField(verbose_name="手机")
    resume = models.TextField(verbose_name="工作简历")
    separate = models.CharField(max_length=10, blank=True, editable=False)
    question1 = models.TextField(verbose_name="问题1")
    question2 = models.TextField(verbose_name="问题2")
    question3 = models.TextField(verbose_name="问题3")
    remark = models.CharField(max_length=10, blank=True, editable=False)
    invoice = models.CharField(verbose_name="发票抬头", max_length=100)
    referrer = models.CharField(verbose_name="推荐人", max_length=100)
    timestamp = models.DateTimeField(verbose_name="报名表提交时间", auto_now_add=True)

    def __unicode__(self):
            return "Form-"+str(self.id)
