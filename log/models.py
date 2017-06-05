from django.db import models
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.
class Subquestion(models.Model):
	question=models.CharField(max_length=1000)
	difficulty=models.IntegerField(choices=[(2,'hard'),(1,'medium'), (0,'easy')])
	category=models.IntegerField(choices=[(0,'C'),(1,'Operating System'), (2,'Microprossesor')])
	class Meta:
		db_table="sbquestion"
	def __str__(self):
		return 'Q:' + self.question 

class Mcqquestion(models.Model):
	question=models.CharField(max_length=1000)
	difficulty=models.IntegerField(choices=[(2,'hard'),(1,'medium'), (0,'easy')])
	category=models.IntegerField(default='C',choices=[(0,'C'),(1,'Operating System'), (2,'Microprossesor')])
	option1=models.CharField(max_length=50)
	option2=models.CharField(max_length=50)
	option3=models.CharField(max_length=50)
	option4=models.CharField(max_length=50)
	answer=models.IntegerField(default=0,choices=[(0,'A'),(1,'B'), (2,'C'),(3,'D')])
	class Meta:
		db_table="mcqquestion"
	def __str__(self):
		return 'Q:' + self.question
class McqTextFile(models.Model):
    mcq = models.FileField(storage=FileSystemStorage(location='/path/to/mcq'))
    answer = models.FileField(storage=FileSystemStorage(location='/path/to/answer'))
class SubTextFile(models.Model):
    sub = models.FileField(storage=FileSystemStorage(location='/path/to/sub'))