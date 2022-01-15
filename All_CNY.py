fp = open("C:\\Users\\kartick kolachala\\Desktop\\kartick\\data\\trans1\\transaction201906\\Transactions1.txt", 'rt').read().splitlines()
fCNY = open("C:\\Users\\kartick kolachala\\Desktop\\experiments\\outCNY2.txt", 'w')

paymentList = []
for i, line in enumerate(fp):
    paymentList=line.split(" ")
    
    if paymentList[40] == 'CNY':
    	fCNY.write(line)
    	fCNY.write("\n")
fCNY.close()