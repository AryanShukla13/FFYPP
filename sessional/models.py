from django.db import models
from django.contrib.auth.models import User

class Sessional(models.Model):
    subject = models.CharField(max_length=25)

class SessionalStudentMapping(models.Model):
    total_marks_student = models.IntegerField()
    sessional = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Sessional, on_delete=models.CASCADE)

class Question(models.Model):
    co = models.CharField(max_length=3)
    maximum_marks = models.IntegerField()
    sessional = models.ForeignKey(Sessional, on_delete=models.CASCADE, null=True, blank=True)

class QuestionStudentMapping(models.Model):
    marks_obtained = models.IntegerField(default=0)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sessional = models.ForeignKey(Sessional, on_delete=models.CASCADE)
