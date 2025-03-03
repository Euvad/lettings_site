# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: VadTheZombie <vadim.intra@inbox.ru>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/03 07:27:48 by VadTheZombi       #+#    #+#              #
#    Updated: 2025/03/03 07:27:48 by VadTheZombi      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.shortcuts import render


def index(request):
    """
    Renders the homepage.
    """
    return render(request, "index.html")


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
