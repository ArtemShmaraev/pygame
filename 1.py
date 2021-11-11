from math import factorial

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13,
     'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26,
     'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35, 'A': 36, 'B': 37, 'C': 38, 'D': 39,
     'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 50, 'P': 51, 'Q': 52,
     'R': 53, 'S': 54, 'T': 55, 'U': 56, 'V': 57, 'W': 58, 'X': 59, 'Y': 60, 'Z': 61}
s = []
for j in range(int(input())):
    k = input().lstrip("0")
    if k == "":
        k = "0"
    n = 0
    for i in range(len(k)):
        n += d[k[i]] * factorial(len(k))
    s.append([n, j + 1])
s = sorted(s, reverse=True)
c = [s[0][1]]
for i in range(1, len(s)):
    if s[i][0] == s[i - 1][0]:
        c.append(s[i][1])
    else:
        break
print(*sorted(c), sep="\n")













n = input()
t = 0
a = ''
k = 0
while int(n) > 1:
    k = len(n)
    t += 1
    if k % 2 == 0:
        if n[:k // 2] < n[k // 2:]:
            n = n[:k // 2]
            a += '3'
        elif int(n[k // 2:]) == 0:
            n = n[:k // 2]
            a += '3'
        else:
            n = n[k // 2:]
            a += '4'
    elif len(str((int(n) // 2))) % 2 == 0 and int(n) % 2 == 0 or n == '2':
        n = str((int(n) // 2))
        a += '2'
    elif len(str((int(n) // 4))) % 2 == 0 and int(n) % 4 == 0 or n == '4':
        n = str((int(n) // 4))
        a += '22'
    else:
        n = str(int(n) * 2)
        a += '1'
print(t)
print(a)






















from sys import stdin

s = ""
for line in stdin:
    s += line
d = list(map(int, s.split()))

k = []
e = {}
c = 1
g = len(d)
while c < g:
    k.append([d[c], d[c + 1], d[c + 2:c + d[c] + 2]])
    c += d[c] + 2
for i in range(len(k) - 1):
    if sum(k[i][2]) != k[i + 1][1]:
        for j in range(len(k[i][2])):
            if k[i][2][j] != 1:
                k[i][2][j] += 1
    for j in range(len(k[i][2])):
        if k[i][2][j] not in e:
            e[k[i][2][j]] = 1
        else:
            e[k[i][2][j]] += 1

for i in range(d[0]):
    if (i + 1) not in e:
        print("0", end=" ")
    else:
        print(e[i + 1], end=" ")


