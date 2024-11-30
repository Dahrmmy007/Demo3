"""This file showcases the use of in-built and custom Python modules."""

# import math
import dami
import random


a = 81
# print(math.sqrt(81))


nupat_list = [12, 23, 56, 3, 78]
# print(dami.find_min(nupat_list))

unknown_1 = random.random()
unknown_2 = random.randint(1, 5)
# print(unknown_1)
# print(unknown_2)

dami_pay = dami.computepay(8, 86.99)
print(dami_pay)
