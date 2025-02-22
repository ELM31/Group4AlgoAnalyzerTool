#insertion Sort move largest element into the right side, move right to left
import time #importing time module to measure execution time 

def insertion_sort(cards):
    for i in range(1, len(cards)):
        key = cards[i] #value where the card will be, move largest to key (correction position)
        j = i -1 #index of the last card in the sorted postion 

        #move elements of the sorted portion 
        while j >= 0 and key < cards[j]:
            cards[j+1] = cards[j] #shift the elements to the right 
            j -= 1 #move one step to the left 

        cards[j + 1] = key # place key in its correct position 

#taking user input 
cards = list(map(int, input("Enter Card numbers separated by space: ").split()))

#measure the execution time 
start_time = time.time()
insertion_sort(cards)
end_time = time.time()

#print the sorted cards and execution time 
print("Sorted cards:", cards)
print(f"Execution tim: {end_time - start_time:.6f} seconds ")