from django.shortcuts import *
from .models import *
from django.http import *
from .forms import *
from django.template import loader
from django.core.mail import send_mail
def home(request):
    obj = student1.objects.all().order_by('-date')
    # obj = student1.objects.all().order_by('date')
    # obj = student1.objects.all()
    return render(request, 'index.html', {'obj':obj})
def form(request):
    if request.method == 'POST':
        f = student_form(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/form/')
    else:
        f = student_form()
    return render(request, 'form.html', {'f':f})
def hello(request):
    return render(request, 'hello.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_q_list=Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_q_list])
    return render(request, 'index.html', {'out':output})
    #return HttpResponse(output)

def index1(request):
    try:
        latest_question_list = Question.objects.all();
    except Question.DoesNotExist:
        raise Http404("Question does not exixt.")
    # question = get_object_or_404(Question, pk=1) # shortcut method for exception
    template = loader.get_template('index.html')
    context = {
        'latest_question_list' : latest_question_list,
    }
    # return render(request,'index.html',{'latest_question_list' : latest_question_list})
    return HttpResponse(template.render(context,request))
def question(request, question_id):
    question=Question.objects.get(id=question_id)
    choice=question.choice_set.all()[0]
    return render(request,'question.html',{'question':question,'choice':choice})

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)
# Create your views here.
