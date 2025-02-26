import bubbleSort
import mergeSort
import quickSort
import radixSort
import linearSearchAlgoAdv
import time
import random
from tkinter import *

##################
#####   GUI  #####
##################
root = Tk()
root.title("ALGO ANALYZER TOOL")
root.geometry("700x600")

# Checks for
checkBS = IntVar(value=0)
checkMS = IntVar(value=0)
checkQS = IntVar(value=0)
checkRS = IntVar(value=0)
checkLS = IntVar(value=0)
checkGo = IntVar(value=0)

def update_check(var, check):
    if var.get() == 1:
        check.set(check.get() + 1)
    else:
        check.set(0)

def button_clicked():
    checkGo.set(1)

# Create IntVars for checkbox
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

# Label for Algo CheckBox
algo_label = Label(root, text="Choose the Algorithms you'd like to compare", font=("Helvetica", 18))
algo_label.pack(pady=15)

# Create checkboxes for the IntVar()
check1 = Checkbutton(root, text="Bubble Sort", variable=var1, onvalue=1, offvalue=0, command=lambda: update_check(var1, checkBS))
check1.pack(pady=(40, 10))

check2 = Checkbutton(root, text="Merge Sort", variable=var2, onvalue=1, offvalue=0, command=lambda: update_check(var2, checkMS))
check2.pack(pady=(40, 10))

check3 = Checkbutton(root, text="Quick Sort", variable=var3, onvalue=1, offvalue=0, command=lambda: update_check(var3, checkQS))
check3.pack(pady=(40, 10))

check4 = Checkbutton(root, text="Radix Sort", variable=var4, onvalue=1, offvalue=0, command=lambda: update_check(var4, checkRS))
check4.pack(pady=(40, 10))

check5 = Checkbutton(root, text="Linear Search", variable=var5, onvalue=1, offvalue=0, command=lambda: update_check(var5, checkLS))
check5.pack(pady=(40, 10))

button = Button(root,
                text="Analyze",
                command=button_clicked,
                activebackground="blue",
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                overrelief="raised",
                padx=10,
                pady=5,
                width=15,
                wraplength=100)

button.pack(padx=20, pady=20)

# Introduction to the program and ask user to check which algorithms they'd like to compare
print("Hello welcome to Algorithm Analyzer Tool")
# take user input
num_arr = int(input("ENTER NUMBER OF SCORES: "))
arr = []
for _ in range(num_arr):
    score = int(input(f"Enter Scores: "))
    arr.append(score)

####################
#### ALGORITHMS ####
####################
def analyze_algorithms():
    if checkGo.get() == 1:
        # Individual arrays for each sorting algorithm
        arrBS = arr[:]  # Bubble sort
        arrMS = arr[:]  # Merge sort
        arrQS = arr[:]  # Quick sort
        arrRS = arr[:]  # Radix sort
        arrLS = arr[:]  # Linear search

        if checkBS.get() == 1:
            ###### BUBBLE SORT ######
            start_time = time.time()
            bubbleSort.bubble_sort(arrBS)
            end_time = time.time()

            print("Sorted Array (Bubble Sort):", arrBS)
            print(f"Execution time FOR BUBBLE SORT: {end_time - start_time:.6f} seconds")

        if checkMS.get() == 1:
            ###### MERGE SORT ######
            start_time = time.time()
            mergeSort.merge_sort(arrMS)
            end_time = time.time()

            print("Sorted Array (Merge Sort):", arrMS)
            print(f"Execution time FOR MERGE SORT: {end_time - start_time:.6f} seconds")

        if checkQS.get() == 1:
            ###### QUICK SORT ######
            start_time = time.time()
            sorted_arr = quickSort.quick_sort(arrQS)
            end_time = time.time()

            print("Sorted Array (Quick Sort):", sorted_arr)
            print(f"Execution time FOR QUICK SORT: {end_time - start_time:.6f} seconds")

        if checkRS.get() == 1:
            ###### RADIX SORT ######
            start_time = time.time()
            sorted_arr = radixSort.radix_sort(arrRS)
            end_time = time.time()

            print("Sorted Array (Radix Sort):", sorted_arr)
            print(f"Execution time FOR RADIX SORT: {end_time - start_time:.6f} seconds")

        if checkLS.get() == 1:
            ###### LINEAR SEARCH ######
            L = arrLS[:]
            T = random.randint(0, num_arr - 1)

            # Call LinearSearch function
            start_time = time.time()
            result = linearSearchAlgoAdv.linearSearch(L, T)
            end_time = time.time()

            print(f"The number was {T} found at the index {result}")
            print(f"Execution time FOR LINEAR SEARCH: {end_time - start_time:.6f} seconds")

        print(f"checkGo is {checkGo.get()}")

# Run the analysis when the GUI starts
root.after(100, analyze_algorithms)

root.mainloop()
