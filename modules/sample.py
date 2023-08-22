# """
#
#
# """
#
#
#
# import may11
# # from may11 import sum
# #
# # print(sum(4,6))
#
# import math
#
# print(math.sqrt(5))
# print(math.factorial(5))
# print(math.pi)
# r = 5
# print(math.pi*r*r)
#
#
# #os module
#
# import os
#
# # os.mkdir(r"C:\Users\Luminar\PycharmProjects\May_Python\sample\test")
# # os.rmdir("")
# # os.rmdir(r"C:\Users\Luminar\PycharmProjects\May_Python\test")
# # print(os.getcwd())
# # os.chdir('D:/')
# # print(os.getcwd())
#
# #random module
#
# import random
#
# # print(random.randrange(10))
# # print(random.randint(1,100))
# a = [1,4,5,6,7,8]
# (random.shuffle(a))
# print(a)
# str = 'computer'
# print(random.choice(str))
# print()
import datetime
import time
from datetime import date

# today = date.today()
# print("Todays dateis :",today)

# now = datetime.datetime.now()
# print(now)

import datetime

today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)

# time = datetime.time.second
# print(str(time))

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%X")
print(current_time)
# print(current_time)
# current_time = now.ctime()
# print(current_time)
# current_time = time.ctime()
# print(current_time)