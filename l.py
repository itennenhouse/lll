
import numpy as np
import copy
#Credit to JJGO on github who posted implementation (which I modified slightly) of gs at https://gist.github.com/iizukak/1287876/edad3c337844fac34f7e56ec09f9cb27d4907cc7
def gs(B):
    basis = []
    for v in B:
        w = v - np.sum(np.dot(v,b)*b/(np.dot(b,b)) for b in basis)
        basis.append(w)
    return np.array(basis)
def proj(u,v):
    p = ((np.dot(u,v))/(np.dot(v,v)))
    return p*v
    #make sure the scalar mult isn't being wack
def proj_co_round(u, v):
    p = ((np.dot(u,v))/(np.dot(v,v)))
    return round(p)
def mag_squared(v):
    return np.dot(v,v)
def LLL(B, delta, n):
    #note B needs to be a numpy matrix in order for scalar mult to work
    done=False
    while(not done):
        Q=gs(B)
        for i in range(1,n):
            for j in range(i-1, -1, -1):
                B[i]=B[i]-proj_co_round(B[i],Q[j])*B[j]
        for i in range(0,n-1):
            left = delta*mag_squared(Q[i])
            right = mag_squared(proj(B[i+1],Q[i])+Q[i+1])
            if(left>right):
                temp=copy.copy(B[i])
                B[i]=B[i+1]
                B[i+1]=temp
                break
            if(i==n-2):
                done=True
    return B
def proj_coeff(u,v):
    return ((np.dot(u,v))/(np.dot(v,v)))
def tester(B, delta, n):
    Q=gs(B)
    for i in range(0,n):
        for j in range(0,i):
            if(abs(proj_coeff(B[i],Q[j]))>.5):
                return False
    for i in range(0,n-1):
            left = delta*mag_squared(Q[i])
            right = mag_squared(proj(B[i+1],Q[i])+Q[i+1])
            if(left>right):
                return False
    return True
test = np.array([[1,2,3],[3,2,4],[5,2,-1]])
ans = LLL(test, .75, 3)
print(ans)
print(tester(ans, .75, 3))

