import pytest
import numpy as np
from mst import Graph
from sklearn.metrics import pairwise_distances
from collections import deque


def check_mst(adj_mat: np.ndarray, 
              mst: np.ndarray, 
              expected_weight: int, 
              allowed_error: float = 0.0001):
    """
    
    Helper function to check the correctness of the adjacency matrix encoding an MST.
    Note that because the MST of a graph is not guaranteed to be unique, we cannot 
    simply check for equality against a known MST of a graph. 

    Arguments:
        adj_mat: adjacency matrix of full graph
        mst: adjacency matrix of proposed minimum spanning tree
        expected_weight: weight of the minimum spanning tree of the full graph
        allowed_error: allowed difference between proposed MST weight and `expected_weight`

    TODO: Add additional assertions to ensure the correctness of your MST implementation. For
    example, how many edges should a minimum spanning tree have? Are minimum spanning trees
    always connected? What else can you think of?

    """

    def approx_equal(a, b):
        return abs(a - b) < allowed_error

    total = 0
    for i in range(mst.shape[0]):
        for j in range(i+1):
            total += mst[i, j]
    assert approx_equal(total, expected_weight), 'Proposed MST has incorrect expected weight'

    # additional assertions added below:

    # how many edges should an mst have?
    n = adj_mat.shape[0] # number of nodes
    mst_triu = np.triu(mst, k=1) # extract upper triangle of mst (avoid counting edges twice and ignore diagonal)
    num_edges =  np.count_nonzero(mst_triu) # counts non-zero entries (actual edges) in mst upper triangle
    assert num_edges == n - 1, f'mst should have {n-1} edges, we found {num_edges}' # spanning tree on n nodes has n - 1 edges

    # are msts always connected?
    visited = set([0]) # use to keep track of nodes we've reached so far
    queue = deque([0]) # create FIFO queue with starting node 0

    while queue:
        current_node = queue.popleft() # remove and return oldest node in the queue
        # loop over every node neighbor that's connected to the current_node by an mst edge
        for neighbor in np.where(mst[current_node] > 0)[0]:
            if neighbor not in visited: # if we haven't already reached this neighbor
                visited.add(neighbor) # mark it as now reached
                queue.append(neighbor) # add to queue so we can look at its own neighbors later
    assert len(visited) == n, 'mst not connected' # if connected, we shouldve been able to visit all nodes (n)

    # making sure edges in mst exist in the original adj_mat
    mst_edges = mst > 0 # sets to True whenever mst has an edge
    # index into adj_mat using the mst edge mask
    assert np.all(adj_mat[mst_edges] > 0), 'mst contains edge that is not present in adj_mat' 

    # making sure matrices are symmetric
    assert np.allclose(adj_mat, adj_mat.T), 'adj_mat not symmetric' # use transposed matrix to check symmetry
    assert np.allclose(mst, mst.T), 'mst not symmetric' 

def test_mst_small():
    """
    
    Unit test for the construction of a minimum spanning tree on a small graph.
    
    """
    file_path = './data/small.csv'
    g = Graph(file_path)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 8)


def test_mst_single_cell_data():
    """
    
    Unit test for the construction of a minimum spanning tree using single cell
    data, taken from the Slingshot R package.

    https://bioconductor.org/packages/release/bioc/html/slingshot.html

    """
    file_path = './data/slingshot_example.txt'
    coords = np.loadtxt(file_path) # load coordinates of single cells in low-dimensional subspace
    dist_mat = pairwise_distances(coords) # compute pairwise distances to form graph
    g = Graph(dist_mat)
    g.construct_mst()
    check_mst(g.adj_mat, g.mst, 57.263561605571695)


def test_mst_student():
    """
    
    TODO: Write at least one unit test for MST construction.
    
    """
    pass
