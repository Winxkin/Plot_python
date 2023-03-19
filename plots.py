import sys
import matplotlib.pyplot as plt

print('Plot avg loss, mAP, Precision, Recall, F1-score from log file.')
print('version 1.0')
print('author: HuanNguyen')

lines_mAP = []
lines_avgloss = []
lines_PR = []
for line in open(sys.argv[1]):
    if "mean average precision (mAP@0.50) = " in line:
        lines_mAP.append(line)
    if "avg" in line:
        lines_avgloss.append(line)
    if "for conf_thresh = 0.25, precision" in line:
        lines_PR.append(line)

iterations = []
avg_loss = []
#get Avg loss
for i in range(len(lines_avgloss)):
    lineParts = lines_avgloss[i].split(',')
    iterations.append(int(lineParts[0].split(':')[0]))
    avg_loss.append(float(lineParts[1].split()[0]))

#get precision, recall 
precision = []
recall = []
f1_score = []

for i in range(len(lines_PR)):
    lineParts = lines_PR[i].split(',')
    p = lineParts[1].replace(' precision = ','')
    r = lineParts[2].replace(' recall = ','')
    f1 = lineParts[3].replace(' F1-score = ','')
    precision.append(float(p))
    recall.append(float(r))
    f1_score.append(float(f1))

#change to %
for i in range(0,len(precision)):
    precision[i] = precision[i]*100
    recall[i] = recall[i]*100
    f1_score[i] = f1_score[i]*100

#get mAP
mAP = []
for i in range(len(lines_mAP)):
    lineParts = lines_mAP[i].split(',')
    temp1 = lineParts[1].replace(' or ','')
    temp2 = temp1.replace(' % \n','')
    mAP.append(float(temp2))

print('Precision:')
print(precision)
print('Recall:')
print(recall)
print('F1-score:')
print(f1_score)
print('mAP:')
print(mAP)

fig, (ax1, ax2, ax3)  = plt.subplots(1, 3)
fig.suptitle(str(sys.argv[2]))

#plot avg loss
for i in range(0, len(lines_avgloss)):
    ax1.plot(iterations[i:i+2], avg_loss[i:i+2], '#4000ff')

ax1.set_title('AVG loss')
ax1.set_ylabel('avg loss')
ax1.set_xlabel('epoch')

ax2.plot(recall,'r.-',label='recall')
ax2.plot(precision,'b.-',label='precision')
ax2.plot(f1_score,'g.-',label='F1-score')
ax2.set_xlabel('times caculation')
ax2.set_ylabel('percentage %')
ax2.legend()
ax2.set_title('recall,precision,F1-score')

ax3.plot(mAP,'r.-',label='mAP %')
ax3.set_xlabel('times caculation mAP')
ax3.set_ylabel('mAP %')
ax3.set_title('mAP@0.50')
ax3.legend()

plt.show()