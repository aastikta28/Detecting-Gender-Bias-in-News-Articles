import glob
import json
import name_recognition as nr
import os
import re
import sys

# python extract_names_from_json.py <year>
if len(sys.argv) < 2:
	print 'Please use the format: python extract_names_from_json.py <year>'

year = sys.argv[1]

data_path = os.path.join("data", year.strip())

for i in range(1, 13):
	directory = data_path + "_" + str(i)
	if not os.path.isdir(directory):
		continue
	for file_path in glob.glob(os.path.join(directory, "*")):
		json_string = open(file_path).read().decode('cp1252')
		document = json.loads(json_string)

		# These are the fields that will be retained in the final JSON
		# 'persons', 'subject', 'organizations', 'male', 'female', 'anonymous'
		# will be added later on.
		required_keys = [
			'news_desk',
			'snippet',
			'lead_paragraph',
			'word_count',
			'subsection_name',
			'pub_date',
			'keywords'
		]
		for key in document.keys():
			if key not in required_keys: del document[key]

		# Extract categories from keywords
		for keyword in document['keywords']:
			category = keyword['name']
			value = keyword['value']
			if category not in document: document[category] = []
			document[category].append(value)
			
		# Delete keywords
		del document['keywords']

		# Extract whatever entities we can
		bad_chars = [u'\u2019', u'\u2014']
		para = document['lead_paragraph']
		if para is None: continue
		for bad_char in bad_chars:
		  para = para.replace(bad_char, '')
		ents = nr.get_entities(para)

		# Merge with current dictionary
		for key in ents.keys():
			plural_key = key.lower() + 's'
			if plural_key not in document: 
				document[plural_key] = ents[key]
				continue

		# Call gender labeling function
		first_names = []
		if 'persons' in document:
			for name in document['persons']:
				if ',' in name: name_parts = name.strip().split(',')
				else: name_parts = name.split(' ')
				if len(name_parts) == 1: first_names.append(name)
				elif ',' in name: first_names.append(name_parts[1].split(' ')[0].strip())
				else: first_names.append(name_parts[0].strip())

		print first_names