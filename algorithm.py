import math as m

class Circle:
    def __init__(self, x=0, y=0, r=float('inf'), area=0):
        self.x = x
        self.y = y
        self.r = r
        self.area = area

def readDataset(file):
    with open(file, 'r') as f:
        first_line = f.readline() 
        lines = f.readlines()  
    points = []
    for line in lines:
        x, y = line.split()
        points.append((float(x), float(y)))
    return points, int(first_line)  

def twoPointApproach(points, n):
    minCircle = Circle()
    minCirclePoints = []
    
    # find largest distance between 2 points
    maxDist = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            dist = m.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if dist > maxDist:
                maxDist = dist
                minCirclePoints = [points[i], points[j]]
    
    # set largest circle as minCircle if there are no valid circles
    if minCirclePoints:
        xc = (minCirclePoints[0][0] + minCirclePoints[1][0]) / 2
        yc = (minCirclePoints[0][1] + minCirclePoints[1][1]) / 2
        rc2 = (maxDist / 2)**2
        minCircle.x = xc
        minCircle.y = yc
        minCircle.r = m.sqrt(rc2)
        minCircle.area = m.pi * rc2

    found = True

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
                found = True
                if rc2 < minCircle.r:
                    minCircle.x = xc
                    minCircle.y = yc
                    minCircle.r = m.sqrt(rc2)
                    minCircle.area = m.pi * rc2
                    minCirclePoints = [points[i], points[j]]
    
    text = "" if found else "No valid circles found, returned circle with largest distance between 2 points."
    print(text)
    print("2-point approach:", minCirclePoints)
    print(f"Midpoint: {round(minCircle.x,4)}, {round(minCircle.y,4)}\nRadius: {round(minCircle.r,4)}\nArea: {round(minCircle.area,4)}")
    return minCircle.x, minCircle.y, minCircle.r, minCircle.area



def threePointApproach(points, n):
    minCircle = Circle()
    minCirclePoints = []
    
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                A = points[i]
                B = points[j]
                C = points[k]

                D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))

                if D == 0:
                    continue

                xc = ((A[0]**2 + A[1]**2) * (B[1] - C[1]) + (B[0]**2 + B[1]**2) * (C[1] - A[1]) + (C[0]**2 + C[1]**2) * (A[1] - B[1])) / D
                yc = ((A[0]**2 + A[1]**2) * (C[0] - B[0]) + (B[0]**2 + B[1]**2) * (A[0] - C[0]) + (C[0]**2 + C[1]**2) * (B[0] - A[0])) / D
                rc2 = (A[0] - xc)**2 + (A[1] - yc)**2

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
                        minCirclePoints = [points[i], points[j], points[k]]

    print("3-point approach:", minCirclePoints)
    print(f"Midpoint: {round(minCircle.x,4)}, {round(minCircle.y,4)}\nRadius: {round(minCircle.r,4)}\nArea: {round(minCircle.area,4)}")
    return minCircle.x, minCircle.y, minCircle.r, minCircle.area