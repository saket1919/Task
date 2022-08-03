import logging


logger = logging.getLogger('mylogger')
#setup logger
logger.setLevel(logging.ERROR)


handler = logging.FileHandler('mylog.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#write a error message
logger.error('This is an ERROR message')