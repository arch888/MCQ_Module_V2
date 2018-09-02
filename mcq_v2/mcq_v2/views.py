from django.shortcuts import render,redirect
from django.http import HttpResponse


def index(request):
	return render(request,'index/index.html',{})


def login(request):
	return render(request,'login/login.html',{})


def signup(request):
	return render(request,'signup/signup.html',{})



def instruction(request):
	return render(request,'index/instruction.html',{})



def dashboard(request):
	return render(request,'test/dashboard.html',{})


def leaderboard(request):
	return render(request,'test/leaderboard.html',{})