from django.shortcuts import render, get_object_or_404
from .models import Profile


def profiles_index(request):
    """
    Renders the profiles index page with a list of all profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    """
    Renders a specific profile page based on the username.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)
