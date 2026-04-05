# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_different_errors.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: ybarut <ybarut@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/05 19:34:05 by ybarut             #+#    #+#             #
#   Updated: 2026/04/05 20:20:25 by ybarut            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "garden" + 42
 
 
def test_error_types() -> None:
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
 
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
 
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
 
    print("Testing operation 3...")
    try:
        garden_operations(3)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
 
    print("Testing operation 4...")
    try:
        garden_operations(4)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    else:
        print("Operation completed successfully")
 
    print("\nAll error types tested successfully!")
 
 
if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()