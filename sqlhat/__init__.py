from Pymacs import lisp
from dbcfg import DBConfig
import logging  


dbcfg = None



interactions = {}

def init(content):
    global dbcfg
    dbcfg = DBConfig(content)
#    logging.basicConfig(filename = '/home/chengming/log.txt', level = logging.DEBUG)

def getParameter(parameter):
    global dbcfg
    return dbcfg.getParameter(parameter)
    

interactions[init] = ''
interactions[getParameter] = ''
