import sys
sys.path.append("/NewAppLib")
from os import listdir
from multiprocessing import Process
import os 
from NewAppLib.Server import *
from PyQt5 import QtWebEngine
from NewAppLib import webview


def StartBroswerByCode():
    webview.create_window("Hello world", "http://localhost",js_api=True)
    webview.start(http_port=80)




def getFileName():
    global subjects
    FileNames=listdir("database/")
    subjects=[ i[:-3] for i in FileNames if( i.endswith(".db") ) ]

def Main():
    subjects=getFileName()
    prs=Process(target=StartServer,args=[subjects])
    prs.start()
    StartBroswerByCode
    input()
    prs.terminate()




#==========================================================================================================================

        

if(__name__ == "__main__"):
    
    Main()

