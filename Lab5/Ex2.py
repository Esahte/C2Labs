def isPalindrome(lst):
    if len(lst) == 0:
        return True
    elif lst[0] != lst[-1]:
        return False
    return isPalindrome(lst[1:-1])


def main():
    wrd = input('Enter a word: ')
    if isPalindrome(wrd):
        print('is Palindrome')
    else:
        print('is not Palindrome')


main()
