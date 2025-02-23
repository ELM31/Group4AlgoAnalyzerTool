#bubblesort 
def bubble_sort(students):
    n = len (students)

    for i in range(n):
        for j in range(0, n-i - 1):
            if students[j][1] > students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]

