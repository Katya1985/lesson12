# n = int (input ("Введите число от 3 до 20"))
# resulte = " "
# for i in range(3, n + 1):
#     for j in range(3, n + 1):
#         if (i %  (i + j) ==0):
#             resulte += f ("{i}, {j}")
# print(resulte)












n = int (input ("Введите число от 3 до 20"))
resulte = ""
for i in range (1, n):
    for j in range (1 + i, n):
        if n %  (i + j) ==0:
            resulte += (str(i) + str (j))
print(resulte)













n = int (input ("Введите число от 3 до 20"))
resulte = " "
import random
a = [random.randint (3, 21)]
def pair (a):
    random = list()
    b = (a + 1) // 2
    for i in range(1, b):
        j = i + 1
        while i + j <= a:
            if a % (i + j) == 0:
                numbers = (i, j)
                random.append(numbers)
            j += 1
    return random



