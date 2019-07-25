# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import sys
import random
import pprint
from optparse import OptionParser

# create a sequence of words to choose from
#WORDS = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
#WORDS = ["debris", "abuse", "earth", "garbage", "trash", "messy", "laugh",
#        "responsibility", "children", "planet",
#        "diagonal", "circle", "cuboid", "square", "cylinder", "sphere",
#        "surface", "edges", "corners", "rectangle",
#        "antarctica", "hemisphere", "arctic", "america", "continent", "penguin",
#        "equator", "northern", "southern", "dimensions",
#        "germination", "creepers", "sunlight", "photosynthesis", "climbers",
#        "fibrous root", "herbs", "shrubs", "breathe", "flowers"]

def check_options(options, args):
    if len(args) != 1:
        print 'Error: Incorrect number of arguments'
        return False
    return True

usage = '%prog word_file\n'

# Please update this version string
parser = OptionParser(description='jumbles words given in a file',
                      version="%prog 1.0",
                      usage=usage)

(options, args) = parser.parse_args()

if not check_options(options, args):
    parser.print_help()
    sys.exit(-1)

word_file = args[0]

with open(word_file) as f:
        WORDS = f.read().split()

random.shuffle(WORDS)
word = ""

max_len = max(map(lambda x: len(x), WORDS)) + 2
i=0
for word in WORDS:
    i = i+1
    # create a jumbled version of the word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]

    print str(i) + ": " + jumble + " "*(max_len - len(jumble)) + "__ "*len(jumble)
    print


print "\n"*28

i=0
# Answer sheet
print "Answer Key:\n"
for word in WORDS:
    i = i+1
    print str(i) + ": " + word
    print


