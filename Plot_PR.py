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

fig = plt.figure()
fig.suptitle(str(sys.argv[2]))
plt.plot(recall,'#ff0000',label='recall')
plt.plot(precision,'#0000ff',label='precision')
plt.plot(f1_score,'#00ff40',label='F1-score')
plt.legend()
plt.show()
