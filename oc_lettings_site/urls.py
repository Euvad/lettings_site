# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    urls.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: VadTheZombie <vadim.intra@inbox.ru>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/03 07:25:27 by VadTheZombi       #+#    #+#              #
#    Updated: 2025/03/03 07:25:27 by VadTheZombi      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.contrib import admin
from django.urls import path, include
from . import views  # Import correct des vues locales

urlpatterns = [
    path("", views.index, name="index"),  # Vue principale pour la page d'accueil
    path("lettings/", include("letting.urls")),  # Inclusion des URLs de l'app letting
    path(
        "profiles/", include("user_profile.urls")
    ),  # Inclusion des URLs de user_profile
    path("admin/", admin.site.urls),
]

handler404 = "oc_lettings_site.views.error_404_view"
handler500 = "oc_lettings_site.views.error_500_view"
