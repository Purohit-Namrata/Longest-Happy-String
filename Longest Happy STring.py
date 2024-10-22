class Solution:
    def longesDiverseString(self,a:int,b:int,c:int)->str:
        cur_a = cur_b = cur_c = 0
        total_chars= a+b+c
        result=[]
        for i in range(total_chars):
            if (a>=b and a>=c and cur_a!=2) or (a>0 and (cur_b ==2 or cur_c==2)):
                result.append("a")

                a-=1
                cur_a+=1
                cur_b=0
                cur_c=0
            
            if (b>=a and b>=c and cur_b!=2) or (b>0 and (cur_c ==2 or cur_a==2)):
                result.append("b")
                b-=1
                cur_b+=1
                cur_a=0
                cur_c=0

            if (c>=a and c>=b and cur_c!=2) or (c>0 and (cur_a ==2 or cur_b ==2)):
                result.append("c")
                c-=1
                cur_c+=1
                cur_a=0
                cur_b=0

        return "".join(result)
s=Solution()
print(s.longesDiverseString(a=1,b=1,c=7))
            
