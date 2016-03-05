import glob
import json
import name_recognition as nr
import os
import gender_labeling
#import re
#import sys


def extract_json(yr):
    # python extract_names_from_json.py <year>
   # if len(sys.argv) < 2:
   #     print 'Please use the format: python extract_names_from_json.py <year>'
    
    year = yr
    
    data_path = os.path.join("data", year.strip())
    for i in range(1, 13):
        directory = data_path + "_" + str(i)
        if not os.path.isdir(directory):
            continue
        #file_count = 0
        for file_path in glob.glob(os.path.join(directory, "*")):
            curr_dir = os.getcwd()
            #file_count + 1
            #print "hereeeee ", file_path
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
			'keywords',
                 '_id',
                 'headline'                 
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
            male = []
            female = []
            anony = []
            if 'persons' in document:
                for name in document['persons']:
                    if ',' in name: 
                        name_parts = name.strip().split(',')
                    else: 
                        name_parts = name.split(' ')
                        
                    if len(name_parts) == 1: 
                        gender = gender_labeling.gender_labeling(name)
                        first_names.append(name)
                    elif ',' in name: 
                        name = name_parts[1].split(' ')[0].strip()
                        gender = gender_labeling.gender_labeling(name)
                        first_names.append(name)
                    else: 
                        name = name_parts[0].strip()
                        gender = gender_labeling.gender_labeling(name)
                        first_names.append(name)
                        
                    if gender == 'male':
                        male.append(name)
                    elif gender == 'female':
                        female.append(name)
                    elif gender == 'anonymous':
                        anony.append(name)
                    #print name , " : ", gender
                    
            mydict = {
            "news_desk": document['news_desk'],
            "lead_paragraph": document['lead_paragraph'],
            "headline": document['headline'],
            "word_count": document['word_count'],
            "_id": document['_id'],
            "snippet": document['snippet'],
            "subsection_name": document['subsection_name'],
            "pub_date": document['pub_date'],
            "persons" : document['persons'],
            "male": male,
            "female": female,
            "anonymous": anony
            }
            
            #output_data_path = os.path.join("json_data", year.strip())
            file_name = file_path.split('\\')
            path_prefix = year+'_'+str(i)
            os.chdir('C:\Users\Tanu\Documents\GitHub\Detecting-Gender-Bias-in-News-Articles\json_data')

            if not os.path.exists(path_prefix):
                os.makedirs(path_prefix)
            os.chdir(path_prefix)
            
            with open(file_name[2], mode='w') as feedsjson:            
                json.dump(mydict, feedsjson)
            
            os.chdir(curr_dir)
            print first_names