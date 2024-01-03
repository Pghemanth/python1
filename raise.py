class HemanthInterrupt(Exception):
    pass

try:
    a=input('enter the string:')
    if a[0] in 'aeiouAEIOU':
        raise HemanthInterrupt('first char should not be a vowel')

except HemanthInterrupt:
    print('error handled')