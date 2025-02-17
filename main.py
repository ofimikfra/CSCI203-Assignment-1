from algorithm import readDataset, twoPointApproach, threePointApproach
import matplotlib.pyplot as plt

for file in ['datasets/circle_10.txt', 'datasets/circle_20.txt', 'datasets/circle_40.txt', 
             'datasets/circle_100.txt', 'datasets/circle_400.txt']:
    
    points, n = readDataset(file)
    print(f"\n{file}:")
    x2, y2, r2, area2 = twoPointApproach(points, n)
    print()
    x3, y3, r3, area3 = threePointApproach(points, n)
    print()