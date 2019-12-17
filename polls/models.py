import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('발행날짜')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 이 Question의 pub_date가 (현재시간 - 1일) 보다 크거나 같은여부
        # 이 Question이 발행된지 24시간 이내인지 여부
        return self.pub_date >= timezone.now() - datetime.timedelta(dates=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
