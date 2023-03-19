import sys
import matplotlib.pyplot as plt

print('Get Precision, Recall, F1-score from log file.')
print('version 1.0')
print('author: HuanNguyen')

lines_PR = []
for line in open(sys.argv[1]):
    if "for conf_thresh = 0.25, precision" in line:
        lines_PR.append(line)


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


print('Precision:')
print(precision)
print('Recall:')
print(recall)
print('F1-score:')
print(f1_score)

#change to %
for i in range(0,len(precision)):
    precision[i] = precision[i]*100
    recall[i] = recall[i]*100
    f1_score[i] = f1_score[i]*100

fig = plt.figure()
fig.suptitle(str(sys.argv[2]))
plt.plot(recall,'r.-',label='recall')
plt.plot(precision,'b.-',label='precision')
plt.plot(f1_score,'g.-',label='F1-score')
plt.xlabel('times caculation')
plt.ylabel('percentage %')
plt.legend()
plt.show()
