class Solution:
    def isValid(self, s: str) -> bool:
        index = 0
        x =  len(s)
        while index <= x:
            s = s.replace("[]","")  
            s = s.replace("()","")  
            s = s.replace("{}","")
            if s== "":
                return True
            elif index == x and s!= "":
                return False
            else:
                pass
                index+=1
                