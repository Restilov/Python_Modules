# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_count_harvest_recursive.py                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/01 15:46:06 by ybarut             #+#    #+#             #
#   Updated: 2026/03/01 15:47:58 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(i, total):
        if i > total:
            return
        print(f"Day {i}")
        helper(i + 1, total)
    helper(1, days)
    print("Harvest time!")
