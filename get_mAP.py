import sys
import matplotlib.pyplot as plt

print('Get mAP from log file.')
print('version 1.0')
print('author: HuanNguyen')
lines_mAP = []

for line in open(sys.argv[1]):
    if "mean average precision (mAP@0.50) = " in line:
        lines_mAP.append(line)

#get mAP
mAP = []
for i in range(len(lines_mAP)):
    lineParts = lines_mAP[i].split(',')
    temp1 = lineParts[1].replace(' or ','')
    temp2 = temp1.replace(' % \n','')
    mAP.append(float(temp2))

print('mAP:')
print(mAP)

fig = plt.figure()
fig.suptitle(str(sys.argv[2]))
plt.plot(mAP,'r.-',label='mAP %')
plt.xlabel('times caculation mAP')
plt.ylabel('mAP %')
plt.legend()
plt.show()