# TO-DO:
# 1. Implement v4 using BeautifulSoup
# 2. Go through some dockets and ID where all intervenors (and other parties) lie
# 3. Make sure intervenors-by-right are recognized
# 4. Add PDF processing ability as necessary
# 5. Categorize parties as necessary

import requests, re, os, sys, json, gensim

pNum = sys.argv[1]
link = 'https://app.overton.io/documents.php?query=climate+change&sort=relevance&format=json&api_key=fdf0c1-68c742b8da08ef79b613387c67e26567'


#for i in range (1, 26):
  #  pageLink = 
#nextLinkRegex = 
# implement at one call per second

#link = 'https://www.dora.state.co.us/pls/efi/EFI.Show_Docket?p_session_id=&p_docket_id=13A-0836E'
#link = 'https://www.dora.state.co.us/pls/efi/EFI.Show_Docket?p_session_id=&p_docket_id=04S-164E'
r = requests.get(link)
#r = requests.get('https://www.dora.state.co.us/pls/efi/EFI.Show_Docket?p_session_id=&p_docket_id=04S-164E')
rawText = r.content.decode('utf-8', errors='ignore')
jsonLoaded = json.loads(rawText)
results = rawText['results']

json.loads(rawText)

results = rawText[results]

snippetArray = []
#snippetArray = [0 for x in range (20)]


for result in results:
    if result['snippet'] == "":
        del result
    else:
        snippetArray.append(result['snippet'])

