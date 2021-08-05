# The McAfee Tragedy

**Problem Statement:** <br>
While McAfee mourned its founder’s death, it was threatened by a group of anonymous hackers that have given them an array A with N integers and an integer K. Solving this array by finding the number of quadruples (_i_, _j_, _k_, _l_) such that 1 &le; _i_ < _j_ < _k_ < _l_ &le; _N_ and _A<sub>i</sub>_, _A<sub>j</sub>_, _A<sub>k</sub>_, _A<sub>l</sub>_ add up to _K_, will indicate the number of servers that have been infected in their South China Sea cluster.

Your job is to find this number to solve this small piece of the puzzle.

**Constraints:** <br>
Subtask 1: 20 points
 - 1 &le; _N_ &le; 50

Subtask 2: 30 points
 - 1 &le; _N_ &le; 100

Subtask 3: 50 points
 - 1 &le; _N_ &le; 1000

**Input Format:** <br>
 - The first line contains a single integer _N_
 - The next line contains _N_ space separated integers denoting the elements of _A_

**Output Format:** <br>
 - Print a single integer that is the number of quadruples which satisfy the given criteria

**Sample Input:** <br>
```
6 9
1 3 4 2 4 2
```

**Sample output:** <br>
```
2
```