import os, ctypes

import win32api
import servicemanager
import win32serviceutil
import win32service

class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = 'ScsiAccess'
    _svc_display_name_ = 'ScsiAccess'
    
    
    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)
        
    def sleep(self, sec):
        win32api.Sleep(sec*1000, True)
        
