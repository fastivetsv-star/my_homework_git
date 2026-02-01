# 1.1 
def get_length(text):
    return len(text)
print(get_length("Hello World"))

# 1.2 
def combine_strings(text1, text2):
    return text1 + text2
print(combine_strings("Hello ", "World"))

# 2.1 
def get_square(num):
    return num ** 2
print( get_square(5))

# 2.2 
def sum_numbers(a, b):
    return a + b
print(sum_numbers(33, 22))

# 2.3 

def divide_full(a, b):
    integer_part = a // b
    remainder = a % b
    return integer_part, remainder
print(divide_full(25, 5))

# 3.1
def average_value(numbers):
    if len(numbers) == 0: return 0 
    return sum(numbers) / len(numbers)
my_list = [10, 5, 12, 3, 8]
print(average_value(my_list))

# 3.2 
def common_elements(list1, list2):
    return list(set(list1) & set(list2))
lst1 = [5, 7, 9, 0, 1, 4]
lst2 = [1, 2, 5, 6, 8, 1, 0]
print(common_elements(lst1, lst2))



# 4.1 
def print_keys(data_dict):
    for key in data_dict:
        print(key)
person = {'name': 'Kolia', 'age': '22', 'surname': 'shewcenko'}
print(" Ключі:")
print_keys(person)

# 4.2 
def merge_dictionaries(d1, d2):
    return d1 | d2 
print_keys(person)
info1 = {'name': 'Kolia', 'age': '33'}
info2 = {'city': 'Kyiv', 'job': 'Driver'} 
print(merge_dictionaries(info1, info2))

# 5.1 
def union_sets(set1, set2):
    return set1 | set2
# 5.2
def check_subset(subset, main_set):
    return subset.issubset(main_set)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s_small = {1, 2}
print( union_sets(s1, s2))
print( check_subset(s_small, s1))
# 6.1
def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} - Парне")
    else:
        print(f"{number} - Непарне")

# 6.2
def get_even_numbers(numbers_list):
    result = []
    for num in numbers_list:
        if num % 2 == 0:
            result.append(num) 
    return result

check_odd_even(10)
check_odd_even(7)

numbers = [1, 2, 3, 4, 5, 6, 10, 11]
print("Тільки парні:", get_even_numbers(numbers))
# 7
check_parity = lambda x: "парне" if x % 2 == 0 else "не парне"

print(check_parity(4)) 
print(check_parity(9))  