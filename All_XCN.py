fp = open("C:\\Users\\kartick kolachala\\Desktop\\kartick\\data\\trans1\\transaction201906\\Transactions1.txt", 'rt').read().splitlines()
fXCN = open("C:\\Users\\kartick kolachala\\Desktop\\experiments\\outXCN.txt", 'w')

paymentList = []
for i, line in enumerate(fp):
    paymentList=line.split(" ")
    
    if paymentList[40] == 'XCN':
    	fXCN.write(paymentList[0]+"\t"+paymentList[7]+"\t"+paymentList[33])
    	fXCN.write("\n")
fXCN.close()