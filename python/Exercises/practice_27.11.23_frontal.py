'''
print(22/7)
print("i've {0:12}".format(22/7)) # מינימום 12 תווים
print("i've {0:12f}".format(22/7)) #
print("i've {0:12.50f}".format(22/7)) # מינימום 12 תווים ושיהיה 50 אחרי הנקודה
print("i've {0:52.50f}".format(22/7)) # מינימום 52 תווים ושיהיה 50 אחרי הנקודה
print("i've {0:62.50f}".format(22/7)) #מינימום 52 תווים ושיהיה 50 אחרי הנקודה
print("i've {0:<72.50f}".format(22/7)) # מינימום 72 תווים ושיהיה 50 אחרי הנקודה ולהצמיד לצד ימין
'''


for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))


'''
age = 24.3
print("My age is %.1f years" % age)
'''

'''
age = 24.3
major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
'''

'''
my_dict = {'key1': 'value1', 'key2': 'value2'}
# print(my_dict['key1'])
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
# print(d['k2'])
# print(d['k3'])
print(d['k3']['insideKey'])
'''

'''
d = {'key1': ['a', 'b', 'c', 'd'], 'key2': 'rara'}
d['key1'][2] = 'e'
print(d)
# print(d.keys())
# print(d. values())
print(d.items())
'''