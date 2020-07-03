import requests

#burpproxy = {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}

#tor settings:
session = requests.session()
session.proxies = {'http':  'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}

def banner():
	print(" ____ _          _    ")
	print(" | _ \ |___  ___| |__ ")
	print(" |  _/ / _ \/ _ \ / / ")
	print(" |_| |_\___/\___/_\_\ Password lookup tool using pwndb2am4tzkvold.onion by @C41NC")
banner()

#user selection:
domain = input("\nWhat domain would you like to lookup, e.g outlook.com:")
username = input("\nWhat email user would you like to lookup [leave empty if none]:")

print("\nSearching for: " + username + "@" + domain)

#check connection:
def check_connection():
	r = session.get('http://pwndb2am4tzkvold.onion.ws/')
	if r.status_code == 200:
		print("\n[+] Connected to the onion network")
		print("[+] pwndb2am4tzkvold.onion is online")
	if r.status_code != 200:
		print("\n[!]Unable to connect to service, is TOR running?")
check_connection()

#Perform lookup with splitlines:
print("-----------------------------------------")
def domain_lookup_split():
	domaindata = ("luser="+username+"&domain="+domain+"&luseropr=0&domainopr=0&submitform=em")
	emptyheaders = {'Connection': 'x', 'Accept-Encoding': 'x', 'Accept': 'x', 'User-Agent': 'x'}
	r = session.post('http://pwndb2am4tzkvold.onion.ws/', data=domaindata, headers=emptyheaders)
	result = r.text
	read = result.splitlines()
	print(r.text)
	for l in read:
		if "[luser]" in l:
			print("Username:", l)
		if "[domain]" in l:
			print("Domain:  ", l)
		if "[password]" in l:
			print("Password:", l)
			print("-----------------------------------------")
#	print(r.text)
domain_lookup_split()
