import sys

values = []
with open(sys.argv[1]) as f:
        values = [int(x) for x in f.read().strip("\n").split()]

post_values = []
for v in values:
    iter = [v]
    for i in range(75):
        print(i)
        j = 0
        while j < len(iter):
            if iter[j] == 0:
                iter[j] = 1
                j += 1
                continue

            str_value = str(iter[j])
            if len(str_value) % 2 == 0:
                midPoint = len(str_value)//2
                left = str_value[0:midPoint]
                right = str_value[midPoint:]
                iter[j] = int(left)
                iter.insert(j + 1, int(right))
                j += 2
                continue
            
            iter[j] *= 2024
            j += 1
    post_values.extend(iter)

print(len(post_values))

