# Bitmask DP Optimisation — Codeforces 580D

An accepted PyPy 3 solution for the Codeforces problem **580D — Kefa and Dishes**, implemented with Bitmask Dynamic Programming.

[![Codeforces](https://img.shields.io/badge/Codeforces-580D-1F8ACB?logo=codeforces)](https://codeforces.com/problemset/problem/580/D)
[![Verdict](https://img.shields.io/badge/Verdict-Accepted-brightgreen)](https://codeforces.com/contest/580/submission/391171501)
[![Language](https://img.shields.io/badge/Language-PyPy%203-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Problem Overview

Kefa must choose exactly `m` dishes from `n` available dishes. Every dish has a base satisfaction value, and eating certain dishes consecutively can add an order-dependent bonus.

The objective is to find the selection and eating order that maximises total satisfaction.

- **Problem:** [Codeforces 580D — Kefa and Dishes](https://codeforces.com/problemset/problem/580/D)
- **Rating:** 1800
- **Constraints:** `1 ≤ m ≤ n ≤ 18`
- **Techniques:** Bitmasking, Dynamic Programming

## Dynamic Programming Approach

The state is:

```text
dp[mask][last]
```

- `mask` represents the set of dishes already selected.
- `last` represents the most recently eaten dish.
- `dp[mask][last]` stores the maximum satisfaction achievable for that state.

If `next_dish` has not been selected, the transition is:

```text
new_mask = mask | (1 << next_dish)

new_score = dp[mask][last]
            + satisfaction[next_dish]
            + bonus[last][next_dish]
```

The answer is the best reachable state containing exactly `m` selected dishes.

## Why Bitmask DP?

The order of the selected dishes matters because bonuses depend on consecutive pairs. Tracking only the number of selected dishes is therefore insufficient.

A bitmask records the chosen subset, while `last` preserves the information needed to calculate the next transition bonus. With `n ≤ 18`, all subsets can be explored efficiently.

## Python Optimisations

- Uses `sys.stdin.buffer.readline` for fast input.
- Represents selected dishes with integer bitmasks.
- Iterates through set bits instead of scanning all dishes repeatedly.
- Skips unreachable states.
- Stops expanding states after exactly `m` dishes are selected.
- Uses a precomputed mapping from isolated bits to dish indices.

## Complexity

- **Time:** `O(2^n × n²)`
- **Space:** `O(2^n × n)`

## Accepted Submission

- **Verdict:** Accepted ✅
- **Language:** PyPy 3
- **Submission ID:** `391171501`
- **Submission:** [View accepted submission](https://codeforces.com/contest/580/submission/391171501)

## Example

### Input

```text
4 3 2
1 2 3 4
2 1 5
3 4 2
```

### Output

```text
12
```

One optimal order is dish 2 → dish 1 → dish 4:

```text
2 + 1 + 5 + 4 = 12
```

## Running Locally

Python 3.8 or later is required because the solution uses `int.bit_count()`.

```bash
python kefa_and_dishes.py
```

Enter input using the format specified in the original problem.

## Tests

The repository includes regression tests covering:

- The official sample.
- Selecting only one dish.
- Order-dependent transition bonuses.

Run them with:

```bash
python -m unittest discover -s tests -v
```

## Project Structure

```text
Bitmask-DP-Optimisation-Codeforces-580D/
├── tests/
│   └── test_solution.py
├── .gitignore
├── LICENSE
├── README.md
└── kefa_and_dishes.py
```

## Key Learning Outcomes

- Representing subsets with binary masks.
- Designing multi-dimensional DP states.
- Handling order-dependent rewards.
- Optimising state transitions with bit operations.
- Analysing exponential dynamic-programming complexity.
- Testing algorithmic solutions with automated regression cases.

## License

This project is available under the [MIT License](LICENSE).

## Author

**Shawon Khan**

- GitHub: [@shawonsmith](https://github.com/shawonsmith)
