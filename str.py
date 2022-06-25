from turtle import st


x="childrenplaying"
word=len(x)//2
word2=(x[0:word]).upper()+(x[word:]).lower()
print(word2)

x="Tomorrow"
y=""
for i in x:
    if i  not in y:
        y+=i
print(y)

# statement="Just give up on me"
# t=statement.split()
# start=0
# end=len(statement)-1
# print(statement[0])
# t[start],t[end]=t[end],t[start]
# while start < end:  
#  start+=1
#  end-=1
#  statementt=" "
# print(str.join(statementt))


def findPalindrome(r):
    return r == r[::-1]
r = "rotator"
ans = findPalindrome(r)
 
if ans:
    print("It is  a palindrome")
else:
    print("it is not a palindrome")

def reverse_word(y, start, end):
    while start < end:
        y[start], y[end] = y[end], y[start]
        start = start + 1
        end -= 1
  
y = "Keep moving "
y = list(y)
start = 0
while True:
     end = y.index(' ', start)
     reverse_word(y, start, end - 1)
     start = end + 1
     y = "".join(y)
     print(y)
      
   