from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import signup_form,login_form
from quiz.models import quizze
from random import shuffle

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
	print(request.user.is_authenticated)
	if not request.user.is_authenticated:
		if form_class.is_valid():
			username=form_class.cleaned_data.get("email")
			password=form_class.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			print(user)
			if user is not None:
				login(request,user)
				return redirect("/instruction")
			else:
			    print("Error")
		return render(request,'login/login.html',content)
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
	return render(request,'index/instruction.html',{})



def leaderboard(request):
	return render(request,'test/leaderboard.html',{})










def dashboard(request):
	quiz_object=quizze.objects.filter(title='Recruitment Drive').first()
	queryset=list(quiz_object.ques.all())
	shuffle(queryset)
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
		"question11":queryset[0],
		"question12":queryset[1],
		"question13":queryset[2],
		"question14":queryset[3],
		"question15":queryset[4],
		"question16":queryset[5],
		"question17":queryset[6],
		"question18":queryset[7],
		"question19":queryset[8],
		"question20":queryset[9],
		"time":quiz_object.time

	}
	return render(request,'test/dashboard.html',context)