#Selection Sort Algo
import time 
def selection_sort(books):
    n = len(books)
    for i in range(n):
        min_index = i

        for j in range(i +1, n):
            if books[j][1] < books[min_index][1]:
                min_index = j
        books[i], books[min_index] = books[min_index], books[i]

#user Input
num_books = int(input("Enter the number of BOoks: "))
books = []
for _ in range(num_books):
    name = input("Enter Book name:")
    year = int(input(f"Enter {name}'s publication year:"))
    books.append((name, year))

start_time = time.time()
selection_sort(books)
end_time = time.time()

print("Books are sorted by year: ", books)
print(f"Execution time: {end_time  - start_time:.6f} seconds")