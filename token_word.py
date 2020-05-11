

import spacy 
import pickle
from fuzzywuzzy import fuzz  #fuzz value to check similarity between two strings
import read_symbol  


def get_list(sentence):
	MIN_FUZZ_VALUE=55   #fuzz value to check similarity between two strings
	nlp = spacy.load('en_core_web_sm')  #pretrained model
	company_name=read_symbol.get_company_name()  # list containing company_name
	security=read_symbol.get_company_security()  # list containing security symbols
	final_list=[]  # list containing output list (company_name,security)
 
	doc = nlp(sentence)   #used to find entity
	for ent in doc.ents: 
		temp_fuzz_value=[]  #used to store all fuzz values

		#Now it checks the maximum fuzz value and outputs only single company instead of multiple
		for indx in range(len(company_name)):
			temp_fuzz_value.append(fuzz.ratio(ent.text,company_name[indx]))
			
		max_fuzz_value=max(temp_fuzz_value)	 #Find maximum fuzz value to get best results
		company_index=temp_fuzz_value.index(max_fuzz_value)
		
		if(max_fuzz_value>=MIN_FUZZ_VALUE):
			#print(ent.text)
			final_list.append([ent.text,security[company_index]]) 

	return final_list				


