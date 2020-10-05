
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  #for signin and login form
from django.contrib.auth import login, logout                          #log the user in after login form is filled

# Create your views here.
def signup_view(request):
    if request.method == "POST":    
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)                    #log the user in
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)                                    #log the user in    
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))           #when user is logging-in from create page to create article 
            else:
                return redirect('articles:list')                    #when user is logging-in normally
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form':form})
         

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')