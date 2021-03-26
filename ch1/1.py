# 二分法：函数binary_search 接受一个list和一个元素，如果指定的元素包含在数组中，返回其位置;
# xsj:1.难点在查找到最后只剩下两个元素的时候如何处理；
#     2.标准答案有两个地方值得学习：一是while循环的条件有带等号；二是猜的不对后，我只是直接
#       移动了high和low，答案使用了加一和减一的操作，可以有效解决最后剩下两个元素的问题；


def binary_search_xsj(AList, AElement): #xsj
    low = 0
    high = len(AList) -1
    Mid = int((low + high)/2)
    while( high >low):
        if (AElement <AList[low] or AElement > AList[high]):
            return None
        elif (high -low ==1):
            if(AList[high] == AElement):
                return high
            elif (AList[low] == AElement):
                return low
            else:
                return None
        elif(AList[Mid] > AElement):
            high = Mid
        elif (AList[Mid] < AElement):
            low = Mid
        else:
            return Mid
        Mid = int((low + high)/2)

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while(low <= high):
        mid =int( (high + low)/2)
        guess = list[mid]
        if(guess < item):
           low = mid +1
        elif(guess > item):
            high = mid -1
        else:
            return mid
    return None
A = [1,2,3,4,5,6,7,8,9,10,11,12]
# A = [1,2]
a = 10
location = binary_search(A, a)
print(location)
