def binary_search(seq,v,l,r): 
    
    if l > r:
        return(False)
    
    mid = (l+r)//2

    if v == seq[mid]:
        return(f"Position of element is {mid}")
    
    if v > seq[mid]:
        return(binary_search(seq,v,mid+1,r))
    else:
        return(binary_search(seq,v,l,mid-1))
    

test = [1,3,5,100,543,10000,10323432,32415134234]
print(binary_search(test,543,0,len(test)-1))
print(binary_search(test, 123,0,len(test)-1))

