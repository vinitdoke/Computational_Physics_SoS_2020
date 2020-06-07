import numpy as np
def Solve(A,v):
    N=len(v)
    for i in range(N):
        div=A[i][i]
        k=i
        while div==0:
            k+=1
            div=A[k+1][k]
        A[[i,k]]=A[[k,i]] 
        v[[i,k]]=v[[k,i]]



        div=A[i][i]    
        A[i]/=div
        v[i]/=div
        for j in range(i+1,N):
            mult=A[j][i]
            A[j]-=mult*A[i]
            v[j]-=mult*v[i]
            
    soln=np.empty(N,float)
    for m in range(N-1,-1,-1):
        soln[m]=v[m]
        for i in range(m+1,N):
            soln[m]-=A[m,i]*soln[i]

    return soln
    
  
        