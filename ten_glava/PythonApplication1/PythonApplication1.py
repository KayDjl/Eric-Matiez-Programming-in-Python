# while True:
#     try:
#         sum_one_number = input("Введите первое число: ")
#         sum1 = int(sum_one_number)
#         sum_two_number = input("Введите второе число: ")
#         sum2 = int(sum_two_number)
#     except ValueError:
#         print("Введенно некоректное значение")
#     else:
#         full_sum = sum1 + sum2
#         print(f'Результат слложения равен {full_sum}')

# def lists(full_name):
#     try:
#         with open(full_name, encoding = 'utf-8') as f:
#             cats = f.read()
#     except FileNotFoundError:
#         pass
#     else:
#         print(cats)
        
# ars = ['../text_file/cats.txt', 'dogs.txt']
# for full_name in ars:
#     lists(full_name)

lod = '../text_file/poli.txt'
with open(lod, encoding = 'utf-8') as f:
    ct = f.read()
fl = ct.lower().count('the')
print(fl)

