import random 
lower = 'qwertyuiopasdfghjklçzxcvbnm'
upper = 'QWERTYUIOPÇLKJHGFDSAZXCVBNM'
digits = '1234567890'
symbols = '"!@#$%¨&*()_-+=[{`~^]}/?;:.>,<\|'

qnt = 16
qntInt = int(qnt)
length  = qntInt

all = lower + upper + digits + symbols 
passwordAll = "".join(random.sample(all,length))

print ('New Password = ' + passwordAll)


