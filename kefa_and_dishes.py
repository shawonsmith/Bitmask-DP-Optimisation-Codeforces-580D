import sys

input = sys.stdin.buffer.readline

n, m, k = map(int, input().split())
satisfaction = list(map(int, input().split()))

bonus = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y, c = map(int, input().split())
    bonus[x - 1][y - 1] = c

total_masks = 1 << n
full_mask = total_masks - 1

dp = [[-1] * n for _ in range(total_masks)]

bit_index = [0] * total_masks

for dish in range(n):
    bit = 1 << dish
    bit_index[bit] = dish
    dp[bit][dish] = satisfaction[dish]

answer = 0

for mask in range(1, total_masks):
    eaten = mask.bit_count()

    if eaten > m:
        continue

    row = dp[mask]

    if eaten == m:
        best = max(row)

        if best > answer:
            answer = best

        continue

    last_bits = mask
    available = full_mask ^ mask

    while last_bits:
        last_bit = last_bits & -last_bits
        last = bit_index[last_bit]
        current_score = row[last]

        if current_score != -1:
            next_bits = available

            while next_bits:
                next_bit = next_bits & -next_bits
                next_dish = bit_index[next_bit]
                new_mask = mask | next_bit

                new_score = (
                    current_score
                    + satisfaction[next_dish]
                    + bonus[last][next_dish]
                )

                if new_score > dp[new_mask][next_dish]:
                    dp[new_mask][next_dish] = new_score

                next_bits -= next_bit

        last_bits -= last_bit

print(answer)