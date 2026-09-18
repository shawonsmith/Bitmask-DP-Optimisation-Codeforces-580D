# Bitmask DP Optimisation — Codeforces 580D

An optimised Python implementation of the Codeforces problem **580D — Kefa and Dishes**, developed using Bitmask Dynamic Programming.

## Problem Overview

Kefa can choose exactly `m` dishes from `n` available dishes. Each dish provides a satisfaction value. Eating certain dishes consecutively may also provide an additional satisfaction bonus.

The objective is to determine the best selection and eating order that produces the maximum possible satisfaction.

**Original problem:** [Codeforces 580D — Kefa and Dishes](https://codeforces.com/problemset/problem/580/D)

## Solution Approach

This solution uses **Bitmask Dynamic Programming** to represent and evaluate different combinations and orders of dishes.

The DP state is:

`dp[mask][last]`

Where:

* `mask` represents the dishes that have already been selected.
* `last` represents the most recently selected dish.
* `dp[mask][last]` stores the maximum satisfaction obtainable for that state.

For every valid state, the algorithm attempts to add an available dish. The updated score includes:

* The satisfaction value of the new dish.
* Any sequence bonus earned by eating the new dish after the previous dish.

## State Transition

When `next_dish` has not yet been selected:

`new_mask = mask | (1 << next_dish)`

The new score is calculated as:

`new_score = current_score + satisfaction[next_dish] + bonus[last][next_dish]`

The DP state is then updated only if the new score is greater than the previously stored score.

## Performance Optimisation

The implementation includes several Python-specific optimisations:

* Uses `sys.stdin.buffer.readline` for faster input.
* Uses bit operations for efficient state representation.
* Iterates only through selected dishes and available dishes.
* Avoids unnecessary full-range loops where possible.
* Skips invalid or unreachable DP states.
* Stops expanding a state after exactly `m` dishes have been selected.

## Complexity Analysis

* **Time Complexity:** `O(2^n × n²)`
* **Space Complexity:** `O(2^n × n)`

The constraints allow this approach because the maximum number of dishes is small enough for bitmask-based state representation.

## Sample Input

```text
4 3 2
1 2 3 4
2 1 5
3 4 2
```

## Sample Output

```text
12
```

## Sample Explanation

One optimal order is:

1. Eat dish 2 and receive `2` satisfaction.
2. Eat dish 1 and receive `1` satisfaction plus a bonus of `5`.
3. Eat dish 4 and receive `4` satisfaction.

Total satisfaction:

`2 + 1 + 5 + 4 = 12`

## Project Structure

```text
Bitmask-DP-Optimisation-Codeforces-580D/
├── .gitignore
├── README.md
└── kefa_and_dishes.py
```

## Technologies and Concepts

* Python
* Dynamic Programming
* Bitmasking
* State Transition
* Algorithm Optimisation
* Competitive Programming
* Problem Solving
* Time and Space Complexity Analysis

## Learning Outcomes

Through this project, I practised:

* Representing subsets using binary masks.
* Designing multidimensional dynamic programming states.
* Applying sequence-dependent bonuses.
* Reducing unnecessary iterations with bitwise operations.
* Optimising Python code for strict execution limits.
* Analysing algorithmic time and memory complexity.

## Running the Solution

Make sure Python 3 is installed, then run:

```bash
python kefa_and_dishes.py
```

Enter the input according to the original Codeforces problem format.

## Submission Status

- **Verdict:** Accepted ✅
- **Problem:** Codeforces 580D — Kefa and Dishes
- **Language:** PyPy 3
- **Rating:** 1800
- **Techniques:** Bitmasking and Dynamic Programming
- **Submission:** [View Accepted Submission](https://codeforces.com/contest/580/submission/391171501)

## Author

**Shawon Khan**

- GitHub: [shawonsmith](https://github.com/shawonsmith)
