import md5
def getmd5():
    m = md5.new()
    m.update("Kul")
    m.update("Prasad")
    print m.hexdigest()
    print("Added:")
    m1 = md5.new()
    m1.update("KulPrasad")
    print m1.hexdigest()		

getmd5()
