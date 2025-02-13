# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: VadTheZombie <vadim.intra@inbox.ru>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/06 16:27:52 by VadTheZombi       #+#    #+#              #
#    Updated: 2025/02/06 16:27:52 by VadTheZombi      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.shortcuts import render
from letting.models import Letting
from user_profile.models import Profile
import sentry_sdk


def index(request):
    return render(request, "index.html")


def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting.html", context)


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
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)


def error_404_view(request, exception):
    """
    Renders the custom 404 error page.
    """
    return render(request, "404.html", status=404)


def error_500_view(request):
    """
    Renders the custom 500 error page.
    """
    return render(request, "500.html", status=500)
