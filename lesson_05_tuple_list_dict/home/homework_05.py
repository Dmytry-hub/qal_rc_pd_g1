# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_list_elements = set (small_list)
print("Унікальні елементи списка:", unique_list_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
arithmetic_mean_elements = round(sum (small_list) / len(small_list))
print("Середне арифметичне елементів списка дорівнює:", arithmetic_mean_elements)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
if big_list == set(big_list):
    print('Ні, в списку немає дублікатів')
else:
    print('Так, в списку є дублікати')

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_number = max(add_dict, key=lambda m: add_dict[m])
print("ключ з максимальним значенням у словнику add_dict:", max_number)

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
new_base_dict = {}
for key, vol in base_dict.items():
    new_base_dict[vol] = key
print (new_base_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
#sum_dict = {}
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
sum_dict = base_dict.copy()
for key, vol in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(vol)
    else: sum_dict[key] = vol
print(sum_dict)

# task 7.
line = "Створіть список з всіх символів, які входять у заданий рядок"
new_line = list(line)
print(new_line)

# task 8. Обчисліть суму елементів двох змінних через sum()
value_1  = [1, 2, 3, 4, 5]
value_2 = (4, 6, 5, 10)
summa_list = sum (value_1)
summa_tuple =sum (value_2)
summa_elements_list_tuple = sum (value_1) + sum (value_2)
print("Сума елементів двох змінних дорівнює:", summa_elements_list_tuple)


