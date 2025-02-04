import math as m

class Circle:
    def __init__(self, x=0, y=0, r=float('inf'), area=0):
        self.x = x
        self.y = y
        self.r = r
        self.area = area

def readDataset(file):
    with open(file, 'r') as f:
        first_line = f.readline()  # Read the first line
        lines = f.readlines()  # Read the remaining lines
    points = []
    for line in lines:
        x, y = line.split()
        points.append((float(x), float(y)))
    return points, int(first_line)  # Return the points and the number of points

def determinant(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

def threePointApproach(points, n):
    minCircle = Circle()
    
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                # Matrix setup
                mtx_a = [
                    [points[i][0], points[i][1], 1],
                    [points[j][0], points[j][1], 1],
                    [points[k][0], points[k][1], 1]
                ]
                mtx_d = [
                    [points[i][0]**2 + points[i][1]**2, points[i][1], 1],
                    [points[j][0]**2 + points[j][1]**2, points[j][1], 1],
                    [points[k][0]**2 + points[k][1]**2, points[k][1], 1]
                ]
                mtx_e = [
                    [points[i][0]**2 + points[i][1]**2, points[i][0], 1],
                    [points[j][0]**2 + points[j][1]**2, points[j][0], 1],
                    [points[k][0]**2 + points[k][1]**2, points[k][0], 1]
                ]
                mtx_f = [
                    [points[i][0]**2 + points[i][1]**2, points[i][0], points[i][1]],
                    [points[j][0]**2 + points[j][1]**2, points[j][0], points[j][1]],
                    [points[k][0]**2 + points[k][1]**2, points[k][0], points[k][1]]
                ]

                a = determinant(mtx_a)

                if a == 0:
                    continue

                d = determinant(mtx_d)
                e = determinant(mtx_e)
                f = determinant(mtx_f)

                xc = d / (2 * a)
                yc = -e / (2 * a)
                rc2 = (d**2 + e**2 - 4 * a * f) / (4 * a**2)

                valid = True
                for l in range(0, n):
                    if ((points[l][0] - xc)**2 + (points[l][1] - yc)**2) > rc2:
                        valid = False
                        break
                
                if valid:
                    if rc2 < minCircle.r:
                        minCircle.x = xc
                        minCircle.y = yc
                        minCircle.r = m.sqrt(rc2)
                        minCircle.area = m.pi * rc2

    return minCircle.x, minCircle.y, minCircle.r, minCircle.area

def twoPointApproach(points, n):
    minCircle = Circle()
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            xc = (points[i][0] + points[j][0]) / 2
            yc = (points[i][1] + points[j][1]) / 2
            rc2 = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2) / 4

            valid = True
            for k in range(0, n):
                if ((points[k][0] - xc)**2 + (points[k][1] - yc)**2) > rc2:
                    valid = False
                    break
            
            if valid:
                if m.sqrt(rc2) < minCircle.r:
                    minCircle.x = xc
                    minCircle.y = yc
                    minCircle.r = m.sqrt(rc2)
                    minCircle.area = m.pi * rc2
    
    return minCircle.x, minCircle.y, minCircle.r, minCircle.area