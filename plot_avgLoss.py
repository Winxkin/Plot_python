import sys
import matplotlib.pyplot as plt


print('Plot avg loss from log file.')
print('version 1.0')
print('author: HuanNguyen')
print('argv[1]: file log')
print('argv[2]: batch')
print('argv[3]: title of chart')

lines_avgloss = []
lines_mAP = []
lines_PR = []
for line in open(sys.argv[1]):
    if "avg" in line:
        lines_avgloss.append(line)
    if "mean average precision (mAP@0.50) = " in line:
        lines_mAP.append(line)
    if "for conf_thresh = 0.25, precision" in line:
        lines_PR.append(line)


#get mAP
iterations_mAP = []
mAP = []
for i in range(len(lines_mAP)):
    lineParts = lines_mAP[i].split(',')
    temp1 = lineParts[1].replace(' or ','')
    temp2 = temp1.replace(' % \n','')
    mAP.append(float(temp2))

#get precision, recall 
precision = []
recall = []
for i in range(len(lines_PR)):
    lineParts = lines_PR[i].split(',')
    p = lineParts[1].replace(' precision = ','')
    r = lineParts[2].replace(' recall = ','')
    precision.append(float(p))
    recall.append(float(r))

print(precision)
print(recall)


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

plt.xlabel('Batch Number')
plt.ylabel('Avg Loss')
plt.show()
