fp = open("C:\\Users\\kartick kolachala\\Desktop\\kartick\\data\\trans1\\transaction201906\\Transactions1.txt", 'rt').read().splitlines()
fETH = open("C:\\Users\\kartick kolachala\\Desktop\\experiments\\outETH.txt", 'w')

paymentList = []
for i, line in enumerate(fp):
    paymentList=line.split(" ")
    
    if paymentList[40] == 'ETH':
    	fETH.write(paymentList[0]+"\t"+paymentList[7]+"\t"+paymentList[33])
    	fETH.write("\n")
fETH.close()