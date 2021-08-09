#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from decimal import *


def round_half_up(source, fraction_digits: int = 2):
    """
    对给定的浮点数保留指定位数后四舍五入
    :param source: 源数据
    :param fraction_digits: 四舍五入到小数点后的第几位
    """
    # 小数点后保留几位小数
    fmt = '%.' + str(fraction_digits) + 'f'
    # 四舍五入到的位数:
    # 0 -> 到整数位
    # 0.0 -> 到小数点第一位
    # 0.00 -> 到小数点第二位
    fraction = '0'
    for i in range(fraction_digits):
        if '.' in fraction:
            fraction += '0'
        else:
            fraction += '.0'
    result = fmt % (Decimal(str(source)).quantize(Decimal(fraction), ROUND_HALF_UP))
    return result


if __name__ == '__main__':
    print(round_half_up(3.6554381))
