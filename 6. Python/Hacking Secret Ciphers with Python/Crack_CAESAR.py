
# 暴力破解凯撒加密 (凯撒加密 实质是 移位加密)


message = 'GUVF VF ZL FRPERG ZRFFNTR'  # 密文

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 所有可以被加密的字符



for key in range(1, len(LETTERS)):  # key 每次都是一个数字

    translated = ''     # 保存加密或解密后的信息

    for symbol in message:  # 循环密文的每个字符
        if symbol in LETTERS:
            num = LETTERS.find(symbol)  # 拿这个字符在字母表里的下标
            num = num - key

            if num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol

    print ( "Key: #%s: %s" % (key, translated) )  # 输出加密/解密后的字符串






