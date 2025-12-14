#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists element-wise.
    Args:
        my_list_1 (list): First list.
        my_list_2 (list): Second list.
        list_length (int): Length of result list.
    Returns:
        list: New list of divisions (length = list_length).
    """
    new_list = []
    for i in range(list_length):
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            result = val1 / val2
            new_list.append(result)
        except IndexError:
            print("out of range")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        finally:
            pass
    return new_list
