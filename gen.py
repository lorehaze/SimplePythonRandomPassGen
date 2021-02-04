import string
import random 
import time

def len_randomizer(strl_en):
    random.seed(time.clock_gettime(0)) #randomize seed
    var0= ''.join(random.choices(string.ascii_uppercase +
                             string.digits+string.ascii_lowercase, k = strl_en)) 
    return var0

len0=random.randint(0,8)
len1=random.randint(0,5)    #randomize len salt1
len2=random.randint(0,5)    #randomize len salt2


salt1 =len_randomizer(len1) #gen salt1
 
salt2 = len_randomizer(len2) #gen salt2

psw = len_randomizer(len0)  #gen pass

psw_hash=hash(psw)  #extract hash

saltsum = salt1+str(psw_hash)+salt2   #Sum two salts and (cast) hash

#print(salt1,salt2) OK IT WORKS

print(saltsum)