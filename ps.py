n = int(input("Enter the number of process: "))
chart = [0]
avg = []
k = ()
p = []
sum = 0

for i in range(0, n):
    process = input("Enter Process: ")
    brust_time = int(input("Enter time: "))
    priority = int(input("Enter priority: "))

    k = (process, brust_time, priority)
    p.append(k)

p.sort(key=lambda x: x[2])

for t in p: 
    chart.append(t[0])

    sum += t[1]
    chart.append(sum)
    avg.append(sum)

print(*chart)
sum = 0

for i in range(0, n-1):
    sum += avg[i]
print('The average waiting time: ', sum/n)
