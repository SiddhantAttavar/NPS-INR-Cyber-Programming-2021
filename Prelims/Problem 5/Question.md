**Problem Statement:** <br>
You start at (0, 0). You are given an integer _N_. For each of the _N_ moves input a direction (Up / Down / Left / Right) and number of steps (_A<sub>i</sub>_). At the end of N moves print your location (_X_, _Y_).

**Constraints:** <br>
 - 1 &le; N &le; 10<sup>6</sup>
 - 1 &le; _A<sub>i</sub>_ &le; 100

**Input Format:** <br>
 - The first line contains a single integer _N_
 - The next _N_ lines contain a single letter and a number seperated by space
 - The letter represents a direction (U: Up, D: Down, L: Left, R: Right) and the number represents _A<sub>i</sub>_

**Output Format:** <br>
 - Print 2 space seperated integers _X_ and _Y_ representing the final position

**Sample Input:** <br>
```
5
U 4
L 6
D 2
U 3
R 1
```

**Sample output:** <br>
```
-5 5
```