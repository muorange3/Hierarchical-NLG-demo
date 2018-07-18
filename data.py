import json
with open('example.txt') as f: lines = f.readlines()
out = []
done_sent = {'name':'', 'eatType':'', 'food':'', 'priceRange':'', 'area':'', 'familyFriendly':'', 'near':'', 'customerRating':''}
word_layer = [[],[],[],[]]
resultList = [[],[],[],[]]
for l in lines:
	l = l.replace('\n','')
	if l.startswith('Input: '):
		sent = l.replace('Input: ','').split(' ')
		tmp = ''
		tag = ''
		for s in sent:
			if s == 'customer': continue
			elif s == 'rating': 
				if tag!='':
					done_sent[tag] = tmp
					tmp = ''
				tag = 'customerRating'
			elif s in done_sent: 
				if tag!='': 
					done_sent[tag] = tmp
					tmp = ''
				tag = s
			else:
				if tmp!='': tmp+=('_'+s)
				else: tmp = s
		print(done_sent)
	elif l.startswith('First Layer Output: '): word_layer[0] = l.replace('First Layer Output: ','').split(' ')
	elif l.startswith('Second Layer Output: '): word_layer[1] = l.replace('Second Layer Output: ','').split(' ')
	elif l.startswith('Third Layer Output: '): word_layer[2] = l.replace('Third Layer Output: ','').split(' ')
	elif l.startswith('Fourth Layer Output: '): 
		word_layer[3] = l.replace('Fourth Layer Output: ','').split(' ')
		out.append({'input':done_sent, 'output':word_layer, 'output_sent': l.replace('Fourth Layer Output: ','')})
		with open('out3.json','w') as f: json.dump(out, f)
		done_sent = {'name':'', 'eatType':'', 'food':'', 'priceRange':'', 'area':'', 'familyFriendly':'', 'near':'', 'customerRating':''}
		resultList = [[],[],[],[]]