from algorithm import readDataset, twoPointApproach, threePointApproach
import matplotlib.pyplot as plt
import time

for file in ['datasets/circle_10.txt', 'datasets/circle_20.txt', 'datasets/circle_40.txt', 
             'datasets/circle_100.txt', 'datasets/circle_400.txt', 'datasets/circle_800.txt', 'datasets/circle_1000.txt']:
    
    start_time = time.time()
    
    points, n = readDataset(file)
    print(f"\n{file}:")
    twoPointApproach(points, n)
    print()

    end_time_2 = time.time()
    print(f"Execution time (2-point approach): {end_time_2 - start_time:.4f} seconds\n")
    print()

    threePointApproach(points, n)
    print()

    end_time_3 = time.time()
    print(f"Execution time (2-point approach): {end_time_3 - end_time_2:.4f} seconds\n")

    print(f"Total execution time: {end_time_3 - start_time:.4f} seconds\n")
    
    