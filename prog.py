import pandas as pd
import os
import encrypt as enp
from collections import defaultdict
import json
import networkx as nx
import random
import matplotlib.pyplot as plt

class Graph():
    def __init__(self):

        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

def dijsktra(graph, initial, end):

    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

class Dhobi:
    def __init__(self):
        self.totalprice = 0
        self.username = ''
        self.password = ''
        self.d = {'Shirt':0,'Pant':0,'Tshirt':0,'Blanket':0,'Curtain':0,'Shoes':0}
        self.phone = ''
        self.add=''

    def createdatabase(self):
        if not os.path.isfile('Database.csv'):
            df = pd.DataFrame(columns = ['ID','Pass'])
            df.to_csv('Database.csv')

    def initialTable(self):
        self.createdatabase()
        if not os.path.isfile('Table.csv'):
            df = pd.DataFrame(columns = ['ID','Name','Address','Tshirt','Shirt','Jeans','Trousers','Curtain','Towel','Blanket',"Bedsheet"])
            df.to_csv('Table.csv',sep=',')


    def isUser(self,us):
        e = enp()
        with open('Database.csv','r') as f:
            pr = f.readlines()
            for a in f:
                spl = a.split()
                if spl[0].lower()==us.lower() and spl[1].lower()==e.dec(self.password):
                    try:
                        self.phone = spl[2]
                        self.add = spl[3]
                    except IndexError:
                        self.phone = ''
                        self.add = ''
                    return True
                    break
                else:
                    return False

    def existingUser(self):
        e = enp()
        self.username = input('Enter username: ')
        self.password = input('Enter password: ')
        if self.isUser(self.username)==True:
            print('Login')
        else:
            print('Try again')

    def newUser(self):
        e = enp()
        self.username = input('Enter username: ')
        self.password = input('Enter password: ')
        self.phone = input('Enter phone: ')
        self.add = input('Enter address: ')
        with open('Database.csv','a+') as f:
            f.write('{},{},{}\n'.format(self.username,e.en(self.password),self.phone,self.add))

    def distance(self):
        f = open('Table.csv','r')
        graph =Graph()
        edges= []
        unique_vert = []
        ls = []
        for a in f.readlines():
            if(len(a)>1):
                temp = a.split(',')[3].split('-')

                if not temp[0]=='Address':
                    temp[-1]=int(temp[-1])
                    edges.append(tuple(temp))
                    ls.append((temp[0],temp[1]))
                    tes1,tes2 = temp[0],temp[1]
                    if tes1 not in unique_vert:
                        unique_vert.append(tes1)
                    if tes2 not in unique_vert:
                        unique_vert.append(tes2)
        # print(edges)
        # print(unique_vert)
        for edge in edges:
            graph.add_edge(*edge)

        d = {}

        ra = 0
        for a in unique_vert:
            # print(dijsktra(graph,'X',a))
            d[ra]=dijsktra(graph,'X',a)
            # ls.append(dijsktra(graph,'X',a))
            ra+=1
        # print(ls)
        G =nx.Graph()
        G.add_edges_from(ls)
        nx.draw(G,with_labels=True)
        plt.savefig('static/images/test.png')

        strfi = ''
        for a in d:
            strfi+=str(a)+'\t'+str(d[a])+'\n'
        with open('static/styles/distancecomp.txt','w+') as pf:
            pf.write(strfi)


        # print(json.dumps(d))
        # return json.dumps(d)


# a = Dhobi()
# a.distance()
