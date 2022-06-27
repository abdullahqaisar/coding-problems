def test():
  (N, M) = tuple(map(int, input().split()))
  C = list(map(int, input().split()))
  sum = 0
  for Ci in C:
    sum += Ci
  modulo = sum % M
  print(modulo)

T = int(input())
for test_no in range(1, T + 1):
  print("Case #%d:" % test_no, end=" ")
  test()
