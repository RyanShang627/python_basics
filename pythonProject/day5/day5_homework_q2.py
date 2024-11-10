import random

list1 = []
even_num_count = 0
odd_num_count = 0

for i in range(7):
    num = random.randint(1, 10)
    list1.append(num)
    if num % 2 == 0:
        even_num_count += 1
    else:
        odd_num_count += 1

print(f"列表为: {list1}, 偶数个数为: {even_num_count}, 奇数个数为: {odd_num_count}")