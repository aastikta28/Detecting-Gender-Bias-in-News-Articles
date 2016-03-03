import ner

def get_entities(snippet):
  tagger = ner.SocketNER(host='localhost', port=8080)
  return tagger.get_entities(snippet)

ents = get_entities('Total Truth, the North American Cup winner, drew the No. 5 post position and was made the 3-1 morning line favorite yesterday for the $300,000 Cane Pace on Labor Day at Freehold Raceway in New Jersey. The race is the first event in the Pacing Triple Crown. Total Truth, who will be driven by Ron Pierce, has seasonal earnings of more than $1 million' )

print ents['PERSON']
