import datetime
from django.db import models
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=50)
    rollno = models.IntegerField(default=0,primary_key=True)
    branch = models.CharField(max_length=5)
    year = models.IntegerField(default=0)
    # contact_no = models.IntegerField(default=0)

    def __str__(self):
        r=str(self.rollno)
        return r
        # return self.IntegerToString(rollno)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def ques(self):
        return self.question_text

class Vote(models.Model):
    student_id = models.IntegerField(default=0)
    question_id = models.IntegerField(default=0)
    vote = models.IntegerField(default=0)

    def __str__(self):
         st_id=str(self.student_id)
         return st_id

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_1 = models.CharField(max_length=200)
    choice_2= models.CharField(max_length=200)
    choice_3 = models.CharField(max_length=200)
    choice_4 = models.CharField(max_length=200)
    answer = models.IntegerField(default=0)

    def __str__(self):
        return self.question.question_text

    # def getChoice(self):
    #     li=[self.choice_1,self.choice_2,self.choice_3,self.choice_4]
    #     return li
    # return self.question cannot be used only string return type allowed

# Create your models here.
