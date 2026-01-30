import numpy as np
import heapq
from typing import Union # lets us type-hint that adj_mat can be either a NumPy array or a string path

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """
        self.mst = None
        adj = self.adj_mat # convenience var so we dont have to type self.adj_mat every time
        n = adj.shape[0] # number of nodes = number of rows (or cols) 

        mst_mat = np.zeros((n, n), dtype=float) # placeholder matrix with same dimensions as original adj mat
        in_mst = [False] * n # track which nodes are already in mst matrix

        start = 0 # start at node 0 for now
        in_mst[start] = True # mark the start node as included in the mst matrix [True, False, False, False] 
        num_in_mst = 1 # track how many nodes are in the mst so far

        heap = [] # list to store candidate edges in a min-heap

        # loop through all edges leaving the start node
        for target_node in range(n): 
            weight = adj[start, target_node] # weight from start to current target node
            if target_node!= start and weight!= 0: # if weight isn't 0, the edge exists
                heapq.heappush(heap, (weight, start, target_node)) # push valid edges into the heap

        # keep adding the lowest weighted edge
        while num_in_mst < n: # run until mst contains all n nodes
            weight, source_node, target_node = heapq.heappop(heap) # pop edge with lowest weight

            # skip edges that don't add a new node
            if in_mst[target_node]: # if target node is already in the mst, skip it because it wont expand mst
                continue

            in_mst[target_node] = True # mark this node as in the mst matrix
            num_in_mst += 1
            # add this weight to our mst matrix
            mst_mat[source_node, target_node] = weight
            mst_mat[target_node, source_node] = weight # store symmetrically bc graph is undirected

            # for the newly added node, look at all its edges to the next node
            for next_node in range(n):
                weight2 = adj[target_node, next_node]
                # only push edges if its not in mst yet and isn't a self loop and has a weight
                if not in_mst[next_node] and next_node != target_node and weight2 != 0:
                    heapq.heappush(heap, (weight2, target_node, next_node))

        self.mst = mst_mat