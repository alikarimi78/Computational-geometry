# importing library :

import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math as mt

# azimuth function :

def azimuth(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    d_x = x1 - x2
    d_y = y1 - y2
    t = mt.atan2(d_x,d_y)
    t = t*180/mt.pi
    if t < 0 :
        t = t + 360
    return t

# right or left turn function :
    
def right_turn (last_three):
    
    point1 = last_three[0]
    point2 = last_three[1]
    point3 = last_three[2]
    
    az1 = azimuth(point1, point2)
    az2 = azimuth(point2, point3)
    if az2 > az1 :
        return True
    else :
        return False
    
# get random points :

n = int(input("enter number of points? "))
a = int(input("enter start range of points? "))
b = int(input("enter end range of points "))

points = np.zeros((n , 2))
sorted_points = np.zeros((n , 2))
for i in range(n):
    points[i , 0]  = rd.randint(a, b)
    points[i , 1] = rd.randint(a, b)


# sorting :

points = sorted(points,key=lambda x: (x[0],x[1]))
backup_points = points.copy()

# plotting before caculte CH :
plt.figure(1)
for i in range(len(backup_points)):
    plt.plot(backup_points[i][0], backup_points[i][1], 'b', marker = "*", linestyle = "") 

# get list of CH_up

ch_up = []
ch_lw = []
ch_up.append(points[0])
ch_up.append(points[1])
ch_up.append(points[2])

# conditions for CH_up:

delete_count = 0
i = 2
while (i < n):

    len_ch = len(ch_up)
    last_three = ch_up[len_ch-3:len_ch]
    con = right_turn(last_three)
    if  con == True :
        i += 1
        if i == n:
            break
        ch_up.append(points[i-delete_count])    
    else :
        plt.plot(points[i-1-delete_count][0],points[i-1-delete_count][1], 'r', marker = "*", linestyle = "")
        plt.show()
        del points[i-1-delete_count]
        del ch_up[i-1-delete_count]
        delete_count += 1
        if len(ch_up) < 3 :     
            i += 1
            ch_up.append(points[i-delete_count])

x = []
y = []

# plotting ch_up

for i in range(len(ch_up)):
    x.append(ch_up[i][0])
    y.append(ch_up[i][1])

plt.plot(x, y, "b", linestyle="solid")
plt.show()

# get list of CH_low boundary :

points = backup_points

ch_lw.append(points[0])
ch_lw.append(points[1])
ch_lw.append(points[2])

# conditions for CH_low

delete_count = 0
i = 2
while (i < n):

    len_lw = len(ch_lw)
    last_three = ch_lw[len_lw-3:len_lw]
    con = right_turn(last_three) 
    if  con == False :
        i += 1
        if i == n:
            break
        ch_lw.append(points[i-delete_count])
    else :
        plt.plot(points[i-1-delete_count][0],points[i-1-delete_count][1], 'r', marker = "*", linestyle = "")
        plt.show()
        del points[i-1-delete_count]
        del ch_lw[i-1-delete_count]
        delete_count += 1
        if len(ch_lw) < 3 :     
            i += 1
            ch_lw.append(points[i-delete_count])

x = []
y = []

# plotting CH_low:
    
for i in range(len(ch_lw)):
    x.append(ch_lw[i][0])
    y.append(ch_lw[i][1])
plt.plot(x, y, "b", linestyle="solid")
plt.show()
        
        