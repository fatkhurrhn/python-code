import sys
import time

text = "kamu terlalu berharga untuk disentuh tanpa akad,\njadi jangan mau yaa diajak pacaran, pegang-pegangan,\n peluk-pelukan. kamu itu berharga."

def scrolling_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

scrolling_text(text)