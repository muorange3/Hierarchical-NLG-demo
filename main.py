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
        [['new','All Bar One','N.'],['new','place','N.'],['new','it','N.'],['new','Midsummer House','N.']],
        [['old','All Bar One','N.'],['new','is','V.'],['new','priced','V.'],['old','place','N.'],['old','it','N.'],['new','is','V.'],['new','called','V.'],['old','Midsummer House','N.']],
        [['old','All Bar One','N.'],['old','is','V.'],['new','moderately','Adv.'],['old','priced','V.'],['new','Italian','Adj.'],['old','place','N.'],['old','it','N.'],['old','is','V.'],['old','called','V.'],['old','Midsummer House','N.']],
        [['new','Near','Other.'],['old','All Bar One','N.'],['old','is','V.'],['new','a','Other.'],['old','moderately','Adv.'],['old','priced','V.'],['old','Italian','Adj.'],['old','place','N.'],['old','it','N.'],['old','is','V.'],['old','called','V.'],['old','Midsummer House','N.']]
    ]
    # resultList = [      # generated words
    #     [['new','All Bar One','N.'],['new','place','N.'],['new','it','N.'],['new','Midsummer House','N.']],
    #     [['old','All Bar One'],['new','is'],['new','priced'],['old','place'],['old','it'],['new','is'],['new','called'],['old','Midsummer House']],
    #     [['old','All Bar One'],['old','is'],['new','moderately'],['old','priced'],['new','Italian'],['old','place'],['old','it'],['old','is'],['old','called'],['old','Midsummer House']],
    #     [['new','Near'],['old','All Bar One'],['old','is'],['new','a'],['old','moderately'],['old','priced'],['old','Italian'],['old','place'],['old','it'],['old','is'],['old','called'],['old','Midsummer House']]
    # ]
    resultSent = 'Near All Bar One is a moderately priced Italian place it is called Midsummer House'
    return render_template('hnlg.html', resultList=resultList, resultSent=resultSent)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7777)
    # app.run(debug=True)
