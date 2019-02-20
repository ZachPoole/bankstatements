
class Customers():

    ''' Class that creates object and attributes for customers '''
    
    def __init__(self, cust_record):
        self.acctNum = cust_record[0]
        self.lastName = cust_record[1]
        self.firstName = cust_record[2]
        self.streetOne = cust_record[3]
        self.streetTwo = cust_record[4]
        self.city = cust_record[5]
        self.state = cust_record[6]
        self.postalCode = cust_record[7]
        self.balance = int(cust_record[8])


    def __repr__(self):
        return repr([self.acctNum, self.lastName, self.firstName, self.streetOne, self.streetTwo, self.city, self.state, self.postalCode, self.balance])





class Transactions():

    ''' Class that creates object and attributes for transactions '''

    def __init__(self, trans):
        self.acctNum = trans[0]
        self.transDate = trans[1]
        self.transAmt = trans[2]
        self.transItem = trans[3]

    def __repr__(self):
        return repr([self.acctNum, self.transDate, self.transAmt, self.transItem])
        
        
