class Solution(object):
    def reverse(self, x):
            x=str(x)
            if x[0]=="-":
                x=x[:0:-1]
                x=int(x)*-1
                if x>-2147483648:
                    return(x)
                else:
                    return(0)
            else:
                x=x[::-1]
                x=int(x)
                if x<2147483647:
                    return(x)
                else:
                    return(0)
print(Solution().reverse(-123))