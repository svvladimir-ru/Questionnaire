from django.db import models


class Poll(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    pub_date = models.DateTimeField()
    # pub_date = models.DateTimeField("Дата старта", auto_now_add=True) - для автоматической подстановки даты создания
    end_date = models.DateTimeField()
    description = models.CharField(verbose_name='Описание', max_length=200)

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    q_text = models.CharField(max_length=200)
    q_type = models.CharField(max_length=200)

    def __str__(self):
        return self.q_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, related_name='poll', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.choice_text
