import bubbleSort
import mergeSort
import quickSort
import radixSort
import linearSearchAlgoAdv
import time
import random
from tkinter import * # For GUI
from tkinter import messagebox # For message pop ups specifically
import AlgoVisual # This is the visualization file
import WindowSet # Sets tool window dimensions off of current screen

##################
#####   GUI  #####
##################
root = Tk()
root.title("ALGO ANALYZER TOOL")

WindowSet.setScreen(root, wRatio = 0.4, hRatio = 0.4) # Dynamically sets window size for program
root.configure(bg='#140042')

# Checks for which sorting algorithm will be used 
checkBS = IntVar(value=0)
checkMS = IntVar(value=0)
checkQS = IntVar(value=0)
checkRS = IntVar(value=0)
checkLS = IntVar(value=0)
checkGo = IntVar(value=0)

# Global array variables
arr = []
numElem = 0

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
    global numElem # Declare numElem as global to modify it
    try:
        num_values = int(num_values_entry.get())
        min_value = int(min_value_entry.get())
        max_value = int(max_value_entry.get())

        if min_value > max_value:
            messagebox.showerror("Input Error", "Minimum value cannot be greater than maximum value.")
            return

        # Generate the array based on user inputs
        arr = [random.randint(min_value, max_value) for _ in range(num_values)]
        #Print out array 
        print(f"Unsorted array generated: {arr} ")
        # Store the user input into variable to display onto graph title
        numElem = num_values
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.") 

# Create frames for layout
algo_frame = Frame(root, bg='#200067')
input_frame = Frame(root, bg='#200067')

algo_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
input_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Label for Algo CheckBox
algo_label = Label(algo_frame, text="Choose the \nAlgorithms you'd \nlike to compare", font=("Fixedsys", 17), fg='#c1bec8',bg='#200067')
algo_label.pack(pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)


# Label and Entry for the number of values
num_values_label = Label(input_frame, 
                         text="Number of Values:", 
                         fg='#c1bec8',bg='#200067',
                         font=("Fixedsys", 17))
num_values_label.pack(pady=10)
num_values_entry = Entry(input_frame, 
                         bg='#6a6a6a', 
                         fg='#c1bec8', 
                         font ='Fixedsys' )
num_values_entry.pack(pady=5)

# Label and Entry for minimum value
min_value_label = Label(input_frame, 
                        text="Minimum Value:", 
                        fg='#c1bec8', 
                        bg='#200067'
                        ,font=("Fixedsys", 17))
min_value_label.pack(pady=10)
min_value_entry = Entry(input_frame, 
                        bg='#6a6a6a', 
                        fg='#c1bec8', 
                        font ='Fixedsys' )
min_value_entry.pack(pady=5)

# Label and Entry for maximum value
max_value_label = Label(input_frame, 
                        text="Maximum Value:", 
                        fg='#c1bec8',
                        bg='#200067',
                        font=("Fixedsys", 17))
max_value_label.pack(pady=10)
max_value_entry = Entry(input_frame, 
                        bg='#6a6a6a', 
                        fg='#c1bec8', 
                        font ='Fixedsys' )
max_value_entry.pack(pady=5)

# Button to generate the array
generate_button = Button(input_frame,
                          text="Generate Array",
                            command=generate_array,
                            activebackground="#6a6a6a",
                            activeforeground="white",
                            anchor="center",
                            bd=3,
                            bg="#200067",
                            cursor="hand2",
                            disabledforeground="gray",
                            fg="#c1bec8",
                            font=("Fixedsys", 17),
                            height=2,
                            highlightbackground="black",
                            highlightcolor="green",
                            highlightthickness=2,
                            justify="left",
                            overrelief="raised",
                            padx=10,
                            pady=5,
                            width=15,
                            wraplength=200
                         )
generate_button.pack(pady=20)


# Create IntVars for checkbox
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

# Create checkboxes for the IntVar()
check1 = Checkbutton(algo_frame, text="Bubble Sort", 
                     variable=var1, onvalue=1, 
                     offvalue=0, 
                     command=lambda: update_check(var1, checkBS), 
                     fg='#c1bec8',
                     bg='#200067',
                     font ='Fixedsys',
                     activebackground='#6a6a6a',
                     activeforeground='#ff00e3')
check1.pack(anchor="w")

check2 = Checkbutton(algo_frame, 
                     text="Merge Sort", 
                     variable=var2, 
                     onvalue=1, 
                     offvalue=0, 
                     command=lambda: update_check(var2, checkMS), 
                     fg='#c1bec8',
                     bg='#200067',
                     font='Fixedsys',
                     activebackground='#6a6a6a',
                     activeforeground='#ff00e3')
check2.pack(anchor="w")

check3 = Checkbutton(algo_frame, 
                     text="Quick Sort", 
                     variable=var3, 
                     onvalue=1, 
                     offvalue=0, 
                     command=lambda: update_check(var3, checkQS), 
                     fg='#c1bec8',bg='#200067',
                     font='Fixedsys',
                     activebackground='#6a6a6a',
                     activeforeground='#ff00e3')
check3.pack(anchor="w")

check4 = Checkbutton(algo_frame, 
                     text="Radix Sort", 
                     variable=var4, 
                     onvalue=1, 
                     offvalue=0, 
                     command=lambda: update_check(var4, checkRS), 
                     fg='#c1bec8',
                     bg='#200067',
                     font='Fixedsys',
                     activebackground='#6a6a6a',
                     activeforeground='#ff00e3')
check4.pack(anchor="w")

check5 = Checkbutton(algo_frame, 
                     text="Linear Search", 
                     variable=var5, 
                     onvalue=1, 
                     offvalue=0, 
                     command=lambda: update_check(var5, checkLS), 
                     fg='#c1bec8',
                     bg='#200067',
                     font='Fixedsys',
                     activebackground='#6a6a6a',
                     activeforeground='#ff00e3')
check5.pack(anchor="w")

# Create a text entry for T next to the Linear Search checkbox
t_value_entry = Entry(algo_frame,
      width=5,
      bg='#6a6a6a',
      fg='#c1bec8',
      font='Fixedsys')

# Use grid to place the checkbox and entry side by side
t_value_entry.pack(anchor="w", padx=25, pady=5)

button = Button(algo_frame,
                text="Analyze",
                command=button_clicked,
                activebackground="#6a6a6a",
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="#200067",
                cursor="hand2",
                disabledforeground="gray",
                fg="#c1bec8",
                font=("Fixedsys", 17),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                overrelief="raised",
                padx=10,
                pady=5,
                width=15,
                wraplength=200)

button.pack(pady = 20)


####################
#### ALGORITHMS ####
####################
def analyze_algorithms():
    global arr  # Access the global arr variable
    if checkGo.get() == 1 and arr:  # Ensure array is not empty
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
            t_value = t_value_entry.get()  # Get the user input for T
            
            if t_value.isdigit():
                T = int(t_value)
            else:
                T = L[random.randint(0, len(L) - 1)]

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
            AlgoVisual.plot_algorithm_comparison(algorithms, exeTime, numElem)

root.mainloop()
