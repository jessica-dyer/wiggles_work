# eve_nums = []
# n = 15
#
# # initialize sum and counter
# sum = 0
# i = 0
#
# while i <= n:
#     if i % 2 == 0:
#         eve_nums.append(i)
#     i = i + 1
#
# print(eve_nums)
#
# list1 = [8, 3, 4, 5, 6, 7, 9]
# accum = 0
# list_size = len(list1)
# loop_counter = 0
#
# while loop_counter < list_size:
#     # add current list element to the sum
#     accum = accum + list1[loop_counter]
#     # increment loop index
#     loop_counter = loop_counter + 1
# print(accum)

# list1 = [8, 3, 4, 5, 6, 7, 9]
#
#
# def stop_at_four(a_list_of_numbers):
#     if not isinstance(a_list_of_numbers, list):
#         return None
#     if len(a_list_of_numbers) == 0:
#         return []
#
#     loop_counter = 0
#     new_list = []
#
#     while a_list_of_numbers[loop_counter] != 4:
#         new_list.append(a_list_of_numbers[loop_counter])
#         loop_counter = loop_counter + 1
#         if loop_counter >= len(a_list_of_numbers):
#             break
#
#     return new_list
#
#
# stop_at_four([7, 2, 8])
#
# list_size = len(a_list_of_numbers)
# loop_counter = 0
# current_num = 0
# new_list = []
#
# while loop_counter < list_size:
#     current_num = a_list_of_numbers[loop_counter]
#     new_list.append(a_list_of_numbers[loop_counter])
#
# return(new_list)

# Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to
# return a sublist of the input list. The sublist should contain the same values of the original list up until it
# reaches the number 5 (it should not contain the number 5).

# list([7, 2, 8])
#
#
# def sublist(a_list_of_numbers):
#     if not isinstance(a_list_of_numbers, list):
#         return None
#     if len(a_list_of_numbers) == 0:
#         return []
#
#     loop_counter = 0
#     new_list = []
#
#     while a_list_of_numbers[loop_counter] != 5:
#         new_list.append(a_list_of_numbers[loop_counter])
#         loop_counter = loop_counter + 1
#         if loop_counter >= len(a_list_of_numbers):
#             break
#
#     return new_list

# def sublist(a_list_of_strings):
#     if not isinstance(a_list_of_strings, list):
#         return None
#     if len(a_list_of_strings) == 0:
#         return []
#
#     loop_counter = 0
#     new_list = []
#
#     while a_list_of_strings[loop_counter] != "STOP":
#         new_list.append(a_list_of_strings[loop_counter])
#         loop_counter = loop_counter + 1
#         if loop_counter >= len(a_list_of_strings):
#             break
#
#     return new_list
#
#
# sublist(["Blah", "poo", "STOP"])

# sum1 = 0
#
# lst = [65, 78, 21, 33]
#
# for x in lst:
#     sum1 = sum1 + x
# print(sum1)

# lst = [65, 78, 21, 33]
#
# # initialize sum and counter
# list_size = len(lst)
# loop_counter = 0
# added_nums = 0
#
# while loop_counter < list_size:
#     current_num = lst[loop_counter]
#     loop_counter = loop_counter + 1
#     added_nums = added_nums + current_num
#
# print(added_nums)


# def beginning(a_list):
#     if not isinstance(a_list, list):
#         return None
#     if len(a_list) == 0:
#         return []
#
#     loop_counter = 0
#     new_list = []
#
#     while a_list[loop_counter] != "bye":
#         new_list.append(a_list[loop_counter])
#         loop_counter = loop_counter + 1
#         if loop_counter >= len(a_list):
#             break
#
#     new_list = new_list[0:9]
#
#     return new_list

# def str_mult(a_string, integer=3):
#     total = a_string * integer
#     return total


# def mult(an_int, another=6):
#     total = an_int * another
#
#     return total

# Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value
# is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter
# is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then
# be returned. If the boolean parameter is False, return the boolean value “False”.

# def test(integer, b=True, dict1={2: 3, 4: 5, 6: 8}):
#     if b:
#         maybe_val = dict1[integer]
#         if maybe_val != None:
#             return maybe_val
#         # for k, v in dict1.items():
#         #     if k == integer:
#         #         return v
#
#     return False
#
#
# test(2)

# Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be
# a string. The second is an optional parameter called direction with a default value of True. The third is an optional
# parameter called d that has a default value of
# {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}.
#
# Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is
# a key in the third parameter; if it is, return True, otherwise return False.
#
# But if the second parameter is False, then the function should check to see if the first parameter is not a key of
# the third. If it’s not, the function should return True in this case, and if it is, it should return False.

def checkingIfIn(a_string, direction=True,
                 d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    # contains = d.__contains__(a_string)
    contains = a_string in d
    if direction:
        return contains
    else:
        return not contains

    # if direction:
    #     maybe_value = d[a_string]
    #     if maybe_value is not None:
    #         return True
    #     else:
    #         return False
    # if not direction:
    #     maybe_value = d[a_string]
    #     if maybe_value is None:
    #         return True
    #     else:
    #         return False


# ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
#
# def second_let(a_string):
#     second = a_string[1]
#     return second
#
#
# sorted_by_second_let = sorted(ex_lst, key=second_let)

# dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
#
# y = (sorted(dictionary, key=lambda k: dictionary[k]))

# letters = "alwnfiwaksuezlaeiajsdl"
# sorted_letters = sorted(letters, reverse=True)

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]


def last_four(id):
    last_four_numbers = id % 10000
    return last_four_numbers


sorted_id = sorted(ids, key=lambda id_num: id_num % 10000)
