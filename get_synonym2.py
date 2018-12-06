import os
import requests
import json
import pdb
import sys
### Usage python get_synonym.py word
### Issues:
# '/query?node=/c/en/beverage&rel=/r/Synonym&offset=0&limit=50'
# format=json
def syn_query(node,mode):
	if(mode):
		query = 'http://api.conceptnet.io/query?node=/c/en/'+ node +'&rel=/r/Synonym&limit=None'
	else:
		query = 'http://api.conceptnet.io/query?node='+ node +'&rel=/r/Synonym&limit=None'
	return query;
def query_large(node,val):
	return 'http://api.conceptnet.io/c/en/'+node+'?rel=/r/Synonym&limit=' + str(val);
def get_synonyms(start):
	syn_list = []; 
	response = requests.get(query_large(start,sys.maxsize));
	obj = response.json();
	if ('json' not in response.headers['content-type']):
				while('json' not in response.headers['content-type'] ):
					response = requests.get(query_large(start,sys.maxsize));
	for i in range(0,len(obj['edges'])):
		if (('Synonym' in obj['edges'][i]['rel']['label']) & (obj['edges'][i]['start']['language'] == 'en')):
			syn_list.append(obj['edges'][i]['start']['label']);
	t_new = [i for i,m in enumerate(syn_list) if m == start ]; # if for any reason self references are there!	
	t_new.sort(reverse=True);
	for i in t_new:
		del(syn_list[i]);
	syn_list = list(set(syn_list));
	return syn_list;
h = sys.argv;
syn_li = get_synonyms(h[1]);
print(syn_li);	