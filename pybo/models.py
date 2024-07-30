from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, verbose_name='タイトル')
    content = models.TextField(verbose_name='内容')
    PUBLIC_METHOD_CHOICES = [
        ('time', '時刻公開'),
        ('immediate', 'すぐ公開'),
        ('hold', '保留'),
    ]
    public_method = models.CharField(
        max_length=20,
        choices=PUBLIC_METHOD_CHOICES,
        default='time',
        verbose_name='公開方式'
    )
    PUSH_CHOICES = [
        ('push-on', '通知する'),
        ('push-off', '通知しない'),
    ]
    push = models.CharField(
        max_length=20,
        choices=PUSH_CHOICES,
        default='push-on',
        verbose_name='プッシュ通知有無'
    )
    issued_date = models.DateTimeField(verbose_name='発信日時')
    expiry_date = models.DateTimeField(null=True, blank=True, verbose_name='満了日時')

    class Meta:
        verbose_name = 'お知らせ'
        verbose_name_plural = 'お知らせ'

    def __str__(self):
        return self.subject

    def get_push_display(self):
        return dict(self.PUSH_CHOICES).get(self.push)

    def get_public_display(self):
        return dict(self.PUBLIC_METHOD_CHOICES).get(self.public_method)