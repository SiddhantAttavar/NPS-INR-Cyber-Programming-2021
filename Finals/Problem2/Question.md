# H Ram Learns Maths

## Problem Statement: <br>
When he was younger, H Ram’s CS teacher gave him a challenge. She laid out _N_ numbered blocks in a row (_A_) and gave him an integer _X_. She then asked him to find 2 integers i and j such that _A<sub>i</sub>_ + _A<sub>j</sub>_ = _X_.
If there are multiple solutions, he had to print the one where i is minimum (and _j_ is maximum if there are multiple possible values of _j_). Additionally, A is sorted, i.e. Ai ≤ Ai + 1 (1 ≤ i < N)

## Constraints: <br>
 - 1 &le; _A<sub>i</sub>_ &le; 10<sup>9</sup>

Subtask 1: 20 points
 - 1 &le; _N_ &le; 1000

Subtask 1: 80 points
 - 1 &le; _N_ &le; 10<sup>5</sup>

## Input Format: <br>
 - The first line contains two integers _N_ and _X_
 - The second line contains _N_ integers representing _A_

## Output Format: <br>
 - Print two integers _i_ and _j_

## Sample input: <br>
```
4 5
1 2 4 7
```

## Sample output: <br>
```
1 3
```
