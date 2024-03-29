def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [23, 23, 20, 6, 5, 2, -1, -10, -11, -100]

print('Нынешний массив:')
print(arr)

bubble_sort(arr)

print('Отсортированный массив в порядке убывания:')
print(arr)
