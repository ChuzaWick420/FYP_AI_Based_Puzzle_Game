# Prim's Algorithm
## Description[^1]
1. Initialize a tree with a single vertex, chosen arbitrarily from the graph.
2. Grow the tree by one edge: Of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree.
3. Repeat step 2 (until all vertices are in the tree).

## Machine Diagram
<div align="center">
    <img src="../assets/Proj_FYP_Prim's_Algorithm.png">
</div>

## Side Notes
- The starting and ending point will _always_ be connected. In other words, the possibility of dead ends with no possible winning route, is zero.

## References
[^1]: [Wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm#Description)
