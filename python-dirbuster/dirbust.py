import requests, os, argparse
from sys import argv 

title = """
$$$$$$$\  $$\           $$\                             $$\                         
$$  __$$\ \__|          $$ |                            $$ |                        
$$ |  $$ |$$\  $$$$$$\  $$$$$$$\  $$\   $$\  $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$ |  $$ |$$ |$$  __$$\ $$  __$$\ $$ |  $$ |$$  _____|\_$$  _|  $$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |$$ |  \__|$$ |  $$ |$$ |  $$ |\$$$$$$\    $$ |    $$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |$$ |      $$ |  $$ |$$ |  $$ | \____$$\   $$ |$$\ $$   ____|$$ |      
$$$$$$$  |$$ |$$ |      $$$$$$$  |\$$$$$$  |$$$$$$$  |  \$$$$  |\$$$$$$$\ $$ |      
\_______/ \__|\__|      \_______/  \______/ \_______/    \____/  \_______|\__|
"""

print(title)

custom_help = """
A Program to Fetch Directories of a Site. 
You can enter either IP Address of the website or you can use the Domain Name.
Directories will be scanned from the list specified by you.
"""
custom_usage = "Port_Scanner.py [-i] [-w]"

def main():
	praser = argparse.ArgumentParser()
	parser = argparse.ArgumentParser(usage = custom_usage, add_help=False)
	praser.add_argument('--ip', '-i' ,type = str, default= "", help = "Domain Name/ IP Address of Target")
	praser.add_argument('--wordlist', '-w', type = str, default= "", help = "Word List")
	parser.add_argument('-h', '--help', action='store_true', help=print(custom_help))
	args = praser.parse_args()
	if not any(vars(args).values() or args.help or args.h):
		print(help)
	dirb(args.ip, args.wordlist)

def dirb(urls,wordlist):
	arr=[]
	url=urls
	try:
		if url[:7] != 'http://':
			url="http://"+url
		r=requests.get(url)
		if r.status_code == 200:
			print('Host is up.')
		else:
			print('Host is down.')
			return
		if os.path.exists(os.getcwd()+wordlist):
			fs=open(os.getcwd()+wordlist,"r")
			for i in fs:
				print(url+"/"+i)
				rq=requests.get(url+"/"+i)
				if rq.status_code == 200:
					print(">OK".rjust(len(url+"/"+i)+5,'-'))
					arr.append(str(url+"/"+i))
				else:
					print(">404".rjust(len(url+"/"+i)+5,'-'))
			fs.close()
			print("output".center(100,'-'))
			l=1
			for i in arr:
				print(l, "> ", i)
				l+=1
		else:
			print(wordlist+" don't exists in the directory.")
	except Exception as e:
		print(e)



if __name__ == '__main__':
	main()