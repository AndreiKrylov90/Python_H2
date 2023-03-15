# числа от 1 до 9 написаны в ряд, 
# можно вставить + и - в любое место, нужно найти все комбинации, сумма которых = 100

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
                if (first + second + third + fourth + fifth) == 100:
                    print(f"{first} + {second} + {third} + {fourth} + {fifth}")
                if (first + second + third + fourth - fifth) == 100:
                    print(f"{first} + {second} + {third} + {fourth} - {fifth}")
                if (first + second + third - fourth + fifth) == 100:
                    print(f"{first} + {second} + {third} - {fourth} + {fifth}")
                if (first + second + third - fourth - fifth) == 100:
                    print(f"{first} + {second} + {third} - {fourth} - {fifth}")
                if (first + second - third + fourth + fifth) == 100:
                    print(f"{first} + {second} - {third} + {fourth} + {fifth}")
                if (first + second - third + fourth - fifth) == 100:
                    print(f"{first} + {second} - {third} + {fourth} - {fifth}")
                if (first + second - third - fourth + fifth) == 100:
                    print(f"{first} + {second} - {third} - {fourth} + {fifth}")
                if (first + second - third - fourth - fifth) == 100:
                    print(f"{first} + {second} - {third} - {fourth} - {fifth}")
                if (first - second + third + fourth + fifth) == 100:
                    print(f"{first} - {second} + {third} + {fourth} + {fifth}")
                if (first - second + third + fourth - fifth) == 100:
                    print(f"{first} - {second} + {third} + {fourth} - {fifth}")
                if (first - second + third - fourth + fifth) == 100:
                    print(f"{first} - {second} + {third} - {fourth} + {fifth}")
                if (first - second + third - fourth - fifth) == 100:
                    print(f"{first} - {second} + {third} - {fourth} - {fifth}")
                if (first - second - third + fourth + fifth) == 100:
                    print(f"{first} - {second} - {third} + {fourth} + {fifth}")
                if (first - second - third + fourth - fifth) == 100:
                    print(f"{first} - {second} - {third} + {fourth} - {fifth}")
                if (first - second - third - fourth + fifth) == 100:
                    print(f"{first} - {second} - {third} - {fourth} + {fifth}")
                if (first - second - third - fourth - fifth) == 100:
                    print(f"{first} - {second} - {third} - {fourth} - {fifth}")
                
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
                if (first + second + third + fourth) == 100:
                    print(f"{first} + {second} + {third} + {fourth}")
                if (first + second + third - fourth) == 100:
                    print(f"{first} + {second} + {third} - {fourth}")
                if (first + second - third + fourth) == 100:
                    print(f"{first} + {second} - {third} + {fourth}")
                if (first + second - third - fourth) == 100:
                    print(f"{first} + {second} - {third} - {fourth}")
                if (first - second + third + fourth) == 100:
                    print(f"{first} - {second} + {third} + {fourth}")
                if (first - second + third - fourth) == 100:
                    print(f"{first} - {second} + {third} - {fourth}")
                if (first - second - third + fourth) == 100:
                    print(f"{first} - {second} - {third} + {fourth}")
                if (first - second - third - fourth) == 100:
                    print(f"{first} + {second} + {third} + {fourth}")
                
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
                if (first + second + third) == 100:
                    print(f"{first} + {second} + {third}")
                if (first + second - third) == 100:
                    print(f"{first} + {second} - {third}")
                if (first - second + third) == 100:
                    print(f"{first} - {second} + {third}")
                if (first - second - third) == 100:
                    print(f"{first} - {second} - {third}")
                
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
                    sixth = row[d]
                    index = d + 1
                    while index < 9:
                         sxith = int(str(sixth) + str(row[index]))
                         index += 1
                if (first + second + third + fourth + fifth + sixth) == 100:
                    print(f"{first} + {second} + {third} + {fourth} + {fifth} + {sixth}")
                if (first + second + third + fourth + fifth - sixth) == 100:
                    print(f"{first} + {second} + {third} + {fourth} + {fifth} - {sixth}")
                if (first + second + third + fourth - fifth + sixth) == 100:
                    print(f"{first} + {second} + {third} + {fourth} - {fifth} + {sixth}")
                if (first + second + third + fourth - fifth - sixth) == 100:
                    print(f"{first} + {second} + {third} + {fourth} - {fifth} - {sixth}")
                if (first + second + third - fourth + fifth + sixth) == 100:
                    print(f"{first} + {second} + {third} - {fourth} + {fifth} + {sixth}")
                if (first + second + third - fourth + fifth - sixth) == 100:
                    print(f"{first} + {second} + {third} - {fourth} + {fifth} - {sixth}")
                if (first + second + third - fourth - fifth + sixth) == 100:
                    print(f"{first} + {second} + {third} - {fourth} - {fifth} + {sixth}")
                if (first + second + third - fourth - fifth - sixth) == 100:
                    print(f"{first} + {second} + {third} - {fourth} - {fifth} - {sixth}")
                if (first + second - third + fourth + fifth + sixth) == 100:
                    print(f"{first} + {second} - {third} + {fourth} + {fifth} + {sixth}")
                if (first + second - third + fourth + fifth - sixth) == 100:
                    print(f"{first} + {second} - {third} + {fourth} + {fifth} - {sixth}")
                if (first + second - third + fourth - fifth + sixth) == 100:
                    print(f"{first} + {second} - {third} + {fourth} - {fifth} + {sixth}")
                if (first + second - third + fourth - fifth - sixth) == 100:
                    print(f"{first} + {second} - {third} + {fourth} - {fifth} - {sixth}")
                if (first + second - third - fourth + fifth + sixth) == 100:
                    print(f"{first} + {second} - {third} - {fourth} + {fifth} + {sixth}")
                if (first + second - third - fourth + fifth - sixth) == 100:
                    print(f"{first} + {second} - {third} - {fourth} + {fifth} - {sixth}")
                if (first + second - third - fourth - fifth + sixth) == 100:
                    print(f"{first} + {second} - {third} - {fourth} - {fifth} + {sixth}")
                if (first + second - third - fourth - fifth - sixth) == 100:
                    print(f"{first} + {second} - {third} - {fourth} - {fifth} - {sixth}")
                if (first - second + third + fourth + fifth + sixth) == 100:
                    print(f"{first} - {second} + {third} + {fourth} + {fifth} + {sixth}")
                if (first - second + third + fourth + fifth - sixth) == 100:
                    print(f"{first} - {second} + {third} + {fourth} + {fifth} - {sixth}")
                if (first - second + third + fourth - fifth + sixth) == 100:
                    print(f"{first} - {second} + {third} + {fourth} - {fifth} + {sixth}")
                if (first - second + third + fourth - fifth - sixth) == 100:
                    print(f"{first} - {second} + {third} + {fourth} - {fifth} - {sixth}")
                if (first - second + third - fourth + fifth + sixth) == 100:
                    print(f"{first} - {second} + {third} - {fourth} + {fifth} + {sixth}")
                if (first - second + third - fourth + fifth - sixth) == 100:
                    print(f"{first} - {second} + {third} - {fourth} + {fifth} - {sixth}")
                if (first - second + third - fourth - fifth + sixth) == 100:
                    print(f"{first} - {second} + {third} - {fourth} - {fifth} + {sixth}")
                if (first - second + third - fourth - fifth - sixth) == 100:
                    print(f"{first} - {second} + {third} - {fourth} - {fifth} - {sixth}")
                if (first - second - third + fourth + fifth + sixth) == 100:
                    print(f"{first} - {second} - {third} + {fourth} + {fifth} + {sixth}")
                if (first - second - third + fourth + fifth - sixth) == 100:
                    print(f"{first} - {second} - {third} + {fourth} + {fifth} - {sixth}")
                if (first - second - third + fourth - fifth + sixth) == 100:
                    print(f"{first} - {second} - {third} + {fourth} - {fifth} + {sixth}")
                if (first - second - third + fourth - fifth - sixth) == 100:
                    print(f"{first} - {second} - {third} + {fourth} - {fifth} - {sixth}")
                if (first - second - third - fourth + fifth + sixth) == 100:
                    print(f"{first} - {second} - {third} - {fourth} + {fifth} + {sixth}")
                if (first - second - third - fourth + fifth - sixth) == 100:
                    print(f"{first} - {second} - {third} - {fourth} + {fifth} - {sixth}")
                if (first - second - third - fourth - fifth + sixth) == 100:
                    print(f"{first} - {second} - {third} - {fourth} - {fifth} + {sixth}")
                if (first - second - third - fourth - fifth - sixth) == 100:
                    print(f"{first} - {second} - {third} - {fourth} - {fifth} - {sixth}")
                
