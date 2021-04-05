# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:41:24 2021

@author: kumar
"""

from sklearn.neighbors import NearestNeighbors
import numpy as np

def distance(p1, p2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1, lat1 = p1
    lon2, lat2 = p2
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

points = [[28.689519,77.324495],
[28.689431,	77.324347],
[28.689316,	77.324165],
[28.689285,	77.324062]
]
nbrs = NearestNeighbors(n_neighbors=2, metric=distance).fit(points)

distances, indices = nbrs.kneighbors(points)

result = distances[:]
f1=open('C:\\Users\\kumar\\Desktop\\New folder\\point.csv','w')
for row in result:
    np.savetxt(f1,row)
    
f1.close()
ar=np.loadtxt('C:\\Users\\kumar\\Desktop\\New folder\\point.csv').reshape(4,2)
print(ar)