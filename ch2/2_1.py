#选择排序
def findSmallest(arr):
    smallest = arr[0] #存储最小元素
    smallest_index = 0 #存储最小元素的索引
    for i in range(1, len(arr)):
        if(arr[i] < smallest):
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = [] #存放新数组
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 19]))
