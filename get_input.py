import token_word
import read_symbol
import json 
from collections import defaultdict

sentence="Apple, Amazon and Microsoft are reporting earnings after market close on April 30th."
final_list=token_word.get_list(sentence)
symbol=[]

for i in range(len(final_list)):
	symbol.append(final_list[i][1])
print(symbol)	

json_output={'security':None,'securities':None}
json_output = defaultdict(list)
if(len(symbol)>0):
	json_output['security']=symbol[0]
	for i in symbol:
		json_output['securities'].append(i)
with open('output.txt', 'w') as json_file:
  json.dump(json_output, json_file)
