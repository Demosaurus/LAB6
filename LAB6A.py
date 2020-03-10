import hashlib  #HASHLIB IMPORT

hashstring = 'ecsc' #STRING
hash = 'c89aa2ffb9edcc6604005196b5f0e0e4' #HASH

def ASCIIHash(Test): #ASCII ENCODING
    ASCII = hashlib.md5(Test.encode('ascii')) #ECODING ecsc IN ASCII AND PASSING TO MD5
    result = ASCII.hexdigest()#STRING OF DOUBLE LENGTH / HEX VALUE
    return result #RETURN RESULT

if hashstring != 'c89aa2ffb9edcc6604005196b5f0e0e4' : #IF HASHSTRING IS NOT EQUAL OR THE SAME AS THE HASH PROVIDED
    #USE ecsc STRING
    hashstring = ASCIIHash(hashstring)
    print(hashstring) #PRINT HASH's
