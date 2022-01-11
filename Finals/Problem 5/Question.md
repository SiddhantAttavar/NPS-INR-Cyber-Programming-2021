# Mr. Beast's Generous Giveaway

## Problem Statement: <br>
YouTube has hired Mr. Beast to host their new event to support rising content creators. As usual, to make things impressive, Jimmy (Mr. Beast) decides to give-away _$M_ in coins.

However, Jimmy's bank only has coins of denominations in the array _F_.

Determine how many ways change can be made for amount $M. There are an infinite number of coins of each denomination

Example: <br>
_M = 4_ <br>
_F = {10,4,1,2}_ <br>
There are 4 ways to make change for _M: {4}, {1,1,1,1}, {2,1,1}, {2,2}_.

## Constraints: <br>
 - 1 &le; _F<sub>i</sub>_ &le; 50 (1 &le; _i_ &le; _X_)
 - 1 &le; _M_ &le; 250
 - 1 &le; _X_ &le; 50

## Input Format: <br>
 - The first line contains two space-separated integers and _M_, _X_ where _M_ is the amount to be given away and _X_ is the number of coin denominations
 - The second line contains space-separated integers that describe the values of each coin type. 

## Output Format: <br>
 - Print a single integer representing the number of ways to make the change

## Sample input: <br>
```
10 4
2 5 3 6
```

## Sample output: <br>
```
5
```
