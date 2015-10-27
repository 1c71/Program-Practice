# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

# 使用parse()将XML 文档加载并返回ElementTree 对象
tree = ET.parse("hello.xhtml")

# 寻找head 节点下title节点的值
print tree.findtext("head/title")

# 使用getroot()函式返回根节点
root = tree.getroot()

# ...接下来可以做些其他操作

# 保存为本地XML 文档
tree.write("out.xml")
