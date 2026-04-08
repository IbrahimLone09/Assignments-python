A = [[1,1], [1,0]]
temp = A
output = [[0,0],[0,0]]
output[0][0] = temp[0][0] * A[0][0] + temp[0][1] * A[1][0]
output[0][1] = temp[0][0] * A[0][1] + temp[0][1] * A[1][1]
output[1][0] = temp[1][0] * A[0][0] + temp[1][1] * A[1][0]
output[1][1] = temp[1][0] * A[0][1] + temp[1][1] * A[1][1]

print(output)
