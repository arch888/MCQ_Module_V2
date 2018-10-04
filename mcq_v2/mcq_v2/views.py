from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import signup_form,login_form
from quiz.models import quizze
from random import shuffle
from leaderboard.models import leaderboard as lb
from django.utils.timezone import datetime
from userprofile.models import profile

from userprofile.models import profile


from django.contrib.auth import authenticate,login,get_user_model,logout

User=get_user_model()


def index(request):
	if request.POST:
		print(request.POST)
	return render(request,'index/index.html',{})


def login_view(request):
	form_class=login_form(request.POST or None)
	content={
		"form": form_class
	}
	if not request.user.is_authenticated:
		if form_class.is_valid():
			username=form_class.cleaned_data.get("email")
			password=form_class.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect("/instruction")
			else:
			    print("Error")
		return render(request,'login/login.html',content)
	else:
		obj=lb.objects.filter(user=request.user)
		if obj.exists():
			return redirect('/result')
		else:
			return redirect('/instruction')



def logout_view(request):
	if request.user is not None:
		logout(request)
	return redirect('/')


def signup(request):
	form_class=signup_form(request.POST or None)
	context={
		"form":form_class
	}
	if form_class.is_valid():
		name=form_class.cleaned_data.get("name")
		email=form_class.cleaned_data.get("email")
		college=form_class.cleaned_data.get("college")
		year=form_class.cleaned_data.get("year")
		branch=form_class.cleaned_data.get("branch")
		password=form_class.cleaned_data.get("password")
		new_user= User.objects.create_user(email,email,password)
		user_profile=profile(
				user=new_user,
				name=name,
				college=college,
				year=year,
				branch=branch
			)
		user_profile.save()
		if new_user is not None:
			return redirect("/login")
	return render(request,'signup/signup.html',context)



def instruction(request):
	if request.user.profile_set.all().first().start_time==0:
		return render(request,'index/instruction.html',{})
	else:
		return render(request,'test/rule_broken.html',{});



def leaderboard(request):
	object_1=lb.objects.all().order_by('-points')
	context={
		"object":object_1
	}
	return render(request,'test/leaderboard.html',context)










def dashboard(request):
	quiz_object=quizze.objects.filter(title='Recruitment Drive').first()
	queryset=list(quiz_object.ques.all())
	shuffle(queryset)
	time=quiz_object.time
	context={
		"question1":queryset[0],
		"question2":queryset[1],
		"question3":queryset[2],
		"question4":queryset[3],
		"question5":queryset[4],
		"question6":queryset[5],
		"question7":queryset[6],
		"question8":queryset[7],
		"question9":queryset[8],
		"question10":queryset[9],
		"question11":queryset[10],
		"question12":queryset[11],
		"question13":queryset[12],
		"question14":queryset[13],
		"question15":queryset[14],
		"question16":queryset[15],
		"question17":queryset[16],
		"question18":queryset[17],
		"question19":queryset[18],
		"question20":queryset[19],
		"question21":queryset[20],
		"question22":queryset[21],
		"question23":queryset[22],
		"question24":queryset[23],
		"question25":queryset[24],
		"question26":queryset[25],
		"question27":queryset[26],
		"question28":queryset[27],
		"question29":queryset[28],
		"question30":queryset[29],
		"time":time
	}

	if request.POST:
		count=0
		attempted_qus=0
		for jk in range(30):		
			if request.POST.get(str(queryset[jk].qus_id))==str(queryset[jk].correct_option):
				count=count+1		
			if request.POST.get(str(queryset[jk].qus_id))==None:
				attempted_qus=attempted_qus+1
		attempted_qus=30 - attempted_qus
		correct_qus=count
		wrong_qus=attempted_qus-count
		points=(count*4)-(wrong_qus)
		object_1=lb.objects.filter(user=request.user)
		if points<=20:
			message="Congrats You have Done well !!"
		elif points>20 and points<=30:
			message="Congrats You have Done Pretty well !!"
		elif points>30 and points<=40:
			message="Congrats You have Done your Best !!"
		else:
			message="Congrats You Rocked !!"
		if not object_1.exists():
			lb1=lb(
					user=request.user,
					correct_qus=correct_qus,
					wrong_qus=wrong_qus,
					points=points,
					message=message,
					attempted_qus=attempted_qus
				)
			lb1.save()
			return redirect('/result')
		else:
			return redirect('/')
	if request.user.is_authenticated:
		if request.user.profile_set.all().first().start_time==0:
			obj=profile.objects.get(user=request.user)
			obj.start_time=1
			obj.save()
		else:
			if request.user.is_authenticated:
				logout(request)
			return render(request,'test/rule_broken.html',{});
	return render(request,'test/dashboard.html',context)



def result(request):
	if request.user.is_authenticated:
		obj=lb.objects.filter(user=request.user)
		if obj.exists():
			context_2={
				"cqus":obj.first().correct_qus,
				"wqus":obj.first().wrong_qus,
				"points":obj.first().points,
				"message":obj.first().message
			}
		
		logout(request)
	else:
		context_2={}
	return render(request,'test/result.html',context_2)
