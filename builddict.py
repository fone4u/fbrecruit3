import csv
import textmining
import re
from HTMLParser import HTMLParser

filename='Test.csv'
id='ID.txt'
title='title.txt'
body='body.txt'

f=open(filename, 'rb');
f_id=open(id, 'w');
f_title=open(title,'w')
f_body=open(body,'w')

MAX_Line = 3;
counter=0;

class Stripper(HTMLParser):
        def __init__(self):
                self.reset()
                self.fed=[]
        def handle_data(self, d):
                self.fed.append(d)
        def get_data(self):
                return ''.join(self.fed)

def strip(strng):
        s=Stripper()
        s.feed(strng)
        return s.get_data()

def print_matrix(tdm):
        for row in tdm.rows(cutoff=1):
                print row
        return

def stemming(tmp):
        for word in tmp:
                print textmining.stem(word)

tdm=textmining.TermDocumentMatrix()

def createDic(tmp):
        for word in tmp:
                if dict.get(word):
                        dict[word]=dict[word]+1
                else:
                        dict[word]=1
        print dict
        return dict

try:
        reader=csv.reader(f)
        for entry in reader:
                dict={}
                f_id.write(entry[0]+"\n");
                f_title.write(entry[1]+"\n");
                if counter==MAX_Line:
                        break;
                counter=counter+1;
                #print entry[2]
                tmp=strip(entry[2])
                tmp= textmining.simple_tokenize_remove_stopwords(tmp)
                dict= createDic(tmp)
                
finally:
        f.close();
        f_id.close();
        f_title.close();
        f_body.close();
