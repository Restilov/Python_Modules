# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_water_reminder.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/01 15:45:59 by ybarut             #+#    #+#             #
#   Updated: 2026/03/01 15:52:15 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder():
    day_since_watering = int(input("Days since last watering: "))
    if day_since_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
