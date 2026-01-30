# HW 3: Prim's algorithm

In this assignment, you'll implement Prim's algorithm, a non-trivial greedy algorithm used to construct minimum spanning trees. 

## Description of Methods
I referenced these videos:
* https://www.youtube.com/watch?v=cplfcGZmX7I - for general understanding of concept
* https://www.youtube.com/watch?v=EHRqQBlZAtU - had code using heap

For construct_mst I reference these websites:
* https://www.geeksforgeeks.org/dsa/prims-minimum-spanning-tree-mst-greedy-algo-5/ - helpful figure at the beginning
* https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/ - used their implementation of heapq
* https://youcademy.org/prims-mst-algorithm/ - also used this for their implementation of heapq

Used chatgpt's suggestion on how to store weights in mst matrix symmetrically and for help with debugging.

For check_mst I referenced:
* AI overview for figuring out how many edges an MST for a connected graph should have
* HW2 for checking connected graphs

## Tasks

### Coding

* [TODO] Complete the `construct_mst` method found in `mst/graph.py`. All necessary modules have already been imported. You should not rely on any other dependencies (e.g. networkx). 

### Development

* [TODO] Add more assertions to the `check_mst` function in `test/test_mst.py`.
* [TODO] Write at least one more unit test (in the `test_mst.py` file) for your `construct_mst` implementation. (Two unit tests have already been provided: the first operates on a small graph of four nodes, and the second on a larger graph of 140 single cells, projected onto a lower dimensional subspace.)
* [Optional] Make your package `pip` installable. (Refer to prevous assignments for more in-depth information.)
* [Optional] Automate testing with `pytest` and GitHub Actions, and add a status badge to this README file. (Refer to previous assignments for more in-depth information.)

## Getting started

Fork this repository to your own GitHub account. Work on the codebase locally and commit changes to your forked repository. 

You will need following packages:

- [numpy](https://numpy.org/)
- [scikit-learn](https://scikit-learn.org/)
- [pytest](https://docs.pytest.org/en/7.2.x/)

We also strongly recommend you use the built-in [heapq](https://docs.python.org/3/library/heapq.html) module.

## Completing the assignment

Push your code to GitHub with passing unit tests, and submit a link to your repository through this [google form link]([https://forms.gle/guyuWE6hsTiz34WTA](https://docs.google.com/forms/d/e/1FAIpQLSdA3xmIjLZ5_eq9SvC3DHczAdYr6tuRGCHwmFTslspwzboI8A/viewform))

## Grading

### Code (6 points)

* Minimum spanning tree construction works correctly (6)
    * Correct implementation of Prim's algorithm (4)
    * Produces expected output on small graph (1) 
    * Produces expected output on single cell data (1) 

### Unit tests (3 points)

* Complete function "check_mst" (1)
* Write at least two unit tests for MST construction (2)

### Style (1 points)

* Readable code with clear comments and method descriptions (1)

### Extra credit (0.5)

* Github actions/workflow (0.5)
