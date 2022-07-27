from tokenize import Double


chart = [0]
b = 0
sum = 0

n = int(input('Enter the number of process: '))

for i in range(0, n):
    p = input()
    chart.append(p)

    b = int(input())
    le = chart[-2]
    sum += le
    temp = le + b
    chart.append(temp)

print('The average waiting time: ', sum/n)
print(*chart)
