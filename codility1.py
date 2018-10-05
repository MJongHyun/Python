def solution(N):
    b=N
    li=[]
    while N!=0:
        B=N//2
        N=B
        A=N%2
        if A==0:
            li.append(0)
        else:
            li.append(1)
    del li[-1]
    li.reverse()
    if b%2==1:
        li.append(1)
    else:
        li.append(0)
    cn=[]
    dn=0
    for i in range(1,len(li)):
        if li[i]==0:
            dn=dn+1
        else:
            cn.append(dn)
            dn=0
    if cn==[]:
        return 0 
    else:
        return max(cn)

def solution(A,K):
    try:
        for i in range(0,K):
            A.insert(0,A[-1])
            del A[-1]
        return A
    except:        
        if A==[]:
            return []
        elif int(A):
            return [A]
        
A=[2,3,4]
A=1
solution(A,2)
   
A=[3,8,9,7,6]
K=1
solution(A,K)

A.insert(0,A[-1])
del A[-1]

def solution(A):
    B=set()
    for i in A:
        if A.count(i)%2==1:
            B.add(i)
    C=list(B)
    return C[0]

def solution(A):
    B=list(set(A))
    for i in B:
        if A.count(i)%2==1: # 카운드 자체가 for문을 계속일으켜서 느릴 수있다.
            return i
        
def solution(A):
    C={}
    for i in A:
        if i not in C:
            C[i]=1
        else:
            C[i]=C[i]+1
    
    for i,j in C.items():
        if j%2==1:
            return i
        


solution(A)
A=[3,3,9,9,9,9,7]
B=set()
for i in A:
    if A.count(i)%2==1:
        B.add(i)
C=list(B)       


def solution(A):
    B=[]
    for i in range(1,max(A)+1):
        B.append(i)
    C=[]
    for i in B:
        if i not in A:
            return i
            break
 

def solution(A):

    if A==[]:
        return 1
    elif str(A).isnumeric():
        return A+1
    else:
        A.sort()
        for i in range(0,len(A)):
            if i==len(A)-1:
                break
            elif A[i]+1!=A[i+1]:
                return A[i]+1
                break
    if len(A)==max(A):
        return max(A)+1
    elif A[0]==2:
        return 1

def solution(x):
    x=x.replace('?','.')
    x=x.replace('!','.')
    x=x.split('.')
    D=[]
    for i in x:
        y=i.split(' ')
        cn=0
        for j in y:
            if j.isalpha():
                cn=cn+1
        D.append(cn)
    return max(D)
    
def solution(x):
    start=0
    cn=0
    for i in range(0,len(x)):
        start=x[start]
        if start == -1:
            cn=cn+1
            break;
        else:
            cn=cn+1
    return cn  
