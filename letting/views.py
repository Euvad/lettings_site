# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: VadTheZombie <vadim.intra@inbox.ru>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/03 07:27:07 by VadTheZombi       #+#    #+#              #
#    Updated: 2025/03/03 07:27:07 by VadTheZombi      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.shortcuts import render, get_object_or_404
from .models import Letting


def lettings_index(request):
    """
    Renders the lettings index page with a list of all lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


def letting(request, letting_id):
    """
    Renders a specific letting page based on the letting ID.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting.html", context)
