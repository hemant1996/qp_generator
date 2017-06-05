from django.contrib.auth.forms import AuthenticationForm 
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class subjectiveform(forms.Form):
	OPTIONS=((0,'Easy'),(1,'Medium'),(2,'Hard'))
	OPTION2=((100,'100'),(50,'50'))
	OPTION3=((0,'C'),(1,'Operating Systems'),(2,'Micro Processor'))
	difficulty=forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'name': 'difficulty'}),choices=OPTIONS,)
	marks=forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control','name': 'marks'}), choices=OPTION2,)
	subject=forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control','name': 'subject'}), choices=OPTION3,)
class objectiveform(forms.Form):
	OPTIONS=((0,'Easy'),(1,'Medium'),(2,'Hard'))
	OPTION2=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11'),(12,'12'),(13,'13'),(14,'14'),(15,'15'))
	OPTION3=((0,'C'),(1,'Operating Systems'),(2,'Micro Processor'))
	difficulty=forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'name': 'difficulty'}),choices=OPTIONS,)
	marks=forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control','name': 'marks'}), choices=OPTION2,)
	subject=forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control','name': 'subject'}), choices=OPTION3,)