from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

from django.core.mail import send_mail

from .models import Reg,Questions,Enrollment,Subject,Marks
# Create your views here.



def index(request):
    return render(request,'exams/index.html')

def aboutus(request):
    return render(request,'exams/aboutus.html')
def base(request):
    return render(request,'exams/base.html')

def login(request):
    return render(request,'exams/login.html')


def register(request):
    return render(request,'exams/register.html')

def user(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd=request.POST['pwd']
        r=Reg.objects.all()
        for i in r:
            if email==i.email and pwd == i.pwd:
                return render(request,"exams/user.html",{"message":email})

    return render(request,"exams/login.html",{"message":"Invalid Credentials!!!"})


def recess(request):
    if request.method=='POST':
        r = Reg()
        q = Reg.objects.all()
        a = request.POST['email']
        b = request.POST['pwd']
        for i in q:
            if a == i.email :

                return render(request, 'exams/register.html', {"message": "You already have an account!!!"})
                break


        r.email = a
        r.pwd = b
        r.save()
        return render(request, "exams/user.html")

def viewusers(request):

    users=Reg.objects.all()
    return render(request,'exams/viewusers.html',{"reguser":users})


def addsub(request):
    return render(request,'exams/addsub.html')

def adddomain(request):
    return render(request,'exams/adddomain.html')

def addquetions(request):
    return render(request,'exams/addquestions.html')

def addcontest(request):
    if request.method=='POST':
        pass


def uploadque(request):
    if request.method=='POST':
        r=Questions()
        r.subname=request.POST['subname']
        r.marks=request.POST['marks']
        r.question=request.POST['text']
        r.option1=request.POST['op1']
        r.option2 = request.POST['op2']
        r.option3= request.POST['op3']
        r.option4= request.POST['op4']
        r.answer=request.POST['op5']
        r.save()
        return HttpResponse("successfull...")
    return render(request,"start.html")


def enroll(request):
    if request.method=='POST':
        e=Enrollment()
        e.subjectname=request.POST['sub']
        e.email=request.POST['email']
        e.date=str(date.today())
        e.save()
        return render(request,'exams/afterenroll.html',{'sname1':request.POST['sub'],'email':request.POST['email']})
def questionsshow(request):
    if request.method=='POST':
        sub=request.POST['sub_name']
        ee=request.POST['emailid']
        mm=request.POST['marks']
        q=Questions.objects.all()
        items = sorted(Questions.objects.all(), key=lambda x: random.random())
        return render(request,'exams/afterenroll.html',{'data':items,'subject':sub,'marks':mm,'email':ee})
def marksevaluation(request):
    if request.method=='POST':
        subject=request.POST['subject']
        marks=request.POST['marks']
        email=request.POST['emailid']
        q=Questions.objects.all()
        g=0
        m=Marks.objects.all()
        for i in q:
            if(i.marks==marks and i.subname==subject):
                try:
                    m=request.POST[i.question]
                    if(m==i.answer):
                        if(i.marks=='one'):
                            g=g+1
                        elif(i.marks=='two'):
                            g=g+2
                        elif(i.marks=='three'):
                            g=g+3
                except:
                    g=g+0
        m=Marks()
        m.emailid=email
        m.subname=subject
        m.marksvalue=marks
        m.marks=g
        m.save()
        return HttpResponse('successful')

def afteraddq(request):
    pass