# Jeff Needs Help

## Problem Statement: <br>
It is 2090 and Blue Origin’s manned space shuttle beat SpaceX in the race to finding a habitable galaxy.
However, the shuttle is running low on fuel. So, the captain, coincidentally named Jeff, has to find the shortest distance to between the shuttle and every other planet. This is what he knows:
There are _N_ planets. The shuttle is at Planet Green. There are _M_ safe routes connecting the planets. The _ith_ route goes from city _X<sub>i</sub>_ to city _Y<sub>i</sub>_ and has a length of _Z<sub>i</sub>_.
Jeff assigns you this task because you are the smartest in the room. He wants a clear symbol, _-1_ if it is impossible to go to any particular city.

## Constraints: <br>
 - 1 &le; _N_ &le; 10<sup>5</sup>
 - 1 &le; _M_ &le; _min(N × (N - 1) / 2, 10<sup>5</sup>)_
 - 1 &le; &le; _X<sub>i</sub>_, _Y<sub>i</sub>_ &le; _N_ (1 &le; _i_ &le; _M_)
 - 1 &le; _Z<sub>i</sub>_ &le; 10<sup>9</sup> (1 &le; _i_ &le; _M_)
 - (_X<sub>i</sub>_, _Y<sub>i</sub>_) &ne; (_X<sub>j</sub>_, _Y<sub>j</sub>_) (_i_ &ne; _j_, 1 &le; _i_, _j_ &le; _M_)

Subtask 1: 10 points
 - _Z<sub>i</sub>_ = 1 (1 &le; _i_ &le; _N_)

Subtask 2: 20 points
 - _M_ = _N_ - 1

Subtask 3: 20 points
 - 1 &le; _N_ &le; 100

Subtask 4: 30 points
 - 1 &le; _N_ &le; 1000

Subtask 5: 20 points
 - No additional constraints

## Input Format: <br>
 - The first line contains two integers _N_ and _M_
 - The next _M_ lines contain three integers, _X<sub>i</sub>_, _Y<sub>i</sub>_ and _Z<sub>i</sub>_

## Output Format: <br>
 - Print a single line containing _N - 1_ integers where the _ith_ integer represents the shortest distance from the capital city to the _i + 1th_ city

## Sample input: <br>
```
3 3
1 2 3
2 3 1
3 1 1
```

## Sample output: <br>
```
2 1
```
