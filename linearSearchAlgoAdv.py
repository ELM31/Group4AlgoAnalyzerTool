#define function to preform linear search, two elements l and t 
def linearSearch(L, T):
    targets =[]
    for index in range(len(L)):
        if L[index] == T:
            targets.append(index) 
    return targets