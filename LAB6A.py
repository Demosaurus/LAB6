#HASHLIB IMPORTED FOR HASHING FUNCTIONS
import hashlib

#STRING USER
String = 'ecsc'
Hash = 'c89aa2ffb9edcc6604005196b5f0e0e4'

#MD5 HASH OBJECT/PASSING TO MD5
Hash = hashlib.md5(String.encode()).hexdigest()

#IF HASHSTRING IS NOT EQUAL OR THE SAME AS THE HASH PROVIDED
while Hash != 'c89aa2ffb9edcc6604005196b5f0e0e4' :
  Hash = hashlib.md5(Hash.encode()).hexdigest()
#HASH PRINTED OUT IN HEX FORMAT
  print (Hash)
   

