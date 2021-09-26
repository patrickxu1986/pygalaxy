#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import hashlib
import binascii
import jwt
from datetime import datetime, timedelta


ENCODING = "utf-8"
AES_IV = "2018071119861008"
AES_DEFAULT_KEY = "&h24*3)u6@m#,1p~7k&/q!=6h^l*"

JWT_DEFAULT_ISSUER = "ex"
JWT_DEFAULT_SUBJECT = "auth"
JWT_SECRET = "#hhjkhkh&jh2432@ndsf*_erkhwek234&ewhkjwehr^hfh234$2l3j4o32urMiOiJ3a" \
             "Jpc3MiOiJ3aWF0ZWMiLCJzdWIiOiJsZWdhY3kiLCJuYmYiOjE1MjAyNjE5NTgsImJzd" \
             "WIiOiJsZWdhY3kiLCJuYmYiOjE1MjAyNjQ0MjksImV4cCI6MTUyMDM1MD2l3j4o3"


def md5(source: str):
    return hashlib.md5(source.encode(ENCODING)).hexdigest()


def md5_16(source: str):
    return hashlib.md5(source.encode(ENCODING)).hexdigest()[8: 24]


class AesMaster:

    @staticmethod
    def encrypt(source: str, key: str=AES_DEFAULT_KEY, iv: str=AES_IV):
        """
        加密
        """
        amount_to_pad = AES.block_size - (len(source) % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        raw = source + chr(amount_to_pad) * amount_to_pad
        key = str(hashlib.md5(key.encode(ENCODING)).hexdigest()).encode(encoding=ENCODING)
        cipher = AES.new(key, AES.MODE_CBC, iv=iv.encode(encoding=ENCODING))
        encrypt_bytes = cipher.encrypt(raw.encode(ENCODING))
        return str(binascii.b2a_hex(encrypt_bytes).decode(ENCODING))

    @staticmethod
    def decrypt(source: str, key: str=AES_DEFAULT_KEY, iv: str=AES_IV):
        """
        解密
        """
        enc = binascii.a2b_hex(source)
        key = str(hashlib.md5(str(key).encode(ENCODING)).hexdigest()).encode(encoding=ENCODING)
        cipher = AES.new(key, AES.MODE_CBC, iv=iv.encode(encoding=ENCODING))
        decrypt_bytes = cipher.decrypt(enc)
        return str(decrypt_bytes.decode(ENCODING)).replace('\n', '')


class JwtMaster(object):

    @staticmethod
    def encrypt(expires_days: int=7, issuer: str=JWT_DEFAULT_ISSUER, subject: str=JWT_DEFAULT_SUBJECT):
        """
        加密生成JWT token
        :param expires_days:   token过期天数
        :param issuer:         token发行者
        :param subject:        token主题
        :return:               token字符串
        """
        payload = {
            "sub": subject,
            "iss": issuer,
            "iat": datetime.utcnow(),
            "nbf": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=expires_days),
        }
        return jwt.encode(payload=payload, key=JWT_SECRET, algorithm="HS256")

    @staticmethod
    def decrypt(token_str: str):
        """
        解密JWT token
        :param token_str:      jwt token
        :return:               返回token中包含的payload字典
                                    {'sub': 'auth', 'iss': 'ex', 'iat': 1628499184, 'nbf': 1628499184, 'exp': 1629103984}
        """
        return jwt.decode(token_str, JWT_SECRET, algorithms=['HS256'])


if __name__ == '__main__':
    encrypt = AesMaster.encrypt('test content')
    print(encrypt)
    decrypt = AesMaster.decrypt(encrypt)
    print(decrypt)
    token = JwtMaster.encrypt()
    print(token)
    result = JwtMaster.decrypt(token)
    print(result)
    print(md5('123'))
    print(md5_16('123'))
