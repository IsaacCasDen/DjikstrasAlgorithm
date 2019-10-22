#!/usr/bin/python3

from concrete import *

import sys

nodes = []
edges = []
paths = []

filename = None
start_node = None
destination_node = None

def readFile(filename):

    with open(filename,"r") as f:
        header = next(f)
        for line in f:
            # print(line.strip('\n'))
            from_node, to_node, weight = line.strip('\n').split(',')
            if not addEdge(from_node,to_node,weight):
                return False
    
    return True

def addEdge(from_node,to_node,weight):
    edge = Edge(from_node,to_node,weight)
    if edge not in edges:
        edges.append(edge)
        node = Node(from_node)
        if node not in nodes:
            nodes.append(node)
        node = Node(to_node)
        if node not in nodes:
            nodes.append(node)
        
    return True

def createRoutes(from_id):
    used_nodes = []
    node = Node(from_id)
    node.hop = Hop(None,0)
    if node not in nodes:
        return False
    
    run = True
    stack = []
    stack.append(node)

    while run:
        paths.append(node)
        used_nodes.append(node)
        e = [edge for edge in edges if edge.from_id==node]
        for edge in e:
            # print(node.hop)
            next_node = Node(edge.to_id)
            next_node.hop = Hop(node,node.hop.distance+edge.weight)
            stack.append(next_node)
        
        stack.sort(key=lambda x:x.hop.distance,reverse=True)
        [print(node,",",node.hop) for node in paths]
        print("---")
        while run:
            node = stack.pop()
            if (node not in used_nodes):
                break
            run = len(stack)>0

def printRoute(destination_node):
    path = []
    if destination_node in paths:
        node = next((x for x in paths if x == destination_node), None)
        while (node.hop != None and node.hop.prev != None):
            path.append(node)
            node = node.hop.prev
        path.append(node)
    
    path.reverse()
    print(path)

if __name__ == "__main__":
    if len(sys.argv)<4:
        print("Usage:\n\t",sys.argv[0],"<FILE> <FROM> <TO>")
        print("FILE\t\tFile containing node edges with weights")
        print("FROM\t\tStarting Node")
        print("TO\t\tDestination Node")
        exit(0)
    
    filename = sys.argv[1]
    start_node = sys.argv[2]
    destination_node = sys.argv[3]

    if not readFile(filename):
        print("Error loading data")
        exit(1)
    
    if not start_node in nodes:
        print("Start not in nodes")
        exit(2)
    
    if not destination_node in nodes:
        print("Destination not in nodes")
        exit(3)

    createRoutes(start_node)
    printRoute(destination_node)