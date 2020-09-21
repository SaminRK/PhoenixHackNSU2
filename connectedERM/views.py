from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from organisations.models import Organisation, UserOrganisation

def userlogin(request):
    if request.method != "POST":
        return render(request,'login.html')
    else:
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        user = authenticate(username=user_name, password=pass_word,)
        if user is not None:
            login(request,user)
            return redirect('/user/' + str(user.id))
        return redirect('/login')

def signup(request):
    if request.method != "POST":
        return render(request,'signup.html')
    else:
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        user = User()
        user.username = user_name
        user.set_password(pass_word)
        user.email = email
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect('/login')

def dashboard(request, user_id):
    if (request.user.id == user_id):
        user = request.user
        organisations = UserOrganisation.objects.filter(user=user.id).values('organisation', 'organisation__name')
        otherOrganisations = Organisation.objects.all()
        
        return render(request,
            'dashboard.html', {
                'user' : user,
                'my_organisations' : organisations,
                'other_organisations' : otherOrganisations,
            })
    else:
        return redirect('/login')