import json
from datetime import datetime
print(type(json))
from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from users.models import Profile
from .models import Post,MoodStress,HowsDay

def home(request):
    context={
        'posts':Post.objects.all()
        }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})
@csrf_exempt
def detection(request):
    if request.method == 'POST':
        res = request.POST.get('res')
        print(res)

    print("Detection called ! ")
    mood_dict = eval(res)
    emp_id = list(mood_dict.keys())[0]
    detect=MoodStress(username=emp_id,angry=mood_dict[28]['angry'],disgust=mood_dict[28]['disgust'],fear=mood_dict[28]['fear'],happy=mood_dict[28]['happy'],neutral=mood_dict[28]['neutral'],sad=mood_dict[28]['sad'],surprise=mood_dict[28]['surprise'],user_id=28)
    detect.save()
    return render(request,'blog/about.html')
@csrf_exempt
def howday(request):
    print("lalalal")
    if request.method == 'POST':
        res = request.POST.get('res')
    mood_dict = eval(res)
    mood_dict['user']=int(mood_dict['user'])
    detect=HowsDay(user_id=mood_dict['user'],feeling=mood_dict['mood'])
    detect.save()
    return render(request,'blog/about.html')

def dashboard(request):
    all_employees = Profile.objects.all()
    print(all_employees)
    le = list(all_employees)
    print(le)
    for i in le:
        print(i)
        print(i.user)
    return render(request, 'blog/dashboard.html',{'employees':all_employees})

def chartpage(request,user_id):
    context={}
    moodstress_emp = MoodStress.objects.filter(user_id=user_id )
    print(moodstress_emp)
    lst = list(moodstress_emp)
    lstc = lst.copy()
    for i in lst:
        if(i.created.date().day < datetime.now().day-7):
            print(i)
            lstc.remove(i)
    print(lstc)
    context={
        'chart':lstc
    }
    print(context)
    #print(lstc[0].angry)
    angry=0.0
    disgust=0.0
    fear=0.0
    happy=0.0
    neutral=0.0
    sad=0.0
    surprise=0.0
    dictt={}
    
    for i in context['chart']:
        print(i.angry)
        angry = angry + i.angry
        disgust = disgust + i.disgust
        fear = fear + i.fear
        happy = happy + i.happy
        neutral = neutral + i.neutral
        sad = sad + i.sad
        surprise = surprise + i.surprise
    dictt['angry']=angry
    dictt['disgust']=disgust
    dictt['fear']=fear
    dictt['happy']=happy
    dictt['neutral']=neutral
    dictt['sad']=sad
    dictt['surprise']=surprise
    print(dictt)
    print(dictt['angry'])
    # for i in dictt:
    #     total = total + dictt[i]
    
    mood_dict={
        'emotions':dictt
    }
    print(mood_dict)
    return render(request,'blog/charts.html', mood_dict)
    
    
    
#class chartview(View):
    #pylint: disable=unused-argument
def chartview(self,request, *args, **kwargs):
    moodchart = get_object_or_404(MoodStress, username=self.kwargs.get('userid'))
    print("hey")
    return redirect("about.html")
