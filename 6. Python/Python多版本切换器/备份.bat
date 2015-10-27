@echo off

: 下面这条是在修改注册表之前先把原有的信息保存, 如果出错, 还可以恢复

REG EXPORT HKEY_CLASSES_ROOT\Python.File\shell  Backup_python.reg /y

pause