# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    admin.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: VadTheZombie <vadim.intra@inbox.ru>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/06 16:27:56 by VadTheZombi       #+#    #+#              #
#    Updated: 2025/02/06 16:27:56 by VadTheZombi      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.contrib import admin

from letting.models import Letting
from letting.models import Address
from user_profile.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
