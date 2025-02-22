#merge sort persevers the number of equal elements 
import time 

def merge_sort(flights):
    if len(flights) > 1:
        mid = len(flights) // 2 #divide the dataset into two, so we find the middle index 
        left_half = flights[:mid]# divide the list into halfs 
        right_half = flights[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0 

        while i <len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                flights[k] = left_half[i]
                i+= 1
            else: 
                flights[k] = right_half[j]
                j+=1
            k+=1
        while i <len(left_half):
            flights[k] = left_half[i]
            i+=1
            k+=1

        while j <len(right_half):
            flights[k] = right_half[j]
            j+=1
            k+=1

#Take user input 
num_flights = int(input("Enter number of flights: "))
flights = []

for _ in range(num_flights):
    flight_no = input("Enter the flight number: ")
    dep_time = int(input(f"Enter the deptrue time for {flight_no}: "))
    flights.append((flight_no, dep_time))
#measure the execution time 
start_time = time.time()
merge_sort(flights)
end_time = time.time()

print("Flights sorted by depature time: ", flights)
print(f"Execution tim: {end_time - start_time:.6f} seconds ")