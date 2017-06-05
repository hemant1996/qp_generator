#!python
#log/views.py
from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from forms import subjectiveform,objectiveform,LoginForm
from django.template import RequestContext
from log.models import Subquestion,Mcqquestion
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from mimetypes import MimeTypes
from os.path import join, getsize
import random
import sys

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")
def home(request):
	if request.method=='POST':
		form=subjectiveform(request.POST) 
		form2=objectiveform(request.POST)
		if form.is_valid():
			difficulty=form.cleaned_data.get('difficulty')
			marks=form.cleaned_data.get('marks')
			subject=form.cleaned_data.get('subject')
		if form2.is_valid():
			difficulty=form.cleaned_data.get('difficulty')
			marks=form.cleaned_data.get('marks')
			subject=form.cleaned_data.get('subject')


	else:
		form = subjectiveform()
		form2= objectiveform()
	return render_to_response('home.html',{'form':form,'form2':form2},context_instance=RequestContext(request))
def download(request):

	if request.method=='POST':
		form=subjectiveform(request.POST)
		if form.is_valid():
			difficulty=form.cleaned_data.get('difficulty')
			marks=form.cleaned_data.get('marks')
			subject=form.cleaned_data.get('subject')
			x=Subquestion.objects.filter(category=subject,difficulty=difficulty).values_list('question')
			i=1
			f=open("new.txt","w")
			number=10
			if marks==50:
				number=5
			listy=[]
			for insert in range(number):
				listy.append(insert)
			random.shuffle(x)
			for r in listy:
				f.write("Q.%d %s \r\n" % (i,x[r][0]))
				i=i+1
			f.close()
			wrapper=open("new.txt","r")
			response=HttpResponse(wrapper, content_type='text/plain')
			response['Content-Length']=getsize('new.txt')
			response['Content-Disposition']="attachment; filename="+"subjective_paper.pdf"

			return response
def downloadmcq(request):
	reload(sys)
	sys.setdefaultencoding('utf-8')
	if request.method=='POST':
		form=objectiveform(request.POST)
		if form.is_valid():
			difficulty=form.cleaned_data.get('difficulty')
			marks=form.cleaned_data.get('marks')
			subject=form.cleaned_data.get('subject')
			x=Mcqquestion.objects.filter(category=subject,difficulty=difficulty).values_list('question','option1','option2','option3','option4','answer')
			i=1
			f=open("new.txt","w")
			number=int(marks)
			listy=[]
			for insert in range(number):
				listy.append(insert)
			random.shuffle(x)			
			for r in listy:
				f.write("Q.%d %s \r\n" % (i,x[r][0]))
				f.write("a.)%s\r\n" % (x[r][1]))
				f.write("b.)%s\r\n" % (x[r][2]))
				f.write("c.)%s\r\n" % (x[r][3]))
				f.write("d.)%s\r\n\n" % (x[r][4]))
				f.write("       Answer: %s\r\n\n" % (x[r][5]))
				i=i+1
			f.close()
			wrapper=open("new.txt","r")
			response=HttpResponse(wrapper, content_type='text/plain')
			response['Content-Length']=getsize('new.txt')
			response['Content-Disposition']="attachment; filename="+"mcq_paper.pdf"

			return response
