import bubbleSort
import mergeSort
import quickSort
import radixSort
import linearSearchAlgoAdv
import time
import random

###################
### ALGORITHMS ####
###################

###### BUBBLE SORT ###### 

#take user input 
num_students = int(input("ENTER NUMBER OF STUDENTS: "))
students = []
for _ in range(num_students):
    name = input("Enter Student name: ")
    score = int(input(f"Enter {name}'s Score: "))
    students.append((name, score))
bubbleSort.bubble_sort(students)
print("Sorted students by score:", students)

#measrure execution time 
start_time = time.time()
bubbleSort.bubble_sort(students)
end_time = time.time()

print("Sorted students by score:", students)
print(f"Execution time: {end_time  - start_time:.6f} seconds")
#time complexity for this algo would be O(n^2)


###### MERGE SORT ######

#Take user input 
num_flights = int(input("Enter number of flights: "))
flights = []

for _ in range(num_flights):
    flight_no = input("Enter the flight number: ")
    dep_time = int(input(f"Enter the deptrue time for {flight_no}: "))
    flights.append((flight_no, dep_time))
#measure the execution time 
start_time = time.time()
mergeSort.merge_sort(flights)
end_time = time.time()

print("Flights sorted by depature time: ", flights)
print(f"Execution tim: {end_time - start_time:.6f} seconds ")


###### QUICK SORT ######
#Generate random Numbers 
random_list = [random.randint(10, 9999) for _ in range(10)]


print("Orginal Array =: ", random_list)
sorted_arr = quickSort.quick_sort(random_list)
print("Sorted Array =: ", sorted_arr)



###### RADIX SORT ######
#generate a random list of numbers 
random_list = [random.randint(10, 9999) for _ in range (10)]

print("Original Array:", random_list)
sorted_arr = radixSort.radix_sort(random_list)
print("Sorted Array:", sorted_arr)


###### LINEAR SEARCH ######
user_input = input("Enter number separated by spaces: ")
L = list(map(int, user_input.split()))

T = int(input("Enter the target element to search: "))

#call LinearSearch function function
result = linearSearchAlgoAdv.linearSearch(L, T)

#display
print(f"The number was {T} found at the index {result}")