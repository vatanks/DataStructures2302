#Course: CS 2302 Data Structures
#Assignment: Lab 3 Part 1
#TA: Anindita Nath
#Professor: Olac Fuentes
#Lab purpose: sorting algorithms implemented in different ways
#Author: Shahnaz Vatankhah 9/24/2019
import time

def select_bubble(L,k):
    bubble_sort(L, 1)
    if k > len(L): #check if list contains index k
        return "element is out of list range"
    return L[k]

def bubble_sort(L, n):
    if n < len(L): 
        for i in range(len(L)-n): #recursively iterate over each sublength of L
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]                
        bubble_sort(L, n+1)
    
def select_quick(L,k):
    quick_sort(L, 0, len(L)-1)
    if k > len(L):
        return "element is out of list range"
    return L[k]

def quick_sort(L, low, high):
    if low < high:
        pvotindex = partition(L, low, high)
        quick_sort(L, low, pvotindex-1)
        quick_sort(L, pvotindex+1, high)
    return L

def select_modified_quick(L,k):
    quick_sort2(L, 0, len(L)-1, k)
    if k > len(L):
        return "element is out of list range"
    return L[k]    

def quick_sort2(L, low, high, k):
    if low < high:
        pvotindex = partition(L, low, high)
        if k < pvotindex: #sort left half if k is less than pivot index
            quick_sort2(L, low, pvotindex-1, k)
        else: #sort right half otherwise
            quick_sort2(L, pvotindex+1, high, k)
    return L

def partition(L, low, high):
    mid = (high+1 - low)//2 #select pivot value from median of first, last, and middle index values
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
    L[pvoti], L[low] = L[low], L[pvoti] #begin sorting
    for i in range(low, high+1):
        if L[i] < pvotval:
            border = border +1
            L[border], L[i] = L[i], L[border]
    L[border],L[low] = L[low], L[border]
    return border


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

print("bubble sort test: ")
start_time = time.time()
print("Should return out of bounds")
print(select_bubble(test1, 3))
print("Should return 4")
print(select_bubble(test2, 3))
print("Should return 5")
print(select_bubble(test3, 3))
print("Should return 10")
print(select_bubble(test4, 7))
print("Should return 5")
print(select_bubble(test5, 8))
print("Should return 0")
print(select_bubble(test5, 1))
print("--- %s seconds ---" % (time.time() - start_time - normalized))

test1 = []
test2 = [1,2,3,4,5,6]
test3 = [9,8,7,6,5,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
test4 = [1,0,2,3,7,6,5,99,22,33,44,55,10,18,11,12,12,12,12,12,12,12,12,12,12]
test5 = [0,0,4,5,4,5,6,3,3,6,0,1]

print("quick sort test: ")
start_time = time.time()
print("Should return out of bounds")
print(select_quick(test1, 3))
print("Should return 4")
print(select_quick(test2, 3))
print("Should return 5")
print(select_quick(test3, 3))
print("Should return 10")
print(select_quick(test4, 7))
print("Should return 5")
print(select_quick(test5, 8))
print("Should return 0")
print(select_quick(test5, 1))
print("--- %s seconds ---" % (time.time() - start_time - normalized))

test1 = []
test2 = [1,2,3,4,5,6]
test3 = [9,8,7,6,5,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
test4 = [1,0,2,3,7,6,5,99,22,33,44,55,10,18,11,12,12,12,12,12,12,12,12,12,12]
test5 = [0,0,4,5,4,5,6,3,3,6,0,1]

print("modified quick sort test: ")
start_time = time.time()
print("Should return out of bounds")
print(select_modified_quick(test1, 3))
print("Should return 4")
print(select_modified_quick(test2, 3))
print("Should return 5")
print(select_modified_quick(test3, 3))
print("Should return 10")
print(select_modified_quick(test4, 7))
print("Should return 5")
print(select_modified_quick(test5, 8))
print("Should return 0")
print(select_modified_quick(test5, 1))
print("--- %s seconds ---" % (time.time() - start_time - normalized))

