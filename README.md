# Detecting-Gender-Bias-in-News-Articles


--------------------------------------------------------------------------------

SOLR
Starting solr: bin/solr start -p 8080
Stopping solr: bin/solr stop -all
Accessing solr: http://detecting-gender-bias-achaitra11021.c9users.io/solr

--------------------------------------------------------------------------------

CORES
Creating a core: bin/solr create -c "core_name"

--------------------------------------------------------------------------------

DATA
XML format:
  <add>
    <doc>
      <field name="id">Value</field>
      <field name="news_desk">Value</field>
    </doc>
  </add>
  
Adding files:
    - cd to directory containing file
    - curl "http://detecting-gender-bias-achaitra11021.c9users.io/solr/mycore/
    update?commit=true" -H 'Content-type:text/xml' --data-binary @sample.xml
Querying core:
    curl "http://detecting-gender-bias-achaitra11021.c9users.io/solr/mycore/
    select?q=news_desk:Sports&wt=xml"

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
java -mx1000m -cp stanford-ner-2015-04-20\classifiers\english.all.3class.distsim.crf.ser.gz -port 8080 -outputFormat inlineXML

