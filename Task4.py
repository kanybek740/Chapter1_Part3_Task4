# Minimal positive integer:
# //Find minimal positive integer that is not in list. If list contains only n
# Example: [1,2,3,4,6] - Answer 5
# Example: [1,2,3] - Answer 4
# Example: [-1, -2, -6] - Answer 1
# Create effective algorithm

a = input('napiwite chisla cherez probel: ').split(',')
b = a 
for i in range(len(b)):
    b[i] = int(b[i])
b.sort()
print(b)

for i  in range(1, max(b)):
    if i > 0 and i not in b:
        print(i)