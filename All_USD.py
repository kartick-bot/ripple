fp = open("C:\\Users\\kartick kolachala\\Desktop\\experiments\\Transactions1.txt", 'rt').read().splitlines()
fUSD = open("C:\\Users\\kartick kolachala\\Desktop\\experiments\\outUSD2.txt", 'w')

paymentList = []
i=0
for i, line in enumerate(fp):
    paymentList=line.split(" ")
    
    if paymentList[40] == 'USD':
    	
    	fUSD.write(line)
    	fUSD.write("\n")
fUSD.close()