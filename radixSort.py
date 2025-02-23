#radix sort 
def radix_sort(arr):
      #least siginigicant digit approach (LSD)
      #FIND THE MAIXMUM NUMBER TO DETERMINE THE NUMBER DIGITS 
      max_num = max(arr)
      exp = 1 

      #continue sortin for each digit place value 
      while max_num // exp >0: 
            n = len(arr)
            output = [0] *n
            count = [0]* 10 

            #count occurences of each digit in the current place vlaue 
            for i in range(n):
                index = (arr[i] // exp) % 10
                count[index] += 1

            #update count[i] so that it contains actual position in the output[]
            for i in range (1, 10):
                count[i] += count[i -1] #cumulative sum for stable sorting 

            #build the output array by placing elements in correct corer 
            for i in range(n -1, -1,-1): 
                index = (arr[i] // exp) % 10
                output[count[index]-1] = arr[i]
                count[index] -=1 #decrement count to handle duplicates 

            #copy sorted output back to the original array 
            for i in range(n):
                arr[i] = output[i] #overwrite oringinal array with sorted values 
            exp*=10 
      return arr
