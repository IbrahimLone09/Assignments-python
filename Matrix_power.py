def matrixpower(A,n):
    #B = A
    B =[i[:] for i in A]
    #C = A
    C = [i[:] for i in  A]
    for i in range(n - 1):
        C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
        
        #B = C
        B = [i[:] for i in C]
    return C


A = [[1,1],[1,0]] 
matrixpower(A,2)
for n in range(10):
    result = matrixpower(A, n)
    print(result)

for n in range(10):
    result = matrixpower(A,n)
    print(n,result[0][0])