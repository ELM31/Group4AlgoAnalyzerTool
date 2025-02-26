import bubbleSort
import mergeSort
import quickSort
import radixSort
import linearSearchAlgoAdv
import time
import random
from tkinter import *
from tkinter import messagebox
import AlgoVisual # This is the visualization file

##################
#####   GUI  #####
##################
root = Tk()
root.title("ALGO ANALYZER TOOL")
root.geometry("800x600")  # Adjusted size for better fit

# Checks for which sorting algorithm will be used 
checkBS = IntVar(value=0)
checkMS = IntVar(value=0)
checkQS = IntVar(value=0)
checkRS = IntVar(value=0)
checkLS = IntVar(value=0)
checkGo = IntVar(value=0)

# Global array variable
arr = []

def update_check(var, check):
    if var.get() == 1:
        check.set(check.get() + 1)
    else:
        check.set(0)

def button_clicked():
    checkGo.set(1)
    analyze_algorithms()

def generate_array():
    global arr  # Declare arr as global to modify it
    try:
        num_values = int(num_values_entry.get())
        min_value = int(min_value_entry.get())
        max_value = int(max_value_entry.get())

        if min_value > max_value:
            messagebox.showerror("Input Error", "Minimum value cannot be greater than maximum value.")
            return

        # Generate the array based on user inputs
        arr = [random.randint(min_value, max_value) for _ in range(num_values)]
        print("Generated Array:", arr)
        messagebox.showinfo("Array Generated", f"Array: {arr}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.")

# Create frames for layout
algo_frame = Frame(root)
input_frame = Frame(root)

algo_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")
input_frame.grid(row=0, column=1, padx=20, pady=20, sticky="n")

# Label for Algo CheckBox
algo_label = Label(algo_frame, text="Choose the Algorithms you'd like to compare", font=("Helvetica", 14))
algo_label.pack(pady=10)

# Create IntVars for checkbox
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

# Create checkboxes for the IntVar()
check1 = Checkbutton(algo_frame, text="Bubble Sort", variable=var1, onvalue=1, offvalue=0, command=lambda: update_check(var1, checkBS))
check1.pack(anchor="w")

check2 = Checkbutton(algo_frame, text="Merge Sort", variable=var2, onvalue=1, offvalue=0, command=lambda: update_check(var2, checkMS))
check2.pack(anchor="w")

check3 = Checkbutton(algo_frame, text="Quick Sort", variable=var3, onvalue=1, offvalue=0, command=lambda: update_check(var3, checkQS))
check3.pack(anchor="w")

check4 = Checkbutton(algo_frame, text="Radix Sort", variable=var4, onvalue=1, offvalue=0, command=lambda: update_check(var4, checkRS))
check4.pack(anchor="w")

check5 = Checkbutton(algo_frame, text="Linear Search", variable=var5, onvalue=1, offvalue=0, command=lambda: update_check(var5, checkLS))
check5.pack(anchor="w")

button = Button(algo_frame,
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

button.pack(pady=20)

# Label and Entry for the number of values
num_values_label = Label(input_frame, text="Number of Values:")
num_values_label.pack(pady=10)
num_values_entry = Entry(input_frame)
num_values_entry.pack(pady=5)

# Label and Entry for minimum value
min_value_label = Label(input_frame, text="Minimum Value:")
min_value_label.pack(pady=10)
min_value_entry = Entry(input_frame)
min_value_entry.pack(pady=5)

# Label and Entry for maximum value
max_value_label = Label(input_frame, text="Maximum Value:")
max_value_label.pack(pady=10)
max_value_entry = Entry(input_frame)
max_value_entry.pack(pady=5)

# Button to generate the array
generate_button = Button(input_frame, text="Generate Array", command=generate_array)
generate_button.pack(pady=20)

# Introduction to the program 
print("Hello welcome to Algorithm Analyzer Tool")


####################
#### ALGORITHMS ####
####################
def analyze_algorithms():
    global arr  # Access the global arr variable
    if checkGo.get() == 1 and arr:  # Ensure arr is not empty
        # Individual arrays for each sorting algorithm
        arrBS = arr[:]  # Bubble sort
        arrMS = arr[:]  # Merge sort
        arrQS = arr[:]  # Quick sort
        arrRS = arr[:]  # Radix sort
        arrLS = arr[:]  # Linear search

        # Lists for the bar plot data
        algorithms = [] # X-axis
        exeTime = [] # Y-axis

        if checkBS.get() == 1:
            ###### BUBBLE SORT ######
            start_time = time.time()
            bubbleSort.bubble_sort(arrBS)
            end_time = time.time()

            print("Sorted Array (Bubble Sort):", arrBS)
            print(f"Execution time FOR BUBBLE SORT: {end_time - start_time:.6f} seconds")

            algorithms.append('Bubble Sort') # Adds value to x-axis
            exeTime.append(end_time - start_time) # Adds value to y-axis

        if checkMS.get() == 1:
            ###### MERGE SORT ######
            start_time = time.time()
            mergeSort.merge_sort(arrMS)
            end_time = time.time()

            print("Sorted Array (Merge Sort):", arrMS)
            print(f"Execution time FOR MERGE SORT: {end_time - start_time:.6f} seconds")

            algorithms.append('Merge Sort')
            exeTime.append(end_time - start_time)

        if checkQS.get() == 1:
            ###### QUICK SORT ######
            start_time = time.time()
            sorted_arr = quickSort.quick_sort(arrQS)
            end_time = time.time()
        
            print("Sorted Array (Quick Sort):", sorted_arr)
            print(f"Execution time FOR QUICK SORT: {end_time - start_time:.6f} seconds")

            algorithms.append('Quick Sort')
            exeTime.append(end_time - start_time)

        if checkRS.get() == 1:
            ###### RADIX SORT ######
            start_time = time.time()
            sorted_arr = radixSort.radix_sort(arrRS)
            end_time = time.time()

            print("Sorted Array (Radix Sort):", sorted_arr)
            print(f"Execution time FOR RADIX SORT: {end_time - start_time:.6f} seconds")

            algorithms.append('Radix Sort')
            exeTime.append(end_time - start_time)

        if checkLS.get() == 1:
            ###### LINEAR SEARCH ######
            L = arrLS[:]
            T = random.randint(0, len(arr) - 1)

            # Call LinearSearch function
            start_time = time.time()
            result = linearSearchAlgoAdv.linearSearch(L, T)
            end_time = time.time()

            print(f"The number was {T} found at the index {result}")
            print(f"Execution time FOR LINEAR SEARCH: {end_time - start_time:.6f} seconds")

            algorithms.append('Linear Search')
            exeTime.append(end_time - start_time)

        # Displays bar plot given algorithm list is not empty
        if algorithms:
            AlgoVisual.plot_algorithm_comparison(algorithms, exeTime)

root.mainloop()
