from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse # type: ignore
from . models import Question, Choice
from django.http import Http404 # type: ignore
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return render(request,'polls/index.html',{'latest_question_list':latest_question_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Quesion not found")
    return render(request, 'polls/detail.html', {'question': question})

from django.shortcuts import get_object_or_404

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)