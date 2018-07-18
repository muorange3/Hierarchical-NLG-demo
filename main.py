#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json, os, sqlite3, requests
from flask import (
    Flask, jsonify, render_template, request, send_from_directory, url_for, 
    g, redirect, session,
)
app = Flask(__name__)

ONLINE = False

def clean(d):
    for k,v in d.items(): d[k] = v[0]
    return d

def assign_word_type(word_layer):
    word_type = ['n','v','a','other']
    resultList = [[],[],[],[]]
    for i in range(len(word_layer)):
        if i==0:
            for w in word_layer[i]: resultList[i].append([w,word_type[i]])
        else:
            for w in word_layer[i]:
                if w in word_layer[i-1]: resultList[i].append(resultList[i-1][word_layer[i-1].index(w)])
                else: resultList[i].append([w,word_type[i]])
    return resultList

@app.route('/')
def main():
    return render_template('hnlg.html', request={})

@app.route('/result', methods=['GET', 'POST'])
def result():
    resultList = [[],[],[],[]]
    resultSent = ''

    if request.method == 'POST':
        result = clean(request.form.to_dict(flat=False))       # user request
        print(result)
        
        if ONLINE:
            r = requests.post("http://140.112.29.227:3000/predict", data=result)
            # print(r)
            data = r.json()
            for i,d in enumerate(data['results']): resultList[i] = d[0]
            resultSent = ' '.join(resultList[3])
        else:        
            with open('out.json','r') as f: example_pairs = json.load(f)
            for example_pair in example_pairs:
                same = 1
                for k,v in result.items():
                    if example_pair['input'][k] in ['','NAME']: continue
                    if v != example_pair['input'][k]:
                        same=0
                        break
                if same==1:
                    resultList = example_pair['output']
                    resultSent = example_pair['output_sent']
                    break

        if result['name']!='':
            resultSent = resultSent.replace('NAMETOKEN', result['name'])
            for l in resultList:
                for i,w in enumerate(l):
                    if w=='NAMETOKEN': l[i] = result['name']

    return render_template('hnlg.html', resultList=assign_word_type(resultList), resultSent=resultSent, request=result)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7777)
    # app.run(debug=True)
