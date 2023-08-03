class Solution:
    def compress(self, chars) -> int:
        d=[]
        c=1
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                c+=1
            else:
                d.append([chars[i-1],c])
                c=1
        d.append([chars[-1],c]) 
        i=0
        for k,v in d:
            chars[i]=k
            i+=1
            if v>1:
                for item in str(v):
                    chars[i]=str(item)
                    i+=1
        return i


a = ["a","a","b","b","c","c","c"]
print(Solution().compress(a))




# print(2>float("inf"))


# s = " hello    world "

# new_s = s.split(' ')
# new_s = new_s[::-1]

# for i in new_s:
#     if i:
#         print(i,end=" ")
#     else:
#         pass