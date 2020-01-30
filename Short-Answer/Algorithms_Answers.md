#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n log n)


c) O(n)



## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

UNDERSTANDING:
-GOAL: We want to determine which floor(f) yields the least broken eggs when dropped
-Floors above f: more broken eggs when dropped
-Floors below f: less broken eggs when dropped

PLANNING:
1) since we know that floors above f lead to more broken eggs, find the middle floor (m) in the building: n//2. 
2) check for broken eggs on middle floor:
    *if there are broken eggs on middle floor(depending on the number of floors, I would consider dividing the halves further before employing this strategy):
        => iterate through the list of lower floors beginning at m-1, checking for broken eggs:
            * if no eggs are broken on m-1:
                => I have found f
            * if any eggs are broken on m-1: 
                => check m+2, and so on, until I find the floor on which no eggs are broken: 'f' 
    *if no eggs are broken on middle floor: 
        => iterate through list of upper floors checking for broken eggs beginning at m+1:
            * if no eggs are broken: 
                => check the floor directly above for broken eggs (m+2), and so on until I find the floor at which eggs are broken. Once I have found that floor, the floor directly below it is 'f'
            * if eggs are broken:
                => the floor below is 'f'

RUNTIME COMPLEXITY:
O(log n) b/c halving n each time loop is run
