import time
import base64
import hmac,struct,hashlib

import random


class GoogleCodeBuilder(object):
    def __init__(self):
        pass

    def get_code(self,secretKey = '6dh3 sjxe 3rp2 7xow iacr czgx uxsz knrw'):
        input = int(time.time()) // 30
        tmp_key = secretKey.upper().replace(" ", '') if secretKey.find(" ") != -1 else secretKey.upper()
        key = base64.b32decode(tmp_key)
        msg = struct.pack(">Q", input)
        googleCode = hmac.new(key, msg, hashlib.sha1).digest()
        o = googleCode[19] & 15
        googleCode = str((struct.unpack(">I", googleCode[o:o + 4])[0] & 0x7fffffff) % 1000000)
        if len(googleCode) == 5:  # 如果验证码的第一位是0，则不会显示。此处判断若是5位码，则在第一位补上0
            googleCode = '0' + googleCode
        return googleCode

if __name__ == "__main__":
    print(GoogleCodeBuilder().get_code("OMHKTIDVBGYPM5GG2QFMF6DQWZKHTO7O"))

