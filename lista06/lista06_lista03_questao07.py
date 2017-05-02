sequence = input().split()
size = len(sequence)
times = []
used_numbers = []
repetitions = 0
c = 0
while c < size:
    if sequence[c] not in used_numbers:
        for i in sequence[:]:
            if float(sequence[c]) == float (i):
                repetitions += 1
        used_numbers += [sequence[c]]
        times += [repetitions]

    c += 1
    repetitions = 0

c = 0
while c < len(times):
    if times[c] > 1:
        print(used_numbers[c],"ocorre",times[c],"Vezes")
    else:
        print(used_numbers[c],"ocorre",times[c],"Vez")
    c += 1

