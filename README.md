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
