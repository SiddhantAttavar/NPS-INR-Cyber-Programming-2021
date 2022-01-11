# Elon Musk's Crazy Contraption

## Problem Statement: <br>
In the time that Elon Musk isn’t driving the price of obscure cryptocurrencies to the moon, he thinks of ideas for crazy contraptions. This week he built a machine which takes a number and does the following operations in order:

1. Multiplies the number by 13
2. Multiplies the number by 11
3. Multiplies the number by 7
4. Outputs all the distinct 3-digit numbers possible from the result of the above operations (such that each digit can only be used once).

Elon, to test his machine, does the following _N_ times:

1. Given a 3-digit positive number _K_, he feeds it to the contraption for processing.
2. He then takes the numbers it gives as output, and sends it through the contraption again

Help Elon find the number of distinct 3-digit numbers which the device outputs over the _N_ steps.

## Constraints: <br>
 - Each digit of _K_ is non-zero 

Subtask 1: 20 points
 - 1 &le; _T_ &le; 1000

Subtask 2: 80 points
 - 5 &le; _N_ &le; 10<sup>9</sup>

## Input Format: <br>
 - First line will contain _T_, number of testcases. Then the testcases follow.
 - Each testcase contains of a single line of input, two integers _K_, _N_

## Output Format: <br>
 - For each test case, print the number of distinct 3-digit numbers which the device outputs over the _N_ steps.

## Sample input: <br>
```
1
123 5
```

## Sample output: <br>
```
27
```
