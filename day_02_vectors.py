A = [4, 150, 1]
B = [2, 80, 1]

sum_ab = [A[i] + B[i] for i in range(len(A))]
print(f"A + B = {sum_ab}")

scaled = [2 * x for x in A]
print(f"2 * A = {scaled}")

dot = sum(A[i] * B[i] for i in range(len(A)))
print(f"A . B = {dot}")