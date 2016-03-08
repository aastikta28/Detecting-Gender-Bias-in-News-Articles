# Detecting-Gender-Bias-in-News-Articles


--------------------------------------------------------------------------------

SOLR
Starting solr: bin/solr start -p 8080
Stopping solr: bin/solr stop -all
Accessing solr: http://detecting-gender-bias-achaitra11021.c9users.io/solr

--------------------------------------------------------------------------------

CORES
Creating a core: bin/solr create -c trial -d server/solr/configsets/basic_configs/

--------------------------------------------------------------------------------

Adding files:
    - cd to directory containing the month folder
    - ../../solr/solr-5.4.1/bin/post -c trial <file> -p 8080  
Querying core:
    curl "http://detecting-gender-bias-achaitra11021.c9users.io/solr/trial/
    select?q=news_desk:Sports&wt=xml"
    
Deleting all files in index:
curl http://localhost:8983/solr/update --data '<delete><query>*:*</query></delete>' -H 'Content-type:text/xml; charset=utf-8'
curl http://localhost:8983/solr/update --data '<commit/>' -H 'Content-type:text/xml; charset=utf-8'

--------------------------------------------------------------------------------

Python with Stanford NER:
Stanford NER version: 2015-04-20
PyNER: pip install ner

Environment variables:
STANFORD_MODELS
\stanford-ner\classifiers

JAVAHOME
\Java\JDK18~1.0_6\java.exe

CLASSPATH
\stanford-ner\stanford-ner.jar

Start Stanford NER server:
java -mx1000m -cp stanford-ner-2015-04-20\stanford-ner.jar edu.stanford.nlp.ie.NERServer -loadClassifier stanford-ner-2015-04-20\classifiers\english.all.3class.distsim.crf.ser.gz -port 8080 -outputFormat inlineXML

-------------------------------------------

Schema details:
1. Remove managed schema from solrconfig.xml
2. 
