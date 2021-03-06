# -*- coding: utf-8 -*-
"""Ayush-ngk-LP-2-triadic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RKBHWPFMgU6ouVmh8qZEuTCYadmXptNT
"""

import networkx as nx
import matplotlib.pyplot as plt
  
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (3, 4), (4, 5)])
  
plt.figure(figsize =(10, 10))


print("Triadic closure below :")
e = list(G.edges())
  
def triadic(e):
  new_edges = []
  
  for i in e:
    a, b = i
  
    for j in e:
      x, y = j
  
      if i != j:
        if a == x and (b, y) not in e and (y, b) not in e:
          new_edges.append((b, y))
        if a == y and (b, x) not in e and (x, b) not in e:
          new_edges.append((b, x))
        if b == x and (a, y) not in e and (y, a) not in e:
          new_edges.append((a, y))
        if b == y and (a, x) not in e and (x, a) not in e:
          new_edges.append((a, x))
  
  return new_edges
  
print("The possible new edges according to Triadic closure are :")
print(triadic(e))

print("Similarity measure values are below:")
  
print(list(nx.jaccard_coefficient(G)))

print("Jaccard Coeffi over. ResourceAllocaton index is below to identify missing links")
  
print(list(nx.resource_allocation_index(G)))

print("adamic adar below:")
print(list(nx.adamic_adar_index(G)))

print("Preferential attachtment below :")
print(list(nx.preferential_attachment(G)))

print("Community common neighbour :")
G.add_node('A', community = 0)
G.add_node('B', community = 0)
G.add_node('C', community = 0)
G.add_node('D', community = 0)
G.add_node('E', community = 1)
G.add_node('F', community = 1)
G.add_node('G', community = 1)
G.add_node('H', community = 1)
G.add_node('I', community = 1)
  
G.add_edges_from([('A', 'B'), ('A', 'D'), ('A', 'E'), ('B', 'C'),
                  ('C', 'D'), ('C', 'F'), ('E', 'F'), ('E', 'G'), 
                             ('F', 'G'), ('G', 'H'), ('G', 'I')])
  
nx.draw_networkx(G)