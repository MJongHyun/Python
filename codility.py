A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

int solution(int X, int Y, int D);

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.


def solution(X,Y,D):
    S=X
    cn=0
    if S>=Y:
        return 0
    while 1:
        S=S+D
        if S>=Y:
            cn=cn+1
            break
        else:
            cn=cn+1
    return cn

def solution(X,Y,D):
    S=X
    cn=0
    if S>=Y:
        return 0
    elif (Y-X)%D==0:
        return (Y-X)//D
    else:
        return (Y-X)//D+1


solution(10,85,30)

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7 
P = 2, difference = |4 − 9| = 5 
P = 3, difference = |6 − 7| = 1 
P = 4, difference = |10 − 3| = 7 
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

def solution(A):
    if str(A).isnumeric():
        return A
    if len(A)==2:
        return abs(A[0]-A[1])
    D=[]
    for i in range(0,len(A)):
        if i==len(A)-1:
            break
        B=A[0:i+1]
        C=A[i+1:]
        a=sum(B)
        b=sum(C)
        if abs(a-b)==0:
            return abs(a-b)
        else:
            D.append(abs(a-b))
    return min(D)

def solution(A):
    if len(A)==2:
        return abs(A[0]-A[1])    
    B=[abs(sum(A[0:i+1])-sum(A[i+1:])) for i in range(0,len(A))]
    del B[-1]
    return min(B)


z=[i for i in range(1,101) if i%2==0] # if문도 추가가 가능하다.

A=[-10,-20,-30,-40,100]
solution(A)

A=[3,1,2,4,3]
solution(A)



A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].

def solution(A):
    
     if len(set(A)) != len(A):
         return 0
     elif max(A) != len(A):
         return 0

     else:
         return 1

A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

def solution(X, A): #54%
    B=[]
    D=[i for i in range(1,X+1)]
    
    for i in range(0,len(A)):
        B.append(A[i])
        C=list(set(B))
        if C==D:
            return i
    return -1

def solution(X, A):
    B={}
    count=0
    for i in A:
        if i not in B:
            B[i]=1
        if len(B.keys())==X:
            return count
        count=count+1
    return -1

        
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Copyright 2009–2018 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

def solution(N, A): # pandas는 왜 안되는가
    from pandas import Series,DataFrame
    B={}
    for i in range(0,N):
        B[i+1]=0
    C=Series(B)

    for i in A:
        if i==len(B)+1:
            C[:]=max(C)
        else:
            C[i]=C[i]+1

    return list(C)

N=5
A=[3,4,4,6,1,4,4]        
solution(N,A)



def solution(N, A): # 44%
    B={}
    for i in range(0,N):
        B[i+1]=0
    for i in A:
        if i==len(B)+1:
            for j in B.keys():
                B[j]=max(B.values())
        else:
            B[i]+=1

    return list(B.values())   

def solution(N, A):
    B=[]
    for i in range(0,N):
        B.append(0)
    for i in A:
        if i==len(B)+1:
            B=[max(B) for i in range(0,N)]
        else:
            B[i-1]=B[i-1]+1
    return B
    
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].


A = [-1,-3]
A = [1, 2, 3]
A = [1,3,6,4,1,2]

A=[i for i in range(1,100000)]
A=[-1,-3254353,1393,1]
solution(A)
B=set(A)
A=[1,56,90,123]
B=list(set(A))
B.sort(reverse=True)

def solution(A): # 55%
    
    if 1 not in A:
        return 1
    B=list(set(A))

    if max(B)==len(B):
        return (max(B)+1)
    else:
        for i in range(0,len(B)):
            if i==len(B)-1 or i<0:
                break
            elif B[i]==B[i+1]+1:
                continue
            else:
                return (B[i]+1)
        
def solution(A): #66%
    
    if 1 not in A:
        return 1
    B=list(set(A))
    B.sort(reverse=True)
    cn=1
    C=[]
    
    for i in range(0,len(B)):
        if i==len(B)-1 or B[i]<0:
            break
        elif B[i]==B[i+1]+1:
            cn+=1
            continue
        else:
            C.append(B[i+1]+1)            
    if B[0]==cn:
        return cn+1
    else:
        return min(C)
    

def solution(A): #66%
    
    if 1 not in A:
        return 1
    B=list(set(A))
    B.sort(reverse=True)
    cn=1
    
    for i in range(0,len(B)):
        if i==len(B)-1 or B[i]<0:
            break
        elif B[i]==B[i+1]+1:
            cn+=1
            continue
        else:
            return B[i+1]+1            
    if B[0]==cn:
        return cn+1

A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.     

A=[0,1,0,1,1]
def solution(A): # 60%
    B=[]
    C=[]

    for i in range(0,len(A)):
        if A[i]==0:
            B.append(i)
        else:
            C.append(i)

    cn=0
    for i in range(0,len(B)):
        for j in range (0,len(C)):
            if B[i]<C[j]:
                cn+=1
    return cn
        
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.

a={'A':1,'C':2,'G':3,'T':4}

S='CAGCCTA'

P=[2,5,0]
Q=[4,5,6]


def solution(S, P, Q): # 50 %
    B=[]
    for i in range(0,len(P)):
        A=S[P[i]:Q[i]]
        if A=='':
            if S[P[i]]=='A':
                B.append(1)
            elif S[P[i]]=='C':
                B.append(2)
            elif S[P[i]]=='G':
                B.append(3)
            elif S[P[i]]=='T':
                B.append(4)
        elif 'A' in A:
            B.append(1)
            continue
        elif 'C' in A:
            B.append(2)
            continue
        elif 'G' in A:
            B.append(3)
            continue
        elif 'T' in A:    
            B.append(4)
            continue
    
    return B

def solution(S, P, Q): # 100%
    B=[]
    for i in range(0,len(P)):
        A=S[P[i]:Q[i]+1]
   
        if 'A' in A:
            B.append(1)
            continue
        elif 'C' in A:
            B.append(2)
            continue
        elif 'G' in A:
            B.append(3)
            continue
        elif 'T' in A:    
            B.append(4)
            continue
    
    return B

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].

A=[4,2,2,5,1,5,8]

def solution(A):
    D={}
    m=99999999
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            B=A[i:j+1]
            C=sum(B)/len(B)
            if C<m:
                m=C
                D[i]=m
        
    for i,j in D.items():
        if j==min(D.values()):
            return i 

solution(A)

Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

def solution(A, B, K):
    cn=0
    if K==1:
        return B-A+1
    for i in range(A,B+1):
       if i%K==0:
           cn=cn+1
    return cn

Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    return len(set(A))
    
A=[2,1,1,2,3,1]
solution(A)

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].




