def gauss_elimination(A, b):
  n = len(A) 
  for i in range(n):
    pivot = abs(A[i][i])
    pivot_row = i
    for j in range(i+1, n):
      if abs(A[j][i]) > pivot:
        pivot = abs(A[j][i])
        pivot_row = j
    if pivot_row != i:
      A[i], A[pivot_row] = A[pivot_row], A[i]
      b[i], b[pivot_row] = b[pivot_row], b[i]
    for j in range(i+1, n):
      factor = A[j][i] / A[i][i]
      for k in range(i, n):
        A[j][k] -= factor * A[i][k]
      b[j] -= factor * b[i]
  # Back-substitute to find the solution
  x = [0,0,0]
  for i in range(n-1, -1, -1):
    x[i]=b[i]
    for j in range(i+1, n):
      x[i]= x[i]-A[i][j]*x[j]
    x[i] = x[i]/A[i][i]
  return x
A = [[1,-2,1], [0,2,-8], [-4,5,9]]
b = [0,8,-9]
x = gauss_elimination(A, b)
print(x)