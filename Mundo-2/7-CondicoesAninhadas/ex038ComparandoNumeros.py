n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1>n2:
    print('O \033[1;31mPRIMEIRO\033[m valor é \033[1;32mMAIOR\033[m do que o \033[1;31mSEGUNDO\033[m.')
elif n2>n1:
    print('O \033[1;31mSEGUNDO\033[m valor é \033[1;32mMAIOR\033[m do que o \033[1;31mPRIMEIRO\033[m')
else:
    print('Os dois valores são \033[1;32mIGUAIS\033[m!')
