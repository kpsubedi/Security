import ctypes

if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print '[-] You do not have admin access!'
else:
    print '[+] You have admin access'
