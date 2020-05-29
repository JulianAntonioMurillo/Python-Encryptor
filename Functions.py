#Julian Murillo
#002301366
#jmurillo@chapman.edu
#230-06
#PA7-Encryption/Decryption

#Function One: encryption
def encrypt(unencrypted_file,map_file):
    #first need to read "map_file"
    #Then create a dict of the mappings in that file
            #Third Function
    to_map=mapping(map_file)
    
    p=open(unencrypted_file,"r")

    #Empty string to create encryption
    string=""
    for line in p:
        for lett in line:
            # verify string is in alphabet
            if not lett.isalpha():
                string+=lett
            # If it is a letter, then find it in the mapping/encrypter and encrypt it

            else:
                for k,v in to_map.items():
                    if lett==k:
                        string+=v
                        break
    #now write in file
    w_file=open("encrypted.txt","w")

    #write the encrypted lines to the file
    w_file.write(string)
    w_file.close()

#Function Two: decryption
def decrypt(file,sub_file):
    #read file that contains encrypted lines
    #create dictionary of mappings like in first function
    to_map=mapping(sub_file)

    f=open(file,"r")
    #create empty string like in previous func
    string=""
    for line in f:
        for lett in line:
            if not lett.isalpha():
                string+=lett
            else:
                for k,v in to_map.items():
                    if lett==v:
                        string+=k
                        break
                        
    w_file=open("unencrypted.txt","w")
    w_file.write(string)
    w_file.close()
    
#third function for calling into previous functions
def mapping(map_param):
    #open the mapping file to read
    act_code=open(map_param,"r")
    to_map=act_code.readlines()
    act_code.close()
    m={}
    #for loop for encryption/to replace x with y
    for elem in to_map:
        m[elem[0]]=elem[2]
    return m
#call n watch the magic happen
encrypt("hp.txt","mapping.txt")
decrypt("encrypted.txt","mapping.txt")


