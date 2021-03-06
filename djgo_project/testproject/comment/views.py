from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    respond = """
       Hello, world. Comment!  <br/>
       try:                    <br/>
       -ex: /comment/          <br/>
       -ex: /comment/5/        <br/>
       -ex: /comment/5/results/<br/>
       -ex: /comment/5/vote/   <br/>
    """
    return HttpResponse(respond)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
