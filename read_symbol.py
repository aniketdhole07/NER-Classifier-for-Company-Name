import pickle

def get_company_name():
	company_name=[]
	file = open('package/symbols.pickle', 'rb')  #read company names from pickle
	data = pickle.load(file)
	file.close()
	for i in data['company']:
	  company_name.append(i)
	company_name.append('Google')  
	return company_name

def get_company_security():
	file = open('package/symbols.pickle', 'rb')  #read company names from pickle
	data = pickle.load(file)
	file.close()
	security=[]
	for i in data['symbol']:
	  security.append(i)
	security.append('GOOGL')
	return security
