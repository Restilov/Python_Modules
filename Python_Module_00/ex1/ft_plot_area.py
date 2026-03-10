# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plot_area.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/01 15:45:40 by ybarut             #+#    #+#             #
#   Updated: 2026/03/01 15:52:18 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    plot_area = length * width
    print(f"Plot area: {plot_area}")
