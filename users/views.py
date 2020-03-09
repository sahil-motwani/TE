from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,ProfileRegisterForm
from .models import Questions
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        p_reg_form = ProfileRegisterForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p_reg_form = ProfileRegisterForm(request.POST, instance=user.profile)
            p_reg_form.full_clean()
            p_reg_form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, "Your Account has been created ! Answer some questions then you can now login")
            return redirect('question',pk=user.id,ck=username)
    else:
        form=UserRegisterForm()
        p_reg_form = ProfileRegisterForm()
    context = {
    'form': form,
    'p_reg_form': p_reg_form
    }
    return render(request,'users/register.html',context)
@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your Account has been updated !")
            return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)

def question(request,pk,ck):
    if request.method == 'POST':
        if request.POST.get('question1') and request.POST.get('question2') and request.POST.get('question3') and request.POST.get('question4'):
            q1=request.POST.get('question1')
            q2=request.POST.get('question2')
            q3=request.POST.get('question3')
            q4=request.POST.get('question4')
            #username=request.POST.get('user.username')
            #user_id=request.POST.get('user.id')
            #post=Questions(username=request.user.username,question1=q1,question2=q2,question3=q3,question4=q4,user_id=request.user.id)
            post=Questions(username=ck,question1=q1,question2=q2,question3=q3,question4=q4,user_id=pk)
            post.save()
            print("happy")
            return redirect('profile') 
    else:
        return render(request,'users/question.html')