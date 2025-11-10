import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

def med_top_down(S, T, MED={}):
    ## look up the memory
    if (S, T) in MED:
        return MED[(S, T)]
    ## base cases
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    ## recursive cases
    if S[0] == T[0]:  # If first characters are the same, move to the next
        MED[(S, T)] = med_top_down(S[1:], T[1:], MED)
    else:
        insert = med_top_down(S, T[1:], MED) + 1  # Insert a character
        delete = med_top_down(S[1:], T, MED) + 1  # Delete a character
        MED[(S, T)] = min(insert, delete)
    
    return MED[(S, T)]
    
def fast_MED(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
    
    

def fast_align_MED(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    backtrack = [[None] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
        backtrack[i][0] = 'del'
    for j in range(n + 1):
        dp[0][j] = j
        backtrack[0][j] = 'ins'
    backtrack[0][0] = None

    # Fill DP and backtrack
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                backtrack[i][j] = 'match'
            else:
                delete = dp[i - 1][j] + 1
                insert = dp[i][j - 1] + 1
                substitute = dp[i - 1][j - 1] + 1

                dp[i][j] = min(delete, insert, substitute)

                if dp[i][j] == substitute:
                    backtrack[i][j] = 'sub'
                elif dp[i][j] == delete:
                    backtrack[i][j] = 'del'
                else:
                    backtrack[i][j] = 'ins'

    # Reconstruct alignment
    aligned_S = ""
    aligned_T = ""
    i, j = m, n

    while i > 0 or j > 0:
        move = backtrack[i][j] if i > 0 and j > 0 else None
        if move in ('match', 'sub'):
            aligned_S = S[i - 1] + aligned_S
            aligned_T = T[j - 1] + aligned_T
            i -= 1
            j -= 1
        elif move == 'del' or (j == 0 and i > 0):
            aligned_S = S[i - 1] + aligned_S
            aligned_T = "-" + aligned_T
            i -= 1
        elif move == 'ins' or (i == 0 and j > 0):
            aligned_S = "-" + aligned_S
            aligned_T = T[j - 1] + aligned_T
            j -= 1

    return aligned_S, aligned_T
