abc  =  input('Enter a string:')

new1  = ' '
new2  = ' '

i = 0

while i < len(abc):
    if abc[i] != ' ':
        new1 = new1 + abc[i]
        i = i + 1
    else:
        break


while i < len(abc):
    if abc[i] == ' ':
       i = i + 1
       continue
    else:
       new2 = new2+abc[i]
       i = i + 1

result = new1 + new2

result = result.lstrip()
print(result)
        
