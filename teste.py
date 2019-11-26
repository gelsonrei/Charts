from time import time

lista = range(100000)
t = time()
c1 = ''
for i in lista:
    c1 = '%s,%s' % (c1, i)
c1 = c1[1:]
print ('Teste concatenação 01: %.3f segundos' % (time()-t))
#print (c1)

t = time()
c3 = ','.join([str(i) for i in lista])
print ('Teste concatenação 03: %.3f segundos' % (time()-t))