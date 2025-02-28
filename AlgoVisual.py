import matplotlib.pyplot as plt
import numpy as np

def plot_algorithm_comparison(algorithms, exeTime, numElem):
    plt.figure(figsize=(12, 7))  # Slightly larger figure for better readability
    x = np.arange(len(algorithms))  # Label locations

    # Create bars with a gradient color
    bars = plt.bar(x, exeTime, color='skyblue', edgecolor='black', linewidth=1)

    plt.xlabel('Algorithms', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title(f'Execution Time Comparison of the Algorithms\n (Number of Elements: {numElem})', fontsize=16, fontweight='bold')
    plt.xticks(x, algorithms, fontsize=10, rotation=45, ha='right')  # Rotate x-axis labels for better fit
    plt.yticks(fontsize=10)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # Dashed grid lines for y-axis
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    plt.show()
