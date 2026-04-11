# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_command_quest.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/11 21:18:51 by ybarut             #+#    #+#             #
#   Updated: 2026/04/11 23:02:43 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys

def main() -> None:
    args = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")

    if len(args) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        for i, arg in enumerate(args[1:], start=1):
            print(f"Argument {i}: {arg}")

    print(f"Total arguments: {len(args)}")


main()