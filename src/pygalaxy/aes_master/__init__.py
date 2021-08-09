#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import hashlib
import binascii

IV = "#fsi&3)f23&fsf%!"
ENCODING = "utf-8"
DEFAULT_KEY = "www.wiatec.com"


class AesMaster:

    @staticmethod
    def __pad(source):
        """
        填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充
        """
        text_length = len(source)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return source + pad * amount_to_pad

    @staticmethod
    def __bytes2hex(bs):
        """
        字节转16进制数字
        """
        return str(binascii.b2a_hex(bs).decode(ENCODING)).upper()

    @staticmethod
    def encrypt(source: str, key: str = DEFAULT_KEY):
        """
        加密
        """
        raw = AesMaster.__pad(source)
        key = str(hashlib.md5(str(key).encode(ENCODING)).hexdigest()).encode(encoding=ENCODING)
        cipher = AES.new(key, AES.MODE_CBC, iv=IV.encode(encoding=ENCODING))
        result = cipher.encrypt(raw.encode(ENCODING))
        return AesMaster.__bytes2hex(result)

    @staticmethod
    def decrypt(source: str, key: str = DEFAULT_KEY):
        """
        解密
        """
        enc = binascii.a2b_hex(source)
        key = str(hashlib.md5(str(key).encode(ENCODING)).hexdigest()).encode(encoding=ENCODING)
        cipher = AES.new(key, AES.MODE_CBC, iv=IV.encode(encoding=ENCODING))
        result = cipher.decrypt(enc)
        return str(result.decode(ENCODING)).replace('\n', '')


if __name__ == '__main__':
    encrypt = AesMaster.encrypt('test content', key='this is a key')
    print(encrypt)
    decrypt = AesMaster.decrypt(encrypt, key='this is a key')
    print(decrypt)

