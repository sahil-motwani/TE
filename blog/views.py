import json
print(type(json))
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from users.models import Profile
from .models import Post,MoodStress
#from django.http import HttpResponse
# Create your views here.

def home(request):
    context={
        'posts':Post.objects.all()
        }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def detection(request):
    print("Detection called ! ")
    mood_obj = {"emp" : [{"angry":0.1, "disgust":0.0, "fear":0.02, "happy":0.0, "neutral":0.3, "sad":0.58, "surprise":0.0 }]}
    print(type(mood_obj))
    #idar jo b json m obj aaega ! 
    mood = json.dumps(mood_obj) #object to string

    # mood = '{"emp":[{"angry":0.1, "disgust":0.0, "fear":0.02, "happy":0.0, "neutral":0.3, "sad":0.58, "surprise":0.0 }]}'
    print(type(mood))
    emp_id = ''
    mood_dict = json.loads(mood) #string to dict
    print(mood_dict)
    for i in mood_dict.keys():
        emp_id = i
    detect=MoodStress(username=emp_id,angry=mood_dict['emp'][0]['angry'],disgust=mood_dict['emp'][0]['disgust'],fear=mood_dict['emp'][0]['fear'],happy=mood_dict['emp'][0]['happy'],neutral=mood_dict['emp'][0]['neutral'],sad=mood_dict['emp'][0]['sad'],surprise=mood_dict['emp'][0]['surprise'])
    detect.save()
    return render(request,'blog/about.html')

def dashboard(request):
    all_employees = Profile.objects.all()
    # print("get called")
    # employees = Profile.objects.all()
    # print(list(employees))
    print(all_employees)
    le = list(all_employees)
    print(le)
    for i in le:
        print(i)
        print(i.user)
    return render(request, 'blog/dashboard.html',{'employees':all_employees})