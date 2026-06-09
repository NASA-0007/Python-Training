class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        l2=[]
        result=True
        for i in bills:
            if i not in [5,10,20]:
                return False
            elif i==5:
                l2.append(i)
                result=True
            elif i>5:
                if 5 not in l2:
                    result =  False 
                else:
                    for i in range(i//5-1):
                        l2.remove(5)
        return result