# CMPS 2200 Assignment 3
## Answers

**Name:**_________Darian Tocci________________


Place all written answers from `assignment-03.md` here for easier grading.

1 a. For this algorithm, in order to produce the fewest amount of coins as possible when the denominations are powers of 2, we must always choose the largest coin value that does not exceed the remaining amount. 

1b. Greedy choice property: The greedy algorithm always chooses the largest possible coin first. Since powers of 2 coins can combine to form any smaller value, choosing the largest coin never prevents there being an optimal solution. Any smaller combination would require more coins to in order to get to the same value, so this choice is always optimal. Optimal Substructure: After selecting the largest coin 
2^k, the remaining problem is to make change for N-2^K which is smaller but of the same form. The greedy algorithm can be applied recursively to the remaining amount, and since the subproblem structure is identical, the optimal solution for the overall problem is built from the optimal solution of the subproblem.
So, by induction, the greedy algorithm yields the minimum number of coins.

1c. The work is O( log N), because the number of coin denominations is proportional to the number of bits in N. The Span is O(1) if they are computed in parallel. 


2a. Counterexample: If the denominations are 1, 3, 4 and we want to make change for N = 6.
Greedy approach: take 4, then 1, then 1 is total of 3 coins.
Optimal solution: 3 + 3 is a total of 2 coins.
So, the greedy algorithm does not always yield the fewest coins when the denominations are arbitrary.

2b. 

The problem has an optimal substructure because the optimal solution for making change for N can be built from the optimal solutions for smaller values of N. So,

OPT(N) = 0 if N = 0,
otherwise OPT(N) = min(1 + OPT(N - Di)) for all denominations Di ≤ N.

This means that if the best way to make change for N uses one coin of value Di, then the rest of the coins must form an optimal solution for N − Di. Since the remaining amount is a smaller instance of the same problem, the overall problem exhibits optimal substructure.

2c. We can use bottom up dynamic programming to to avoid recomputing subproblems.
MakeChange(D[], N):
    dp[0] = 0
    for i in 1..N:
        dp[i] = ∞
        for each coin in D:
            if coin ≤ i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[N]

    The work is O(Nk), where k is the number of coin denominations.
    And the SPan is O(Nk), where k is the number of coin denominations.

    This  guarantees the minimum number of coins if change can be made, or returns infinity if it’s not possible.
