import time

class Logger:
    def log(message):
        currentTime = time.strftime('[%d.%m.%Y %H:%M:%S]', time.localtime())
        message = "{} {}".format(currentTime, message)
        file = open('error.log', 'a')
        file.write(message)
        file.close()

    log = staticmethod(log)