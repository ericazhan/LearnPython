#import shutil, sys ; shutil.copy(sys.argv[1], sys.argv[2])
from sys import argv ;open(argv[2], 'w').write(open(argv[1]).read())