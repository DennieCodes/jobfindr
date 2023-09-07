from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import SignupForm, LoginForm
from django.contrib.auth.models import User

# USER_LOGIN
def user_login(request):
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data["email"]
      password = form.cleaned_data["password"]

      user = authenticate(
        request,
        username=email,
        password=password,
      )

      if user is not None:
        login(request, user)
        return redirect("list_applications")
  else:
    form = LoginForm()

  context = {
    "form": form
  }

  return render(request, "accounts/login.html", context)

# USER_SIGNUP
def user_signup(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data["email"]
      password = form.cleaned_data["password"]
      password_confirmation = form.cleaned_data["password_confirmation"]

      if password == password_confirmation:
        user = User.objects.create_user(
          username=email,
          email=email,
          password=password
        )

        login(request, user)
        return redirect("list_applications")
  else:
    form = SignupForm()

  context = {
    "form": form
  }

  return render(request, "accounts/signup.html", context)

# LOGOUT
def user_logout(request):
  logout(request)
  return redirect("user_login")