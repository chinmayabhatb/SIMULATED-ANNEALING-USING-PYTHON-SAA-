# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:21:15 2020

@author: LENOVO
"""
import numpy as np
import matplotlib.pyplot as plot

class coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def get_distance(a,b):
        return np.sqrt(np.abs(a.x-b.x)+np.abs(a.y-b.y))

    def total_distance (coords):
        dist = 0
        for first,second in zip(coords[:-1],coords[1:]):
            dist += coordinate.get_distance(first, second)
        dist += coordinate.get_distance(coords[0], coords[-1])
        return dist
if __name__ == '__main__':
        #fill up coordinates
        coords = []
        with open('./data/att48.txt') as f:
            for line in f.readlines():
                city = line.split(' ')
                coords.append(coordinate(int(city[1]), int(city[2])))
        # for i in range(20):
        #     coords.append(coordinate(np.random.uniform(), np.random.uniform()))


        #plot
        fig = plot.figure(figsize=(20,5))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        for first, second in zip(coords[:-1] , coords[1:]):
            ax1.plot([first.x,second.x],[first.y,second.y],'b')
        ax1.plot([coords[0].x,coords[-1].x],[coords[0].y,coords[-1].y] , 'b')
        for c in coords:
           ax1.plot(c.x , c.y,'ro')

        # simulated anneling
        cost0 = coordinate.total_distance(coords)

        T =35
        factor = 0.98
        T_init = T
        for i in range(1000):
           # print(i,'cost =',cost0)
            T = T*factor
            for j in range(1000):
                # exchange two co ordinates and get new neighbour solution
                r1 , r2 = np.random.randint(0,len(coords),size=2)
                temp = coords[r1]
                coords[r1] = coords[r2]
                coords[r2] = temp

                #get new cost function
                cost1 = coordinate.total_distance(coords)

                if cost0 < cost1:
                    cost0 = cost1
                else:
                    x=np.random.uniform()
                    if x< np.exp((cost0 - cost1)/T):
                        cost0 = cost1
                    else:
                        temp = coords[r1]
                        coords[r1] = coords[r2]
                        coords[r2] = temp
        for first , second in zip (coords[:-1] , coords[1:]):
            ax2.plot([first.x, second.x], [first.y, second.y], 'b')
        ax2.plot([coords[0].x, coords[-1].x], [coords[0].y, coords[-1].y], 'b')
        for c in coords:
            ax2.plot(c.x, c.y, 'ro')
        plot.show()








