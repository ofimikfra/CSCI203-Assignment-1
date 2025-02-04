from algorithm import readDataset, twoPointApproach, threePointApproach

points, n = readDataset('datasets/circle_20.txt')

print("2 point approach: ",twoPointApproach(points, n)) # test
print("3 point approach: ",threePointApproach(points, n)) # test

# make a for loop to read dataset and run twoPointApproach and threePointApproach for each dataset