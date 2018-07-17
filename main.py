#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json
from flask import (
    Flask, jsonify, render_template, request, send_from_directory, url_for, 
    g, redirect, session,
)
import json, os, sqlite3
app = Flask(__name__)

with open('out.json','r') as f: example_pairs = json.load(f)

@app.route('/')
def main():
    return render_template('hnlg.html', request={})

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict(flat=False)       # user request
        print(result)

        resultList = [      # generated words
            [['new','All Bar One','n'],['new','place','n'],['new','it','n'],['new','Midsummer House','n']],
            [['old','All Bar One','n'],['new','is','v'],['new','priced','v'],['old','place','n'],['old','it','n'],['new','is','v'],['new','called','v'],['old','Midsummer House','n']],
            [['old','All Bar One','n'],['old','is','v'],['new','moderately','a'],['old','priced','v'],['new','Italian','a'],['old','place','n'],['old','it','n'],['old','is','v'],['old','called','v'],['old','Midsummer House','n']],
            [['new','Near','other'],['old','All Bar One','n'],['old','is','v'],['new','a','other'],['old','moderately','a'],['old','priced','v'],['old','Italian','a'],['old','place','n'],['old','it','n'],['old','is','v'],['old','called','v'],['old','Midsummer House','n']]
        ]
        resultSent = 'Near All Bar One is a moderately priced Italian place it is called Midsummer House'
        for i in range(len(example_pairs)):
            same = 1
            for k,v in result.items():
                if example_pairs[i]['input'][k] in ['','NAMETOKEN']: continue
                if v[0] != example_pairs[i]['input'][k]:
                    same=0
                    break
            if same==1:
                resultList = example_pairs[i]['output']
                resultSent = example_pairs[i]['output_sent']
                if result['name']!='':
                    resultSent = resultSent.replace('NAMETOKEN', result['name'][0])
                    for l in resultList:
                        for w in l:
                            for i in range(len(w)):
                                if w[i]=='NAMETOKEN': w[i] = result['name'][0]

    return render_template('hnlg.html', resultList=resultList, resultSent=resultSent, request=result)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7777)
    # app.run(debug=True)
