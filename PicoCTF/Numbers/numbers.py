ninp = input("Input numbers: ")
nlist = ninp.split(' ')
temp = ''
con = ''
for i in nlist:
    temp = chr(int(i)+96)
    if temp == 'f':
        con += 'f'
        con += '{'
        continue
    con += temp
    temp = ''
con += '}'
print(con)
    