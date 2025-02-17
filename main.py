from algorithm import readDataset, twoPointApproach, threePointApproach
import matplotlib.pyplot as plt

for file in ['datasets/circle_10.txt', 'datasets/circle_20.txt', 'datasets/circle_40.txt', 
             'datasets/circle_100.txt', 'datasets/circle_400.txt']:
    
    points, n = readDataset(file)
    print(f"\n{file}:")
    twoPointApproach(points, n)
    print()
    threePointApproach(points, n)
    print()