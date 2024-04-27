# remove punctuations

punc = ''' -_[]{};:''",.<>/?,+=()!@#$%^&*'''
s1 = '[my_pythone@gmail.com]'
s2 = ''
for x in s1:
    if x not in punc:
        s2 += x
print(s2)
