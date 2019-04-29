from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm

User = get_user_model()


class SignUp(CreateView):
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/account/info')
        return render(request, 'signup.html', {'form': form})


class UserInfo(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userinfo.html')
