**Problem Statement:** <br>
Consider a square of dimension _N_ * _N_ divided into equal squares with dimension 1 * 1. Each square is either empty or filled. The squares are randomly filled. Find the number of pairs of cells which are filled that are in the same row or in the same column of the square.

**Constraints:** <br>
Subtask 1: 40 points
 - 1 &le; _N_ &le; 100

Subtask 2: 60 points
 - 1 &le; _N_ &le; 1000

**Input Format:** <br>
 - The first line contains a single integer _N_
 - The next _N_ lines contain _N_ characters (0 / 1) each denoting the elements of the square

**Output Format:** <br>
 - Print a single integer that is the sum of filled pairs that are in the same row or in the same column of the square

**Sample Input:** <br>
```
3
011
100
101
```

**Sample output:** <br>
```
4
```