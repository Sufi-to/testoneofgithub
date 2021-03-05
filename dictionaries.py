fname = input("Enter file name: ")
fh= open(fname)
counts= dict()
for line in fh:
    line=line.rstrip()
    if line.startswith('From '):
       words=line.split()
       counts[words[1]]=counts.get(words[1],0)+1
bigcount=0
for word,count in counts.items():
   if bigcount == 0 or count>bigcount:
       bigword=word
       bigcount=count

print(bigword,bigcount)








    ##for word in words:
        #if len(words)< 3 or words[0]!= "From":
            #continue


##print(counts)
##largeword= None
##    if largecount is None or count > largecount:
    #    largeword= word
    #    largecount= count
#print(largeword, largecount)
