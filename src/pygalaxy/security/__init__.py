#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import hashlib
import binascii
import jwt
from datetime import datetime, timedelta


ENCODING = "utf-8"
AES_IV = "#fsi&3)f23&fsf%!"
AES_DEFAULT_KEY = "www.wiatec.com"

JWT_DEFAULT_ISSUER = "ex"
JWT_DEFAULT_SUBJECT = "auth"
JWT_SECRET = "#hhjkhkh&jh2432@ndsf*_erkhwek234&ewhkjwehr^hfh234$2l3j4o32urMiOiJ3a" \
             "Jpc3MiOiJ3aWF0ZWMiLCJzdWIiOiJsZWdhY3kiLCJuYmYiOjE1MjAyNjE5NTgsImJzd" \
             "WIiOiJsZWdhY3kiLCJuYmYiOjE1MjAyNjQ0MjksImV4cCI6MTUyMDM1MD2l3j4o3"


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
    def encrypt(source: str, key: str = AES_DEFAULT_KEY):
        """
        加密
        """
        raw = AesMaster.__pad(source)
        key = str(hashlib.md5(str(key).encode(ENCODING)).hexdigest()).encode(encoding=ENCODING)
        cipher = AES.new(key, AES.MODE_CBC, iv=AES_IV.encode(encoding=ENCODING))
        result = cipher.encrypt(raw.encode(ENCODING))
        return AesMaster.__bytes2hex(result)

    @staticmethod
    def decrypt(source: str, key: str = AES_DEFAULT_KEY):
        """
        解密
        """
        enc = binascii.a2b_hex(source)
        key = str(hashlib.md5(str(key).encode(ENCODING)).hexdigest()).encode(encoding=ENCODING)
        cipher = AES.new(key, AES.MODE_CBC, iv=AES_IV.encode(encoding=ENCODING))
        result = cipher.decrypt(enc)
        return str(result.decode(ENCODING)).replace('\n', '')


class JwtMater(object):

    @staticmethod
    def encrypt(expires_days: int=7, issuer: str=JWT_DEFAULT_ISSUER, subject: str=JWT_DEFAULT_SUBJECT):
        """
        加密生成JWT token
        :param expires_days:   token过期时间
        :param issuer:         token发行者
        :param subject:        token主题
        :return:   token字符串
        """
        payload = {
            "sub": subject,
            "iss": issuer,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=expires_days),
        }
        return jwt.encode(payload=payload, key=JWT_SECRET, algorithm="HS256")

    @staticmethod
    def decrypt(token: str):
        """
        解密JWT token
        :param token:    jwt token
        :return: 返回token中包含的payload字典
            {'sub': 'auth', 'iss': 'ex', 'iat': 1628496462, 'exp': 1629101262}
        """
        return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])


if __name__ == '__main__':
    encrypt = AesMaster.encrypt('test content', key='this is a key')
    print(encrypt)
    decrypt = AesMaster.decrypt(encrypt, key='this is a key')
    print(decrypt)
    token = JwtMater.encrypt()
    print(token)
    result = JwtMater.decrypt(token)
    print(result)

