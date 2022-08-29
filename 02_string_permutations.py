# Python program to print all permutations of a given string of length 3 
  
def toString(List): 
    return ''.join(List) 

# backtrack
def permute(a, l, r): 
    if l==r: 
        print (toString(a))
    else: 
        for i in range(l,r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] 
  
string = "abc"
permute(list(string), 0, len(string))