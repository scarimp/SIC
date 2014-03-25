filein=open('anagrafica.csv','rU')
fileout=open('anagrafica_tab1.txt','w')
##count=0
for line in filein:
    repl=line.replace('|',';')
    fileout.write(repl)
##    count +=1
filein.close()
fileout.close()
##print("finito")
##print (count)

