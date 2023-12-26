# # רשימה עם מחרוזות בגדולות וקטנות
# original_list = ["Apcccple", "banana", "Orange", "grape"]
#
# # מיון לפי אותיות קטנות (case-insensitive)
# sorted_list = sorted(original_list, key=str.lower)
#
# print("Original list:", original_list)
# print("Sorted list (case-insensitive):", sorted_list)
#-----------------------------------------------------------------
# def validate_usr(username):
#     return_data = True
#     if 4 <= len(username) <= 16 and " " not in username:
#         for char in username:
#             if (char.isalpha() and char.islower()) or char.isdigit() or char == "_":
#                 return_data = True
#             else:
#                 return_data = False
#                 break
#     else:
#         return_data = False
#     return return_data
# print(validate_usr("ash!4wbYHe5251w"))
#-----------------------------------------------------
# def take(arr,n):
#     return arr[:n]
#     pass
# print(take([-90, 2, 72, -38, -10, -69, -9, 35, 18, -17, 48, -1, 37, 46, -32, 23, 2, 67, -68, 78, 38, 20, 40, 43, 1, -46, 13, 12, -9, -80, 16, -47, 70, 11, -35, -17, 24, -18, 34, -47, 69, 7, -10, -48, -7, -26, -12, 9, 18, 47, 73, -3, 4, 21, -36, -13, 24, 82, -22, 3, 46, -35, -26, 19, -6, -32, 17, 35, -24, 33, -18, -41, 40, -91, -32, -14, -21, 14, 6, -20, -61, 14, 49, -25, 71, -18] , 22))
#---------------------------------------------------------
# def maskify(cc):
#     return f"{# * cc[-4:]} + {cc[:4]}"
#     pass
#
# maskify(333333344343)
# #-----------------------------------------------------
# def descending_order(num):
#     new_num = []
#     for i in str(num):
#         new_num.append(i)
#     new_num.sort(reverse=True)
#     final_num = "".join(new_num)
#     return int(final_num)
#
# print(descending_order(7353946))
#--------------------------------------------------------
# def longest(a1, a2):
#     s = a1 + a2
#     counter = ""
#     for i in s:
#         if i not in counter:
#             counter += i
#     return "".join(sorted(counter))
# print(longest("dfdgdafgd", "fdvsbghm"))
#------------------------------------------------------
#def print_up(n):
#     if n == 0:
#         return
#
#     print_up(n - 1)
#     print(n)
#
# number = int(input("Enter a number: "))
# print_up(number)
#------------------------------------------------
# def print_even_numbers(n):
#     """Recursively prints even numbers entered by the user."""
#
#     if n == 0:
#         return  # Base case: If no more numbers to ask, return
#
#     number = int(input("Enter a number: "))
#     if number % 2 == 0:
#         print(number)  # Print even number
#     print_even_numbers(n - 1)  # Recursive call with one less number to ask
#
# # Example usage
# n = int(input("Enter the number of times to ask for a number: "))
# print_even_numbers(n)
#--------------------------------------------
# def sort_array(source_array):
#     odd_array = []
#     for i in range(len(source_array)):
#         if source_array[i] % 2 == 0:
#             odd_array.append(i)
#     for i in range(len(odd_array)):
#         source_array[i] = sorted(odd_array)[i]
#     return source_array
#     pass
# print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
# print("i'ts need to be => [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]")
# print(sort_array([5, 8, 6, 3, 4]))
# print("i'ts need to be => [3, 8, 6, 5, 4]")
#--------------------------------------------------------'





