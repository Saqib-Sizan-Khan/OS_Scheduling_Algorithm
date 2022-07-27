n = int(input('Enter the number of process: '))
chart = {}
d = [0]
sum = 0

for i in range(0, n):
    key = input("Enter Process: ")
    value = int(input("Enter time: "))
    chart[key] = value

chart = sorted(chart.items(), key=lambda x: x[1])

for k, v in chart:
    le = d[-1]
    sum += le
    temp = le + v

    d.append(k)
    d.append(temp)

print('The average waiting time: ', sum/n)
print(*d)
