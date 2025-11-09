# CMPS 2200 Assignment 3
## Answers

**Name:**_________Darian Tocci________________


Place all written answers from `assignment-03.md` here for easier grading.

1 a. For this algorithm, in order to produce the fewest amount of coins as possible when the denominations are powers of 2, we must always choose the largest coin value that does not exceed the remaining amount. 

1b. Greedy choice property: The greedy algorithm always chooses the largest possible coin first. Since powers of 2 coins can combine to form any smaller value, choosing the largest coin never prevents there being an optimal solution. Any smaller combination would require more coins to in order to get to the same value, so this choice is always optimal. Optimal Substructure: After selecting the largest coin 
2^k, the remaining problem is to make change for N-2^K which is smaller but of the same form. The greedy algorithm can be applied recursively to the remaining amount, and since the subproblem structure is identical, the optimal solution for the overall problem is built from the optimal solution of the subproblem.
So, by induction, the greedy algorithm yields the minimum number of coins.

1c. The work is O( log N), because the number of coin denominations is proportional to the number of bits in N. The Span is O(1) if they are computed in parallel. 

