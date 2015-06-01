import argparse
from datetime import datetime

def arg():
    parser = argparse.ArgumentParser(description='Parser')
    time = datetime.strftime(datetime.now(), "%H:%M:%S")
    date = datetime.strftime(datetime.now(), "%Y.%m.%d")
    parser.add_argument("-t", "--time", action='store_const', const='1', help='Time')
    parser.add_argument("-d", "--date", action='store_const', const=date, help='Date')
    parser.add_argument("-u", "--uname", action='store_const', const='DaNiL', help='Uname')
    parser.add_argument("-v", "--version", action='store_const', const='1', help='Python version')
    parser.add_argument("-r", "--tree", action='store_const', const='1', help='Files in directory')
def helper():
    parser = arg()
    s = parser.parse_args()
    print s
helper()