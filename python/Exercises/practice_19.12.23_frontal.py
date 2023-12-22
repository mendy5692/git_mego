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
def maskify(cc):
    return f"{cc[-4:]*#{cc[:4]}"
    pass

maskify(333333344343)