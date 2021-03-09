import time

class Logger:
    # Construct the log message and write it to the log
    def log(message):
        currentTime = time.strftime('[%d.%m.%Y %H:%M:%S]', time.localtime())
        message = "{} {}".format(currentTime, message)
        file = open('error.log', 'a')
        file.write(message)
        file.close()

    # Define the log method as a static method
    log = staticmethod(log)