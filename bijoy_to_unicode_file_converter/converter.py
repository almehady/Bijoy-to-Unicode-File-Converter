# from bijoy2unicode import converter
# from main_converter import *
import main_converter
from langdetect import detect
import unicodedata

def convert_bijoy_to_unicode(read_file, write_file):
    print('Working...')
    read_file = open(read_file, "r")
    # for line in read_file:
    #     new_line = len(line.strip())
    #     if new_line != 0:
    #         print('new_line', new_line)

    write_file = open(write_file, 'w')
    # read_file = ["16.	Òm~h©`xNj "]
    for line in read_file:
        try:
            if len(line.strip()) != 0:
                nData = unicodedata.normalize('NFKD', line).encode('UTF-8', 'ignore')
                encoded_new_line = nData.decode()
                eng_text_checker = detect(encoded_new_line)
                if eng_text_checker != 'en':
                    test = main_converter.Unicode()
                    bijoy_text = encoded_new_line
                    toPrint=test.convertBijoyToUnicode(bijoy_text)
                else:
                    toPrint = encoded_new_line
                    

            write_file.write(toPrint)
        except:
            continue

            read_file.close() 


            write_file.close()
        print('Done! Check:', write_file)
# convert_bijoy_to_unicode('bijoy.txt', 'unicode1.txt')