from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Question
# Create your views here.
def index(request):
    latest_question = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question' : latest_question
    }
    # output = ', '.join([q.question_text for q in latest_question]) 
    # return HttpResponse(output)
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    question = get_object_or_404(Question,id=question_id)
    context = {
        'question' : question
    }
    return render(request,'polls/detail.html',context)

def results(request,question_id):
    return HttpResponse(f"you are looking at result of question id : {question_id}")


def vote(request,question_id):
    return HttpResponse(f"you are voting on question id : {question_id}")