from django.shortcuts import *
from .models import *
from django.http import *
from .forms import *
from django.template import loader
from django.core.mail import send_mail
from app.forms import LoginForm
from django.views.generic import TemplateView
def login(request):
    if request.method=='POST':
        login_form = LoginForm(request.POST)
        # form.is_valid()
        # rollno = form.cleaned_data['rollno']
        if Student.objects.filter(rollno=request.POST['rollno']).exists():
            # rollno = login_form.cleaned_data['rollno']
            return  HttpResponseRedirect('/queslist/',{'ques_list':Question.objects.all()})
        if login_form.is_valid():
            rollno = login_form.cleaned_data['rollno']
            request.session['rollno'] = rollno
            login_form.save(commit=True)
            return  HttpResponseRedirect('/queslist/',{'ques_list':Question.objects.all()})
    else:
        form = LoginForm()
    return render(request,'index.html',{'form':form})
   #
   # return render(request, 'loggedin.html', {"username" : "username"})
def queslist(request):
    if request.session.has_key('rollno'):
        rollno = request.session['rollno']
        return render(request, 'queslist.html', {"rollno" : rollno,'ques_list':Question.objects.all()})
    else:
      return HttpResponseRedirect('/login/')
def home(request):
    # obj = Student.objects.all().order_by('-date')
    # obj = student1.objects.all().order_by('date')
    # obj = student1.objects.all()
    return render(request, 'index.html')
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
    question=get_object_or_404(Question, pk=question_id)
    vote=request.POST['vote']
    st_id=request.session['rollno']
    if len(Vote.objects.filter(question_id=question_id,student_id=st_id)) > 0 :
        return HttpResponse("Already Answered.")
    v=Vote()
    v.student_id=st_id
    v.question_id=question_id
    v.vote=vote
    v.save()
    return HttpResponse("You're voting on question %s." % vote)

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
    ques_list=Question.objects.all()
    vote="Not Answered"
    st_id=Student.objects.filter(rollno=request.session['rollno'])[0].rollno
    v_obj=Vote.objects.filter(student_id=st_id,question_id=question_id)
    if v_obj.exists():
        vote=v_obj[0].vote
    return render(request,'question.html',{'question':question,'choice':choice,'ques_list':ques_list,'my_vote':vote})

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)
# Create your views here.
