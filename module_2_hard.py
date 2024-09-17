n = int (input ("Введите число от 3 до 20"))
resulte = ""
for i in range (1, n):
    for j in range (1 + i, n):
        if n %  (i + j) ==0:
            resulte += (str(i) + str (j))
print(resulte)
















