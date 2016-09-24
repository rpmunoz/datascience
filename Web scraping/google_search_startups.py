#! /usr/bin/env python
#
# Required packages:
#
# numpy
# pandas
# google-api-python-client
# openpyxl
# future
#
# Usage
#
# %run google_search_startups.py --api_key=Google_API_KEY --cse_id=Google_customer_search_ID
# For getting the API key and CSE id, follow the isntructions from http://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search

from __future__ import print_function

import numpy as np
import pandas as pd
import argparse
from googleapiclient.discovery import build
import pprint

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def change_encode(data, cols):
    for col in cols:
        data[col] = data[col].str.decode('iso-8859-1').str.encode('utf-8')
    return data   

if __name__ == '__main__':

	ap = argparse.ArgumentParser()
	ap.add_argument("-a", "--api_key", required=True, help="Google API key")
	ap.add_argument("-c", "--cse_id", required=True, help="Google Custom Search Engine ID")
	args = vars(ap.parse_args())

	data_file='desafio_metropolitano_startups.csv'
	search_country='chile'
	search_num=3

	data=pd.read_csv(data_file, header=0, sep=',')
	data.head()

	google_dict={}
	for idx, name in enumerate(data['name']):
		print("Searching info for Startup: ", name)
		title_list=[]
		snippet_list=[]
		link_list=[]
		
		results = google_search(name+' '+search_country, args["api_key"], args["cse_id"], num=search_num)
		for result in results:
			print("Title: ", result['title'])
			print("Link: ", result['link'])
			title_list.append(result['title'])
			snippet_list.append(result['snippet'].replace('\n',' '))
			link_list.append(result['link'])

		google_dict[idx]={ 'title':title_list, 'snippet':snippet_list, 'link':link_list}

	google_data=pd.DataFrame.from_dict(google_dict,orient='index')
	data_info=pd.concat([data,google_data], join='inner', axis=1)[['id','name','title','snippet','link']]
	# Output to CSV file
	data_info.to_csv('desafio_metropolitano_startups_info.csv', index=False, encoding='utf-8')
	# Output to Excel file
	#data.to_excel('desafio_metropolitano_startups_info.xlsx', index=False, encoding='utf-8')