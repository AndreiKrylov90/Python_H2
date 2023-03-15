# числа от 1 до 9 написаны в ряд, 
# можно вставить + и - в любое место, нужно найти все комбинации, сумма которых = 100
                   
n = 3 # на сколько кусков/ интервалов делим нашу последовательность чисел
row = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
for a in range(1, 9 - n + 2):
    for b in range(a + 1, 9 - n + 3):
                first = row[0]
                index = 1
                while index < a:
                    first = int(str(first) + str(row[index]))
                    index += 1
                second = row[a]
                index = a + 1
                while index < b:
                    second = int(str(second) + str(row[index]))
                    index += 1
                third = row[b]
                index = b + 1
                while index < 9:
                     third = int(str(third) + str(row[index]))
                     index += 1
                for i in second, -second:
                    for j in third, -third:
                        if first + i + j == 100:
                                print(first, i, j)

                
n = 4 # на сколько кусков/ интервалов делим нашу последовательность чисел
row = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
for a in range(1, 9 - n + 2):
    for b in range(a + 1, 9 - n + 3):
        for c in range(b + 1, 9 - n + 4):
                first = row[0]
                index = 1
                while index < a:
                    first = int(str(first) + str(row[index]))
                    index += 1
                second = row[a]
                index = a + 1
                while index < b:
                    second = int(str(second) + str(row[index]))
                    index += 1
                third = row[b]
                index = b + 1
                while index < c:
                     third = int(str(third) + str(row[index]))
                     index += 1
                fourth = row[c]
                index = c + 1
                while index < 9:
                     fourth = int(str(fourth) + str(row[index]))
                     index += 1
                for i in second, -second:
                    for j in third, -third:
                        for k in fourth, -fourth:
                            if first + i + j + k == 100:
                                print(first, i, j, k)
                            
n = 6 # на сколько кусков/ интервалов делим нашу последовательность чисел
row = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
for a in range(1, 9 - n + 2):
    for b in range(a + 1, 9 - n + 3):
        for c in range(b + 1, 9 - n + 4):
            for d in range(c + 1, 9 - n + 5):
                for e in range(d + 1, 9 - n + 6):
                    first = row[0]
                    index = 1
                    while index < a:
                        first = int(str(first) + str(row[index]))
                        index += 1
                    second = row[a]
                    index = a + 1
                    while index < b:
                        second = int(str(second) + str(row[index]))
                        index += 1
                    third = row[b]
                    index = b + 1
                    while index < c:
                        third = int(str(third) + str(row[index]))
                        index += 1
                    fourth = row[c]
                    index = c + 1
                    while index < d:
                         fourth = int(str(fourth) + str(row[index]))
                         index += 1
                    fifth = row[d]
                    index = d + 1
                    while index < e:
                         fifth = int(str(fifth) + str(row[index]))
                         index += 1
                    sixth = row[e]
                    index = e + 1
                    while index < 9:
                         sixth = int(str(sixth) + str(row[index]))
                         index += 1
                    for i in second, -second:
                        for j in third, -third:
                            for k in fourth, -fourth:
                                for l in fifth, -fifth:
                                    for m in sixth, -sixth:
                                        if first + i + j + k + l + m == 100:
                                            print(first, i, j, k, l, m)


n = 5 # на сколько кусков/ интервалов делим нашу последовательность чисел
row = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
for a in range(1, 9 - n + 2):
    for b in range(a + 1, 9 - n + 3):
        for c in range(b + 1, 9 - n + 4):
            for d in range(c + 1, 9 - n + 5):
                first = row[0]
                index = 1
                while index < a:
                    first = int(str(first) + str(row[index]))
                    index += 1
                second = row[a]
                index = a + 1
                while index < b:
                    second = int(str(second) + str(row[index]))
                    index += 1
                third = row[b]
                index = b + 1
                while index < c:
                     third = int(str(third) + str(row[index]))
                     index += 1
                fourth = row[c]
                index = c + 1
                while index < d:
                     fourth = int(str(fourth) + str(row[index]))
                     index += 1
                fifth = row[d]
                index = d + 1
                while index < 9:
                     fifth = int(str(fifth) + str(row[index]))
                     index += 1
                for i in second, -second:
                    for j in third, -third:
                        for k in fourth, -fourth:
                            for l in fifth, -fifth:
                                if first + i + j + k + l == 100:
                                            print(first, i, j, k, l)
                
n = 7 # на сколько кусков/ интервалов делим нашу последовательность чисел
row = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
for a in range(1, 9 - n + 2):
    for b in range(a + 1, 9 - n + 3):
        for c in range(b + 1, 9 - n + 4):
            for d in range(c + 1, 9 - n + 5):
                for e in range(d + 1, 9 - n + 6):
                    for f in range(e + 1, 9 - n + 7):
                        first = row[0]
                        index = 1
                        while index < a:
                            first = int(str(first) + str(row[index]))
                            index += 1
                        second = row[a]
                        index = a + 1
                        while index < b:
                            second = int(str(second) + str(row[index]))
                            index += 1
                        third = row[b]
                        index = b + 1
                        while index < c:
                            third = int(str(third) + str(row[index]))
                            index += 1
                        fourth = row[c]
                        index = c + 1
                        while index < d:
                            fourth = int(str(fourth) + str(row[index]))
                            index += 1
                        fifth = row[d]
                        index = d + 1
                        while index < e:
                            fifth = int(str(fifth) + str(row[index]))
                            index += 1
                        sixth = row[e]
                        index = e + 1
                        while index < f:
                            sixth = int(str(sixth) + str(row[index]))
                            index += 1
                        seventh = row[f]
                        index = f + 1
                        while index < 9:
                            seventh = int(str(seventh) + str(row[index]))
                            index += 1
                        for i in second, -second:
                            for j in third, -third:
                                for k in fourth, -fourth:
                                    for l in fifth, -fifth:
                                        for m in sixth, -sixth:
                                            for o in seventh, -seventh:
                                                if first + i + j + k + l + m + o == 100:
                                                    print(first, i, j, k, l, m, o)

n = 8 # на сколько кусков/ интервалов делим нашу последовательность чисел
row = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
for a in range(1, 9 - n + 2):
    for b in range(a + 1, 9 - n + 3):
        for c in range(b + 1, 9 - n + 4):
            for d in range(c + 1, 9 - n + 5):
                for e in range(d + 1, 9 - n + 6):
                    for f in range(e + 1, 9 - n + 7):
                        for g in range(f + 1, 9 - n + 8):
                            first = row[0]
                            index = 1
                            while index < a:
                                first = int(str(first) + str(row[index]))
                                index += 1
                            second = row[a]
                            index = a + 1
                            while index < b:
                                second = int(str(second) + str(row[index]))
                                index += 1
                            third = row[b]
                            index = b + 1
                            while index < c:
                                third = int(str(third) + str(row[index]))
                                index += 1
                            fourth = row[c]
                            index = c + 1
                            while index < d:
                                fourth = int(str(fourth) + str(row[index]))
                                index += 1
                            fifth = row[d]
                            index = d + 1
                            while index < e:
                                fifth = int(str(fifth) + str(row[index]))
                                index += 1
                            sixth = row[e]
                            index = e + 1
                            while index < f:
                                sixth = int(str(sixth) + str(row[index]))
                                index += 1
                            seventh = row[f]
                            index = f + 1
                            while index < g:
                                seventh = int(str(seventh) + str(row[index]))
                                index += 1
                            eight = row[g]
                            index = g + 1
                            while index < 9:
                                eight = int(str(eight) + str(row[index]))
                                index += 1
                            for i in second, -second:
                                for j in third, -third:
                                    for k in fourth, -fourth:
                                        for l in fifth, -fifth:
                                            for m in sixth, -sixth:
                                                for o in seventh, -seventh:
                                                    for p in eight, -eight:
                                                        if first + i + j + k + l + m + o + p == 100:
                                                            print(first, i, j, k, l, m, o, p)