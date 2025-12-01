with open('puzzleInput.txt') as f:
    x = f.readlines()
start = 50
key = ''
count = 0
count2 = 0
for i in x:
    key = i[0]
    match key:
        case 'R':
            start += int(i[1:])
            while start > 99:
                start -= 100
                if start != 0:
                    count2 += 1
        case 'L':
            if start == 0:
                start += 100 - int(i[1:])
            else:
                start -= int(i[1:])
            while start < 0:
                start += 100
                count2 += 1
    if start == 0:
        count += 1
        count2 += 1

print(count)
print(count2)
