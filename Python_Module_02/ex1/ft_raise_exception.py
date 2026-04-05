# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_raise_exception.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/05 18:44:50 by ybarut             #+#    #+#             #
#   Updated: 2026/04/05 19:05:23 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def input_temperature(input: str) -> int:
    try:
        input = int(input)
    except ValueError:
        raise
    if 0 > input:
        raise ValueError(f"{input}°C is too cold for plants (min 0°C)")
    elif 40 < input:
        raise ValueError(f"{input}°C is too hot for plants (max 40°C)")
    return(input)

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
    print("\nInput data is '100'")
    try:
        temp = input_temperature('100')
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nInput data is '-50'")
    try:
        temp = input_temperature('-50')
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
	print("=== Garden Temperature Checker ===")
	test_temperature()