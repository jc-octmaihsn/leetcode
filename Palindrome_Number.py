def isPalindrome(x):
    a=""
    x=str(x)
    for i in range(len(x),0,-1):
        a+=x[i-1]
    if a==x:
        return True
    else:
        return False

i = int(input())
print(palindrome(i))
