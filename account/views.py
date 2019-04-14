from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import UpdateView

from blog.forms import UserForm, UserProfileForm
from blog.models import UserProfile

# Create your views here.


@login_required
def profile(request):
    current_profile = UserProfile.objects.get(user=request.user)
    print(
        "Try:" + str(current_profile.profile_pic).split("/account/profile")[0])
    return render(request, "account/profile.html", {'user': request.user, 'profile_src': str(current_profile.profile_pic).split("/account/profile")[0]})


@login_required
def edit_profile(request):
    edited_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        user = UserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            data=request.POST, instance=edited_profile)
        if user.is_valid() and profile_form.is_valid():
            saved_user = user.save()
            profile = profile_form.save(commit=False)
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            return HttpResponseRedirect(reverse("account:profile"))
        else:
            print(user.errors, profile_form.errors)
    else:
        user_form = UserChangeForm(instance=request.user)
        profile_form = UserProfileForm(instance=edited_profile)
        return render(request, "registration/register.html", {'user_form': user_form, 'profile_form': profile_form})
