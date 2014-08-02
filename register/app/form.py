# -*-coding:utf-8-*-
from django import forms
from app.models import RegisterInfo


class RegisterForm(forms.ModelForm):
        separate = forms.ChoiceField(label="您对课程的期待",
                        widget=forms.RadioSelect,
                        required=False,
                        help_text="以下三个问题将帮助培训师了解学员需求，以便对课堂设计作相应的调整。")
        remark = forms.ChoiceField(label="备注", widget=forms.RadioSelect, required=False)

        class Meta:
                model = RegisterInfo
                fields = ['date', 'name', 'workplace', 'jobtime', 'graduate', 'email', 'phone', 'resume', 'separate', 'question1', 'question2', 'question3', 'remark', 'invoice', 'referrer']
                labels = {
                    'date': '你希望报名哪期“秘书长必修课”',
                    'name': '姓名',
                    'workplace': '机构和职位',
                    'jobtime': '担任该职位时间(年)',
                    'graduate': '毕业院校及所获学位',
                    'email': 'E-mail',
                    'phone': '电话',
                    'resume': '简历',
                    'question1': '1.您对本次课程的总体期望:',
                    'question2': '2.您在“秘书长必修课”9个课程领域中有哪些特别想了解的问题？',
                    'question3': '3.您所在基金会最迫切需要解决的问题:',
                    'invoice': '请填写学费发票抬头(重要)',
                    'referrer': '您是否由他人推荐参加此次课程？',
                }
                help_texts = {
                    'date': '请填写开课月份',
                    'question2': '“秘书长必修课”9门课程分别是：管理革命、治理博弈、战略框架、有效公益、品牌建设、筹资迷思、战略财务与激活资产和团队激励。详细课程介绍请参考：http://www.foundationcenter.org.cn/ftc/class.html 课程简介页面。',
                    'invoice': '注明机构或个人全称，发票抬头将以此为准。',
                    'referrer': '请填写推荐人姓名。',
                }
