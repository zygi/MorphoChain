import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
source = open("./goldstd_trainset.segmentation.fin", 'r')

r = re.compile(":.*", re.UNICODE)

dest = open("./processed_segmentations.txt", 'w')

for line in source.readlines():
    print line
    l = line.split("	")[1].split(" ")
    print l
    l = [r.sub("", s) for s in l]
    print l
    
    dest.write("-".join(l))
    
    
    