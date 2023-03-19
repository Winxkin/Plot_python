import sys
import matplotlib.pyplot as plt


print('Plot avg loss from log file.')
print('version 1.0')
print('author: HuanNguyen')
print('argv[1]: file log')
print('argv[2]: batch')
print('argv[3]: title of chart')

lines_avgloss = []
for line in open(sys.argv[1]):
    if "avg" in line:
        lines_avgloss.append(line)


iterations = []
avg_loss = []
#get Avg loss
for i in range(len(lines_avgloss)):
    lineParts = lines_avgloss[i].split(',')
    iterations.append(int(lineParts[0].split(':')[0]))
    avg_loss.append(float(lineParts[1].split()[0]))

fig = plt.figure()
fig.suptitle(str(sys.argv[3]))
#plot avg loss
for i in range(0, len(lines_avgloss)):
    plt.plot(iterations[i:i+2], avg_loss[i:i+2], 'b.-')
    if i == int(sys.argv[2]):
        break

plt.xlabel('Epoch')
plt.ylabel('Avg Loss')
plt.show()
