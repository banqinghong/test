try:
    f = open('e:/2.txt','w')
    for i in range(1,5):
        num = str(i)
        writeString = 'line ' + num + '\n'
        f.write(writeString)
        i += 1
    j = 1
finally:
    f.close()
try:
    f = open('e:/2.txt', 'r')
    while True:
        line = f.readline()
        if not line:break
        print "%d:  %s" % (j,line)
        j += 1
finally:
    f.close()
