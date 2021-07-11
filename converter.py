from bijoy2unicode import converter
from langdetect import detect
import unicodedata

def isLineEmpty(line):
    return len(line.strip()) == 0

read_file = open("bijoy.txt", "r")
write_file = open('unicode.txt', 'w')
# read_file = ["16.	Òm~h©`xNj "]
for line in read_file:
    if not isLineEmpty(line):
        nData = unicodedata.normalize('NFKD', line).encode('UTF-8', 'ignore')
        new_line = nData.decode()
        eng_text_checker = detect(new_line)
        if eng_text_checker != 'en':
            test = converter.Unicode()
            bijoy_text = new_line
            toPrint=test.convertBijoyToUnicode(bijoy_text)
        else:
            toPrint = new_line

        write_file.write(toPrint)

read_file.close() 


write_file.close()
