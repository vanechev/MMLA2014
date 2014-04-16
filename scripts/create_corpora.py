#!/usr/bin/env python
#coding: utf8 
import nltk
import re

def processData():
	conn = connectToDB()
	vocabulary = []
	filein = open('output.txt')
	for line in filein:
		tokens = nltk.word_tokenize(line)
		text = nltk.Text(tokens)
		words = [re.sub(u'[^a-zA-ZñáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕöü]',"",(w.lower()).decode('utf-8')) for w in text if len(w) > 1]
		vocab = sorted(set(words))
		print('.'),
		for item in vocab:
			if len(item) > 1:
				cursor = conn.cursor()
				sql = "call addWord('%s')" % item.encode('utf-8')
				try:
					cursor.execute(sql)
				except Exception, e:
					print e
				cursor.close()
				conn.commit()
	conn.close()
						

	# 			vocabulary.append(item)
	
	# fdist2 = nltk.FreqDist(vocabulary)
	# freqDistSorted = fdist2.keys()    # freqDist.sorted() is deprecated
	# with open("vocabulary.txt", "w") as f:
	# 	for word in freqDistSorted:
	# 		f.write(word+"\n")

def connectToDB():
	config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'corpora',
  'raise_on_warnings': True,
	}
	cnx = mysql.connector.connect(**config)
	return cnx

if __name__ == "__main__":

	cadena = "hoña1"
	cadena2 = cadena.decode('utf-8')
	print cadena2
	re.sub(r'[^a-zA-ZñáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕöü]',"",cadena2)
	print cadena2
	with open('prueba2.txt','w') as fout:
		fout.write(cadena2.encode('utf-8'))
	fout.close()

	processData()
	
	

