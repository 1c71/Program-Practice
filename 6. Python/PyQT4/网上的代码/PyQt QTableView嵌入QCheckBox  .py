#coding=utf-8

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CheckBoxDelegate(QItemDelegate):

  def __init__(self, parent=None):
    QItemDelegate.__init__(self, parent)
    self.chkboxSize = 19 #?!

  def createEditor(self, parent, option, index):
    chkbox = QCheckBox(parent)
    chkbox.setText('')
    chkbox.setTristate(False) #只用两个状态
    left = option.rect.x() + (option.rect.width() - self.chkboxSize) / 2
    top  = option.rect.y() + (option.rect.height() - self.chkboxSize) / 2
    chkbox.setGeometry(left, top, self.chkboxSize, self.chkboxSize)
    return chkbox

  def paint(self, painter, option, index):
    value = index.data().toBool()
    opt = QStyleOptionButton()
    opt.state |= QStyle.State_Enabled | (QStyle.State_On if value else QStyle.State_Off)
    opt.text = ''
    left = option.rect.x() + (option.rect.width() - self.chkboxSize) / 2
    top  = option.rect.y() + (option.rect.height() - self.chkboxSize) / 2
    opt.rect = QRect(left, top, self.chkboxSize, self.chkboxSize)
    QApplication.style().drawControl(QStyle.CE_CheckBox, opt, painter)

  def updateEditorGeometry(self, editor, option, index):
    pass

###############################################################################

if __name__ == '__main__':

  import sys

  app = QApplication(sys.argv)

  table = QTableView()
  model = QStandardItemModel(3, 3, table)
  model.setHorizontalHeaderLabels(['Name', 'Description', 'Animal?'])
  model.setData(model.index(0, 0, QModelIndex()), QVariant('Squirrel'))
  model.setData(model.index(0, 1, QModelIndex()), QVariant(u'可爱的松树精灵'))
  model.setData(model.index(0, 2, QModelIndex()), QVariant(True))
  model.setData(model.index(1, 0, QModelIndex()), QVariant('Soybean'))
  model.setData(model.index(1, 1, QModelIndex()), QVariant(u'他站在田野里吹风'))
  model.setData(model.index(1, 2, QModelIndex()), QVariant(False))
  table.setModel(model)
  table.setItemDelegateForColumn(2, CheckBoxDelegate(table))
  table.resizeColumnToContents(1)
  table.horizontalHeader().setStretchLastSection(True)
  table.setGeometry(80, 20, 400, 300)
  table.setWindowTitle('Grid + CheckBox Testing')
  table.show()

  sys.exit(app.exec_())
