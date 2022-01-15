fp = open("C:\\Users\\kartick kolachala\\Desktop\\kartick\\data\\trans1\\transaction201906\\Transactions1.txt", 'rt').read().splitlines()
fUST = open("C:\\Users\\kartick kolachala\\Desktop\\experiments\\outUST.txt", 'w')

paymentList = []
for i, line in enumerate(fp):
    paymentList=line.split(" ")
    
    if paymentList[40] == 'UST':
    	fUST.write(paymentList[0]+"\t"+paymentList[7]+"\t"+paymentList[33])
    	fUST.write("\n")
fUST.close()