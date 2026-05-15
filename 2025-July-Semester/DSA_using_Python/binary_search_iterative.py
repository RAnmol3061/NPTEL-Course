def itbinary_search(seq,v,l,r):
    while (l <= r):
        mid = (l+r)//2

        if v == seq[mid]:
            return(f"Position of element is {mid}")
        
        if v > seq[mid]:
            l = mid+1
        else:
            r = mid-1
    
    return("Element not found")    


test = [1,3,5,100,543,10000,10323432,32415134234]
print(itbinary_search(test,543,0,len(test)-1))
print(itbinary_search(test, 123,0,len(test)-1))