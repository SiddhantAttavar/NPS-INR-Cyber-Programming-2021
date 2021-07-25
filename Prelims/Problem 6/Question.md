**Problem Statement:** <br>
There is a hidden number _X_. You are given _Q_ queries to find the number. For each query write an integer into STDOUT and read the result from STDIN. The result is "equal to" (=), "greater than" (>), or "less than" (<). 

Note: Terminate the program once you have received the “=” result and make sure to flush the output stream to get input.

**Constraints:** <br>
 - 1 &le; _X_ &le; 1000
 - Q = 11

**Interaction format:** <br>
 - The first line contains and integer _Q_, denoting the number of queries.
 - For each query, print an integer _X_ into STDOUT and read the result from STDIN.
 - The result will be of 3 types:
   - = : The result is equal to _X_ (Terminate your program)
   - \> : The result is greater than _X_
   - < : The result is less than _X_

**Sample interaction:** <br>
```
1
    >
70
    <
46
    =
```