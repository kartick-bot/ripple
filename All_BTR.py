fp = open("C:\\Users\\kartick kolachala\\Desktop\\kartick\\data\\trans1\\transaction201906\\Transactions1.txt", 'rt').read().splitlines()
fBTR = open("C:\\Users\\kartick kolachala\\Desktop\\experiments\\outBTR.txt", 'w')

paymentList = []
for i, line in enumerate(fp):
    paymentList=line.split(" ")
    
    if paymentList[40] == 'BTR':
    	fBTR.write(paymentList[0]+"\t"+paymentList[7]+"\t"+paymentList[33])
    	fBTR.write("\n")
fBTR.close()