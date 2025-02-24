import bubbleSort
import mergeSort
import quickSort
import radixSort
import linearSearchAlgoAdv
import time
import random 

#Introduction to the program and ask user to check which algorithms they'd like to compare 
print("Hello welcome to Algorithm Analyzer Tool\nPlease indicate which algorithms you'd like to sort. 0 or 1\n")

checkBS = int(input("Bubble Sort: "))
checkMS = int(input("Merge Sort: "))
checkQS = int(input("Quick Sort: "))
checkRS = int(input("Radix Sort: "))
checkLS = int(input("Linear Search: "))




####################
#### ALGORITHMS ####
####################

if checkBS == 1:
    ###### BUBBLE SORT ###### 

    #take user input 
    num_arr = int(input("ENTER NUMBER OF SCORES: "))
    arr = []
    for _ in range(num_arr):
        score = int(input(f"Enter Scores: "))
        arr.append(score)

    #indivdual arrays for each sorting algorithm 
    arrBS = arr #Bubble sort 
    arrMS = arr #Merge sort
    arrQS = arr #Quick sort
    arrRS = arr #Radix sort
    arrLS = arr #Linear search 

    #measrure execution time 
    start_time = time.time()
    bubbleSort.bubble_sort(arrBS)
    end_time = time.time()

    print("Sorted Array:", arrBS)
    print(f"Execution time FOR  BUBBLE SORT: {end_time  - start_time:.6f} seconds")
    #time complexity for this algo would be O(n^2)

if checkMS == 1:
    ###### MERGE SORT ######

    #measure the execution time 
    start_time = time.time()
    mergeSort.merge_sort(arrMS)
    end_time = time.time()

    print("Sorted Array: ", arrMS)
    print(f"Execution time FOR MERGE SORT: {end_time - start_time:.6f} seconds ")

if checkQS == 1:
    ###### QUICK SORT ######

    start_time = time.time()
    sorted_arr = quickSort.quick_sort(arrQS)
    end_time = time.time()
    print("Sorted Array: ", arrQS)
    print(f"Execution time FOR QUICK SORT: {end_time - start_time:.6f} seconds ")

if checkRS == 1:
    ###### RADIX SORT ######

    start_time = time.time()
    sorted_arr = radixSort.radix_sort(arrRS)
    end_time = time.time()
    print("Sorted Array:", sorted_arr)
    print(f"Execution time FOR RADIX SORT: {end_time - start_time:.6f} seconds ")

if checkLS == 1:
    ###### LINEAR SEARCH ######
    L = arrLS

    T = random.randint(0, num_arr-1) 

    #call LinearSearch function function
    result = linearSearchAlgoAdv.linearSearch(L, T)

    #display
    start_time = time.time()
    print(f"The number was {T} found at the index {result}")
    end_time = time.time()
    print(f"Execution time FOR LINEAR SEARCH: {end_time - start_time:.6f} seconds ")
