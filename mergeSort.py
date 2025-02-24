#merge sort persevers the number of equal elements 
def merge_sort(flights):
    if len(flights) > 1:
        mid = len(flights) // 2 #divide the dataset into two, so we find the middle index 
        left_half = flights[:mid]# divide the list into halfs 
        right_half = flights[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0 

        while i <len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
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

