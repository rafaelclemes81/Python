grade = [5, 10, 15, 15, 10, 5]
os = list()
divisor = 6


for i in range(0, 6):
    while grade[i] > 0:
        if grade[i] <= divisor:
            if grade[i] == 1:
                os.append(1)
            else:
                grade[i] -= 1
                os.append(1)
        else:
            if grade[i] == 1:
                os.append(grade[i])
            else:
                os.append(grade[i] // divisor)
                grade[v] = grade[i] - grade[i] // divisor
    print(grade)

print(os)
print(grade[0])

