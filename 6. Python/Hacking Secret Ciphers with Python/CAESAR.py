
# 程序是凯撒加密
# 凯撒加密实质就是移位加密

import pyperclip


message = 'this is my screct message.'


key = 13    # 移多少位

mode = 'encrypt'    # encrypt / decrypt, 模式是加密或解密

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 所有可以被加密的字符

translated = ''     # 保存加密或解密后的信息

message = message.upper()   # 把信息弄成大写


for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)  # 拿下标

        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        # 根据是加密或解密来处理下标

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        if num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol


print (translated)  # 输出加密/解密后的字符串

pyperclip.copy(translated)  # 把字符串复制到剪切板.




























