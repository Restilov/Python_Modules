# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_custom_errors.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/09 16:25:49 by ybarut             #+#    #+#             #
#   Updated: 2026/04/09 16:47:45 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def raise_plant_error(message: str) -> None:
    raise PlantError(message)


def raise_water_error(message: str) -> None:
    raise WaterError(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise_plant_error("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise_water_error("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise_plant_error("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise_water_error("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()