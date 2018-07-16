#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import (
    Flask, jsonify, render_template, request, send_from_directory, url_for, 
    g, redirect, session,
)
import json, os, sqlite3
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('hnlg.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        result = request.form       # user request
        print(result)

    resultList = [      # generated words
        [['new','All Bar One','n'],['new','place','n'],['new','it','n'],['new','Midsummer House','n']],
        [['old','All Bar One','n'],['new','is','v'],['new','priced','v'],['old','place','n'],['old','it','n'],['new','is','v'],['new','called','v'],['old','Midsummer House','n']],
        [['old','All Bar One','n'],['old','is','v'],['new','moderately','a'],['old','priced','v'],['new','Italian','a'],['old','place','n'],['old','it','n'],['old','is','v'],['old','called','v'],['old','Midsummer House','n']],
        [['new','Near','Other.'],['old','All Bar One','n'],['old','is','v'],['new','a','Other.'],['old','moderately','a'],['old','priced','v'],['old','Italian','a'],['old','place','n'],['old','it','n'],['old','is','v'],['old','called','v'],['old','Midsummer House','n']]
    ]
    resultSent = 'Near All Bar One is a moderately priced Italian place it is called Midsummer House'
    return render_template('hnlg.html', resultList=resultList, resultSent=resultSent)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7777)
    # app.run(debug=True)
