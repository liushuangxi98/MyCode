def permute(data, i, length):
    if i == length:
        a.append(data[::])
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


a = []
permute([1, 2, 3, 4], 0, 4)
print(a)
