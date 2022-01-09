# Double Sum

**Problem Statement:** <br>
You are given an array _A_ of length _N_ as well as an integer _X_. Your task is to find 2 integers _i_ and _j_ such that _A<sub>i</sub>_ + _A<sub>j</sub>_. If there are multiple solutions you must print the one where _i_ is minimum (and _j_ is maximum if there are multiple possible values of _j_). Additionally, you know that _A_ is sorted, i.e. _A<sub>i</sub>_ &le; _A<sub>i + 1</sub>_ (1 &le; i &lt; _N_)

**Constraints:** <br>
 - 1 &le; _A<sub>i</sub>_ &le; 10<sup>9</sup>

Subtask 1: 20 points
 - 1 &le; _N_ &le; 1000

Subtask 1: 80 points
 - 1 &le; _N_ &le; 10<sup>5</sup>

**Input Format:** <br>
 - The first line contains two integers _N_ and _X_
 - The second line contains _N_ integers representing _A_

**Output Format:** <br>
 - Print two integers _i_ and _j_

**Sample input:** <br>
```
4 5
1 2 4 7
```

**Sample output:** <br>
```
1 3
```
