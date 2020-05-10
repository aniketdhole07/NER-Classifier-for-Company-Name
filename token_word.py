import spacy 
import pickle
from fuzzywuzzy import fuzz
import read_symbol
import json


def get_list(sentence):
	MIN_FUZZ_VALUE=65
	nlp = spacy.load('en_core_web_sm') 
	company_name=read_symbol.get_company_name()
	security=read_symbol.get_company_security()
	final_list=[]  # list containing 

	doc = nlp(sentence)   
	for ent in doc.ents: 
		if(ent.label_=="ORG"):

			for indx in range(len(company_name)):
				fuzz_value=fuzz.ratio(ent.text,company_name[indx])
				
				if(fuzz_value>=MIN_FUZZ_VALUE):
					print(ent.text)
					
					final_list.append([ent.text,security[indx]])

	return final_list				


