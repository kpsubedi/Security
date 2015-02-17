import urllib2
import argparse

def geturl():
	parser = argparse.ArgumentParser()
	parser.add_argument("hostname", help="Fetch html page",type=str);
	args = parser.parse_args()
	return args.hostname
def main():
	#urlbody = urllib2.urlopen("http://www.ntc.net.np")
	url = geturl()
	urlfinal = "http://"+url
	#print urlbody.read()
	print urlfinal
	urlhandle = urllib2.urlopen(urlfinal)
	print urlhandle.read()


if __name__=='__main__':
	main()



