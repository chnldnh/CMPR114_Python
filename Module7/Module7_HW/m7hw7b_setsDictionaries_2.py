
    #m7homework7b-SetsDictionaries_2
# Pickled Vegetables
import pickle 

def pickled_vege():
    pickvege = {'tomato' : '5.00', 'squash' : '2.34'}
    print(pickvege)

    c = pickvege['tomato'] # print value
    print(c)

    pickvege['lemon'] = '.25' # add 
    print(pickvege)

    del pickvege['tomato'] # delete
    print(pickvege)

    pickvege.pop('squash') # remove
    print(pickvege)

    k = pickvege.keys()
    print(k)
    
    f = open('C://pickled.txt', 'wb') # open file for binary writing     
    pickle.dump(pickvege, f) # write data to new file 
    f.close() # close the file
   
    d = open('C://pickled.txt', 'rb') # open file to read
    read_data = pickle.load(d) # unpickle
    print(read_data)

pickled_vege()
