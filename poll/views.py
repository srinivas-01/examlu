from django.shortcuts import render
from .models import Question
# Create your views here.
def index(response):
	context={}
	q=Question.objects.all()
	context['questions']=q
	return render(response, "poll/index.html",context)