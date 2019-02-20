
#import class library and sqlite3 module
import sqlite3
import PooleCLib


def processing():
#handles all of the processing
    check_numbers = list()
    repeated_checks = list()

    #connects to database
    conn = sqlite3.connect('BankStatements2.db')
    
    #selects all the customers
    my_cust = conn.cursor()
    my_cust.execute ('select * from customers order by acctnum asc')

    my_trans = conn.cursor()

    update_cursor = conn.cursor()

    #for each customer go through every transaction with the same acct number and update the customer balance.
    #   If the check number has been used before it adds that transaction to a repeated checks list.
    for custRec in my_cust:
        #making customer object
        customer = PooleCLib.Customers(custRec)
        custID = customer.acctNum
        my_trans.execute('select * from Transactions where acctNum = ?', (custID,))       

        if my_trans.fetchone() is None:
            pass
        else:
            for transRec in my_trans:
                #making transaction object
                transaction = PooleCLib.Transactions(transRec)

                if transaction.transItem == 'DEP':
                    customer.balance += customer.balance + transaction.transAmt
                else:

                    if transaction.transItem in check_numbers:
                        repeated_checks.append(transaction)
                    else:
                        check_numbers.append(transaction.transItem)
                        customer.balance -= transaction.transAmt

        #updates database with new balances
        update_cursor.execute('''update customers
                                 set balance = ?
                                 where acctNum = ?''',
                                 (round(customer.balance, 2), customer.acctNum,))

    #commits changes to database
    conn.commit()

    #closes connections       
    my_cust.close()
    my_trans.close()
    update_cursor.close()




def main():
    processing()



if __name__ == '__main__':
    main()
