# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    urls.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: VadTheZombie <vadim.intra@inbox.ru>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/03 07:25:22 by VadTheZombi       #+#    #+#              #
#    Updated: 2025/03/03 07:25:22 by VadTheZombi      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles_index, name="profiles_index"),
    path("<str:username>/", views.profile, name="profile"),
]
