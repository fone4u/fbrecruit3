import csv

filename='Test.csv'
id='ID.txt'
title='title.txt'
body='body.txt'

f=open(filename, 'rb');
f_id=open(id, 'w');
f_title=open(title,'w')
f_body=open(body,'w')

MAX_Line = 1000;
counter=0;

try:
        reader=csv.reader(f)
        for entry in reader:
                f_id.write(entry[0]+"\n");
                f_title.write(entry[1]+"\n");
                if counter==MAX_Line:
                        break;
                counter=counter+1;
finally:
        f.close();
        f_id.close();
        f_title.close();
        f_body.close();


