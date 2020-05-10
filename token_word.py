import spacy 
import pickle
from fuzzywuzzy import fuzz  #fuzz value to check similarity between two strings
import read_symbol  


def get_list(sentence):
	MIN_FUZZ_VALUE=65   #fuzz value to check similarity between two strings
	nlp = spacy.load('en_core_web_sm')  #pretrained model
	company_name=read_symbol.get_company_name()  # list containing company_name
	security=read_symbol.get_company_security()  # list containing security symbols
	final_list=[]  # list containing output list (company_name,security)

	doc = nlp(sentence)   #used to find entity
	for ent in doc.ents: 
		if(ent.label_=="ORG"):  #if entity is of an organization(company)

			for indx in range(len(company_name)):
				fuzz_value=fuzz.ratio(ent.text,company_name[indx])
				
				if(fuzz_value>=MIN_FUZZ_VALUE):
					final_list.append([ent.text,security[indx]]) 

	return final_list				


