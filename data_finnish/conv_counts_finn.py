import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
r = re.compile("([^\s]+)\s+([^\s]+)", re.UNICODE)

source = open("./wordlist-2010.txt", 'r')


dest = open("./processed_word_counts.txt", 'w')

for line in source.readlines():
    m = r.match(line)
    t1 = m.group(1)
    t2 = m.group(2)
    dest.write(str(t2))
    dest.write(" ")
    dest.write(t1)
    dest.write("\n")