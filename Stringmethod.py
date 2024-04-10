s = 'hello, how are you'
print(s.find('o'))
print(s.find("o", 5))
print(s.rfind('o', 0, 15))

print(s.center(26, '*'))
print(s.ljust(26, '*'))
print(s.rjust(26, '*'))

s2 = '.... ....+++hello++...'
print(s2.lstrip('.'))  # remove '.' until space
print(s2.lstrip('. '))  # remove space also
print(s2.lstrip('. +'))  # '.' ' ' '+' all character remove
print(s2.rstrip('..+'))
s3="     hi my name is kishan      "
print(s3.strip())         #remove both side spaces;
