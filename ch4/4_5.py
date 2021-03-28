#快速排序
# 思路与答案基本一致，答案的写法更加简洁，python语音用的更加灵活

def quick_sort_result(array):
    if (len(array) <2):
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<= pivot]
        greater = [i for i in array[1:] if i> pivot]
        return quicksort(less) + [pivot] + quick_sort_result(greater)

def quick_sort_xsj(list):
    if(list == []):
        return []
    else:
        base = list[0]
        A = []
        B = []
        for i in list[1:]:
            if (i>= base):
                B.append(i)
            else:
                A.append(i)
        C = quick_sort_xsj(A)
        D = quick_sort_xsj(B)
        C.append(base)
        return C +D


s = [1,4,2,5,5,6,4,6,7,8,10,20]
print(quick_sort_xsj(s))
