**Problem Statement:** <br>
Given a 2d array of size _N_*_N_ filled with 0s and 1s. You need to answer _Q_ queries. For each of the _Q_ queries find the number of 1s in a given subrectangle with corners (_X<sub>1</sub>_, _Y<sub>1</sub>_) and (_X<sub>2</sub>_, _Y<sub>2</sub>_), inclusive.

**Constraints:** <br>
 - 1 &le; _N_ &le; 1000
 - 1 &le; _X<sub>1</sub>_ &le; _X<sub>2</sub>_ &le; _N_
 - 1 &le; _Y<sub>1</sub>_ &le; _Y<sub>2</sub>_ &le; _N_

Subtask 1: (30 points)
 - _Q_ = 1

Subtask 2: (70 points)
 - 1 &le; _Q_ &le; 10<sup>5<sup>

**Input Format:** <br>
 - The first line contains 2 integers _N_ and _Q_
 - The next _N_ lines contain _N_ characters (0 / 1) each denoting the elements of the 2d array
 - The next line contains _Q_ integers separated by a space
 - The next _Q_ lines contain 4 space separated integers _X<sub>1</sub>_, _Y<sub>1</sub>_, _X<sub>2</sub>_, _Y<sub>2</sub>_ each

**Output Format:** <br>
 - Print Q lines, each containing a single integer denoting the number of 1s in the given subrectangle

**Sample input:** <br>
```
4
0010
1110
1001
1100
2
1 1 2 2
2 3 4 4
```

**Sample output:** <br>
```
2
2
```