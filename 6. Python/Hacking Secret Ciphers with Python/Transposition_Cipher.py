
# 实现移位加密
# 跟凯撒加密不同的是, 移位加密不会替换字符, 只是移动字符位置而已.


import pyperclip



def encryptMessage(myKey, myMessage):
    
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]

            pointer += key

    return ''.join(ciphertext)





myMessage = 'Common Sense is not so common'
myKey = 8
# 要加密的明文 以及 移位的数量
    
ciphertext = encryptMessage(myKey, myMessage)
# 调用函数获得密文

print (ciphertext + '|')
pyperclip.copy(ciphertext)  # 复制到剪贴板










































