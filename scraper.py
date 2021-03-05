from Parser import Parser
from Logger import Logger
import traceback
import time

parser = Parser()

while True:
    try:
        parser.parse()
    except Exception as e:
        Logger.log(traceback.format_exc())
        time.sleep(1)