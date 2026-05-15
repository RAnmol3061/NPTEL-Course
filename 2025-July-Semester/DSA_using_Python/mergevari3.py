# Assumptions: i) Both lists (A & B) are already sorted, ii) Both list (A & B) do not contain any duplicate element
# Only if the above assumption is met, it will perform list difference correctly



def merge_diff(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)

    while i+j < m+n:
        if i==m:
            break
        elif j==n:
            break
        elif A[i] < B[j]:
            C.append(A[i])
            i +=1
        elif A[i] > B[j]:
            j +=1
        elif A[i] == B[j]:
            i +=1
            j +=1
    return (C)

a = [1,2,5]
b = [2,3,4,5]

print(merge_diff(a,b))