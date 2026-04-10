#!/ust/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_first_exception.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/10 15:37:41 by ybarut             #+#    #+#             #
#   Updated: 2026/04/10 17:31:46 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def input_temperature(input: str) -> int:
    try:
        input = int(input)
    except ValueError:
        raise
    return input


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        temp = input_temperature('25')
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is 'abc'")
    try:
        temp = input_temperature('abc')
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
