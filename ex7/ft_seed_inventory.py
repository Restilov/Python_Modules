# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_seed_inventory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/01 15:46:16 by ybarut             #+#    #+#             #
#   Updated: 2026/03/01 15:51:56 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    messages = {
        "packets": "{} seeds: {} packets available",
        "grams": "{} seeds: {} grams total",
        "area": "{} seeds: covers {} square meters"
    }
    if unit in messages:
        print(messages[unit].format(seed_type.capitalize(), quantity))
    else:
        print("Unknown unit type")
