# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_harvest_total.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/01 15:45:45 by ybarut             #+#    #+#             #
#   Updated: 2026/03/01 15:52:22 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    first_harvest = int(input("Day 1 harvest: "))
    second_harvest = int(input("Day 2 harvest: "))
    third_harvest = int(input("Day 3 harvest: "))
    print(f"Total harvest: {first_harvest + second_harvest + third_harvest}")
