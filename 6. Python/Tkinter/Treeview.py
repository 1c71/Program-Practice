import Tkinter
import ttk



root = Tkinter.Tk()



tree = ttk.Treeview()

# 往根元素的最后插入,名字是Widget Tour
tree.insert('', 'end', iid='widgets', text='Widget Tour')

 
# 插入到跟元素的第一个
tree.insert('', 0, 'gallery', text='Applications')


# 往根元素的最后插入,名字是Tutorial
id = tree.insert('', 'end', text='Tutorial')



# 插入到已经存在的节点
tree.insert('widgets', 'end', text='Canvas')
tree.insert(id, 'end', text='Tree')



tree.item('widgets', open=True)


tree = ttk.Treeview(root, columns=('size', 'modified'))
tree['columns'] = ('size', 'modified', 'owner')

tree.column('size', width=100, anchor='center')
tree.heading('size', text='Size')







tree.pack()

root.mainloop()















