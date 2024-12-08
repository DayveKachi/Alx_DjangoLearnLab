from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, UserForm


class HomeView(generic.TemplateView):
    template_name = "blog/home.html"


class UserCreateView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        user_form = UserForm(data=request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse("home"))
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "blog/edit_profile.html", context)
