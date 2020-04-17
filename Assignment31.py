#PF-Assgn-31
def check_palindrome(word):
    #pass
    #Remove pass and write your logic here
    rev=word[::-1]
    if(rev == word):
        return True
    else:
        return False
status=check_palindrome("madam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
