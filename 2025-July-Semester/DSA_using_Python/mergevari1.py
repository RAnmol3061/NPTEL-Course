# Assumptions: i) Both lists (A & B) are already sorted, ii) Both list (A & B) do not contain any duplicate element
# Only if the above assumption is met, it will perform union correctly

def merge_union(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)

    while i+j < m+n:
        if i == m:
            C.append(B[j])
            j = j+1
        elif j == n:
            C.append(A[i])
            i = i+1
        elif A[i] < B[j]:
            C.append((A[i]))
            i=i+1
        elif A[i] > B[j]:
            C.append(B[j])
            j=j+1
        elif A[i] == B[j]: 
            C.append(A[i])
            i=i+1
            j=j+1

    return(C)


a = [1,2,2,5]
b = [2,3,4,5,6]
print(merge_union(a,b))
