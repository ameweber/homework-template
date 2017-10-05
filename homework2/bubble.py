a = [1, 3, 4, 10, 9, 11, -9, 0, -100]
j = 1
while j < len(a):
     for i in range(len(a) - j):
          if a[i] > a[i+1]:
               a[i],a[i+1] = a[i+1],a[i]
     j += 1
print(a)

#сложность: O(n^2)
#использует два вложенных цикла.
#во внутреннем последовательно сравниваются пары элементов и если оказывается,
#что предыдущий элемент больше последующего – выполняется перестановка.
#внешний цикл выполняется до тех пор, пока в массиве найдется хоть одна пара элементов,
#нарушающих требуемый порядок


