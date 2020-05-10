import token_word  #Used to get final_list
import json  #Used to store output to json format
from collections import defaultdict  #Used for appending in dictionary

sentence="Apple, Amazon and Microsoft are reporting earnings after market close on April 30th." #input sentence
final_list=token_word.get_list(sentence)  #returns the predictions  ('company_name','security')

symbol=[]  #used to store output

for i in range(len(final_list)):
	symbol.append(final_list[i][1])  #used to add company_name security to output


json_output={'security':None,'securities':None}  #json format
json_output = defaultdict(list)
if(len(symbol)>0):
	json_output['security']=symbol[0]  #adding first occurance to output dict
	for i in symbol:
		json_output['securities'].append(i)   #adding all occurance to output dict
with open('output.json', 'w') as json_file:
  json.dump(json_output, json_file)  
