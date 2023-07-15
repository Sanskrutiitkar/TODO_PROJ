from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import TodoForm
from .models import TodoModel

def home(request):
	if request.user.is_authenticated:
		return redirect("todo")
	elif request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		ur = authenticate(username=un, password=pw)
		if ur is not None:
			login(request,ur)
			return redirect("todo")
		else:
			return render(request, "home.html", {"msg":"Invalid credential"})
	else:
		return render(request, "home.html")

def usignup(request):
	if request.method == "POST":
		un=request.POST.get("un")	
		pw1=request.POST.get("pw1")
		pw2=request.POST.get("pw2")
		if pw1==pw2:
			try:
				ur= User.objects.get(username=un)
				return render(request, "signup.html", {"msg":"username already exist"})
			except User.DoesNotExist:
				ur = User.objects.create_user(username=un , password=pw1)
				ur.save()
				return redirect("home")
		else:
			return render(request, "signup.html", {"msg":"passwords did not match"})
	else:
		return render(request, "signup.html")


def uchangepass(request):	
	if request.user.is_authenticated:
		if request.method=="POST":
			un = request.POST.get("un")
			pw1= request.POST.get("pw1")
			pw2= request.POST.get("pw2")
			if pw1==pw2:
			
				if (un==request.user.username):
					ur = User.objects.get(username=un)
					ur.set_password(pw1)
					ur.save()
					return redirect("home")
				else:
					return render(request, "changepass.html",{"msg":"user does not exist"})
			else:
				return render(request, "changepass.html",{"msg":"passwords did not match"})
		else:
			return render(request, "changepass.html")
	else:
		return redirect("home")

def ulogout(request):
	logout(request)
	return redirect("home")	


def about(request):
	return render(request, "about.html")

def todo(request):
	if request.user.is_authenticated:
		data = TodoModel.objects.filter(owner = request.user)
		return render(request,"todo.html" , {"data":data})
	else:
		return redirect("home")	
	
def todocreate(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			fdk = request.POST.get("task")
			fdk1 = request.POST.get("description")
			data = TodoModel(task = fdk, description = fdk1, owner=request.user)
			
			data.save()
			msg = "Task added to the list!!"
			fm = TodoForm()
			return render(request, "create.html", {"fm":fm , "msg":msg})
			
		else:
			fm = TodoForm()
			return render(request , "create.html" , {"fm":fm})
	else:
		return redirect("home")

def todocomp(request,tid):
	if request.user.is_authenticated:
		de = TodoModel.objects.get(id=tid)
		de.done = True
		de.save()
		return redirect("todo")
	else:
		return redirect("home")
		
def todoview(request,tid):
	if request.user.is_authenticated:
		data1= TodoModel.objects.get(id=tid)
		return render(request, "view.html",{"data":data1})
	else:
		return redirect("home")
	
def tododelete(request,tid):
	if request.user.is_authenticated:
		de = TodoModel.objects.get(id=tid)
		de.delete()
		return redirect("todo")	
	else:
		return redirect("home")
	


