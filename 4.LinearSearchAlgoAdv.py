#define function to preform linear search, two elements l and t 
def linearSearch(L, T):
    targets =[]
    for index in range(len(L)):
        if L[index] == T:
            targets.append(index) 
    return targets

 
#main function 
user_input = input("Enter number separated by spaces: ")
L = list(map(int, user_input.split()))

T = int(input("Enter the target element to search: "))

#call LinearSearch function function
result = linearSearch(L, T)

#display
print(f"The number was {T} found at the index {result}")