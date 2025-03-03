# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    admin.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: VadTheZombie <vadim.intra@inbox.ru>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/13 19:50:46 by VadTheZombi       #+#    #+#              #
#    Updated: 2025/02/13 19:50:46 by VadTheZombi      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.contrib import admin
from .models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "street",
        "city",
        "state",
        "zip_code",
        "country_iso_code",
    )


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    list_display = ("title", "address")
