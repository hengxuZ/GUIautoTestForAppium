import hashlib

#待加密信息
str = '12345678qa'
# 创建md5对象
hl = hashlib.md5()
# Tips
# 此处必须声明encode
# 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))
#print('MD5加密前为 :' + str)
#print('MD5加密后为 :' + hl.hexdigest())
def hashencryption(password):
    hl = hashlib.md5()
    hl.update(password.encode(encoding='utf-8'))
    return hl.hexdigest()
def hashen(*args):
    if len(args)==1:
        h= hashlib.md5()
        h.update("".join(args).encode(encoding='utf-8'))
        return h.hexdigest()
    else:
        sum=''
        for i in args:
            h = hashlib.md5()
            h.update(i.encode(encoding='utf-8'))
            sum+=h.hexdigest()
        hashen(sum)
    return hashen(sum)
a=hashen('12345678qa','2020020318240652709000036')
print(a)














