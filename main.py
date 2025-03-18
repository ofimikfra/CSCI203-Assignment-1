from algorithm import readDataset, twoPointApproach, threePointApproach
import matplotlib.pyplot as plt
import time

def plot_circle(points, center, radius, filename, approach, color):

    fig, ax = plt.subplots(figsize=(6, 6))

    x_vals, y_vals = zip(*points)
    ax.scatter(x_vals, y_vals, color='blue', label='Data Points')

    circle = plt.Circle(center, radius, color=color, fill=False, linewidth=2, label=f'{approach} Approach')
    ax.add_patch(circle)

    ax.scatter(*center, color='green', marker='x', s=100, label='Circle Center')

    padding = max(1, 0.2 * radius)
    ax.set_xlim(min(x_vals) - padding, max(x_vals) + padding)
    ax.set_ylim(min(y_vals) - padding, max(y_vals) + padding)
    ax.set_aspect('equal', adjustable='datalim')
    plt.title(f"Smallest Enclosing Circle for {filename} ({approach} Approach)")
    plt.legend()
    plt.grid()
    plt.show()

for file in ['datasets/circle_10.txt', 'datasets/circle_20.txt', 'datasets/circle_40.txt', 'datasets/circle_100.txt', 'datasets/circle_400.txt', 'datasets/circle_800.txt']:
    
    start_time = time.time()
    
    points, n = readDataset(file)
    print(f"\n{file}:")

    x2, y2, r2, _ = twoPointApproach(points, n)
    end_time_2 = time.time()
    print(f"Execution time (Two-Point Approach): {end_time_2 - start_time:.4f} seconds\n")
    
    plot_circle(points, (x2, y2), r2, file, "Two-Point", "red")

    x3, y3, r3, _ = threePointApproach(points, n)
    end_time_3 = time.time()
    print(f"Execution time (Three-Point Approach): {end_time_3 - end_time_2:.4f} seconds\n")
    
    plot_circle(points, (x3, y3), r3, file, "Three-Point", "green")

    print(f"Total execution time: {end_time_3 - start_time:.4f} seconds\n")
