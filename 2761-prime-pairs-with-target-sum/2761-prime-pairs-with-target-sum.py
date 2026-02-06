class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        Prime=[True]*(n+1)
        for i in range(2,int(n**0.5)+1):
            if Prime[i]==True:
                for j in range(i*i,n+1,i):
                    Prime[j]=False
        result=[]
        for x in range(2,n//2+1):
            if Prime[x]and Prime[n-x]:
                result.append([x,n-x]) 
        return result   