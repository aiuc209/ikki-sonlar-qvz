def juft_elementlar_yigindisi(a, b):
    natija = []
    for i in range(len(a)):
        natija.append(a[i] + b[i])
    return natija

a = [1, 2, 3]
b = [4, 5, 6]
print(juft_elementlar_yigindisi(a, b))
