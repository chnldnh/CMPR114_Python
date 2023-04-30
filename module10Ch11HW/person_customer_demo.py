
import client

def main():   
    try:
        na = input('What is the name? ')
        ad = input('What is the address? ')
        ph = input('What is the phone number? ')
        cn = input('What is the customer number? ')
        ml = input('Do you want to be on the mailing list? (Enter y for yes or n for no) ')

        while (ml != 'y') and (ml != 'n') and (ml != 'Y') and (ml != 'N'):                 
            ml = input('Do you want to be on the mailing list? (Enter y for yes or n for no) ')

        cust = client.Customer(na, ad, ph,cn, ml)

        print('The name is ', cust.get_name())
        print('The address is ', cust.get_address())
        print('The phone number is ', cust.get_phone())
        print('The customer number is ', cust.get_cusNum())
        print('The mailing list: ', cust.set_mailList(ml))         
    except Exception as err:
        print(err)

main()