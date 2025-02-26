import matplotlib.pyplot as plt # Library for matplot
import numpy as np # Library for array handling

# Function to generate the bar plot
def plot_algorithm_comparison(algorithms, exeTime):
    plt.figure(figsize=(10, 6))
    x = np.arange(len(algorithms))  # Label locations
    plt.bar(x, exeTime, color = 'skyblue')
    
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Comparison of the Algorithms')
    plt.xticks(x, algorithms)  # Algorithms on x-axis
    plt.grid(True, axis='y')  # Time in seconds on y-axis
    plt.show()
