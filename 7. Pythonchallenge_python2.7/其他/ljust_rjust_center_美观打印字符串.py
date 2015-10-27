print '|', '*'.ljust(10), '|'
print '|', '*'.ljust(10,'-'), '|'
print '|', '*'.rjust(10,'-'), '|'
print '|', '*'.center(10,'-'), '|'

for a in range(1, 6):
    print 'a = '.ljust(5), repr(a).ljust(10), 'b = '.ljust(5), repr(a * 2)
