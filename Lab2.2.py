#Course: CS 2302 Data Structures
#Assignment: Lab 3 Part 2
#TA: Anindita Nath
#Professor: Olac Fuentes
#Lab purpose: sorting algorithms implemented in different ways
#Author: Shahnaz Vatankhah 9/24/2019
import time

def select_quick2(L,k):
    qsort_stack(L)
    if k > len(L):
        return "element is out of list range"
    return L[k]
  

def select_modified_quick2(L,k):
    if k > len(L):
        return "element is out of list range"
    quick_sort3(L, 0, len(L)-1, k)
    return L[k]


def quick_sort3(L, low, high, k):
    pvotindex = partition(L, low, high)
    while k <= pvotindex: #sort left half if k is less than or equal to pivot index
        pvotindex = partition(L, low, pvotindex-1)
    while k >= pvotindex:
        pvotindex = partition(L, pvotindex+1, high)
    return L


def partition(L, low, high):
    mid = (high+1 - low)//2
    pvoti = mid
    if L[mid] < L[high] and L[mid] < L[low]:
        if L[high] < L[low]:
            pvoti = high
        else:
            pvoti = low
    elif L[high] < L[mid] and L[high] < L[low]:
        if L[mid] < L[low]:
            pvoti = mid
        else:
            pvoti = low        
    else:
        pvoti = high
    pvotval = L[pvoti]
    border = low
    L[pvoti], L[low] = L[low], L[pvoti]
    for i in range(low, high+1):
        if L[i] < pvotval:
            border = border +1
            L[border], L[i] = L[i], L[border]
    L[border],L[low] = L[low], L[border]
    return border

def qsort_stack(L):
    myStack = [] #create stack list and add first & last index
    myStack.append(0)
    myStack.append(len(L))
    while len(myStack) > 0:
        high = myStack.pop()
        low = myStack.pop()
        if (high - low) >= 2: #simulate recursive calls by storing partition index values in stack list
            border = partition(L, low, high-1)
            myStack.append(border+1)
            myStack.append(high)
            myStack.append(low)
            myStack.append(border)
    return L

start_time = time.time()
print("Should return out of bounds")
print("Should return 4")
print("Should return 5")
print("Should return 10")
print("Should return 5")
print("Should return 0")
normalized = time.time() - start_time
        
test1 = []
test2 = [1,2,3,4,5,6]
test3 = [9,8,7,6,5,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
test4 = [1,0,2,3,7,6,5,99,22,33,44,55,10,18,11,12,12,12,12,12,12,12,12,12,12]
test5 = [0,0,4,5,4,5,6,3,3,6,0,1]

print("quick sort stack test: ")
start_time = time.time()
print("Should return out of bounds")
print(select_quick2(test1, 3))
print("Should return 4")
print(select_quick2(test2, 3))
print("Should return 5")
print(select_quick2(test3, 3))
print("Should return 10")
print(select_quick2(test4, 7))
print("Should return 5")
print(select_quick2(test5, 8))
print("Should return 0")
print(select_quick2(test5, 1))
print("--- %s seconds ---" % (time.time() - start_time - normalized))

test1 = []
test2 = [1,2,3,4,5,6]
test3 = [9,8,7,6,5,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
test4 = [1,0,2,3,7,6,5,99,22,33,44,55,10,18,11,12,12,12,12,12,12,12,12,12,12]
test5 = [0,0,4,5,4,5,6,3,3,6,0,1]

print("modified quick sort non-recursive test: ")

print("Should return out of bounds")
start_time = time.time()
print(select_modified_quick2(test1, 3))
print("Should return 4")
print(select_modified_quick2(test2, 3))
print("Should return 5")
print(select_modified_quick2(test3, 3))
print("Should return 10")
print(select_modified_quick2(test4, 7))
print("Should return 5")
print(select_modified_quick2(test5, 8))
print("Should return 0")
print(select_modified_quick2(test5, 1))
print("--- %s seconds ---" % (time.time() - start_time - normalized))
