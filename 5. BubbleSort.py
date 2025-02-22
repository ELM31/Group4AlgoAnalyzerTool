import time
#bubblesort 
def bubble_sort(students):
    n = len (students)

    for i in range(n):
        for j in range(0, n-i - 1):
            if students[j][1] > students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]

#take user input 
num_students = int(input("ENTER NUMBER OF STUDENTS: "))
students = []
for _ in range(num_students):
    name = input("Enter Student name: ")
    score = int(input(f"Enter {name}'s Score: "))
    students.append((name, score))
bubble_sort(students)
print("Sorted students by score:", students)

#measrure execution time 
start_time = time.time()
bubble_sort(students)
end_time = time.time()

print("Sorted students by score:", students)
print(f"Execution time: {end_time  - start_time:.6f} seconds")

#time complexity for this algo would be O(n^2)