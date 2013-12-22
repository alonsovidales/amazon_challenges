final_str = ''
words = []
for count in range(10000):
    words.append("key%s" % str(count).replace('1', 'a').replace('2', 'b').replace('3', 'c').replace('4', 'd').replace('5', 'e').replace('6', 'f').replace('7', 'g').replace('8', 'h').replace('9', 'i').replace('0', 'j'))

for word in words:
    for key in range(20):
        final_str += word + ' '

print final_str
print 10000
print '\n'.join(words)
