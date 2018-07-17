#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import (
    Flask, jsonify, render_template, request, send_from_directory, url_for, 
    g, redirect, session,
)
import json, os, sqlite3
app = Flask(__name__)

# switchList = [
#                 {
#                     'title':'Area',
#                     'id':'switch_area',
#                     'item':['city_centre','riverside'],
#                     'item_name':['City Centre','Riverside']
#                 }
#             ]
# def to_checked(result):
#     field_name = ['switch_area','switch_custumor_rating','switch_eating_type','switch_family','switch_food','switch_name','switch_near','switch_pricerange']
#     value_name = {'switch_area':['city_centre','riverside'],'switch_custumor_rating':['1_out_of_5','3_out_of_5','5_out_of_5','average','high','low'],'switch_eating_type':['coffee','pub','restaurant'],'switch_family':['no','yes'],'switch_food':['chinese','english','fast_food','french','indian','italian','japanese'],'switch_name':['alimentum','aromi','bibimbap_house','blues_spice','browns_cambridge','clowns','cocum','cotto','fitzbillies','giraffe','green_man','loch_fyne','midsummer_house','strada','taste_of_cambridge','the_cambridge_blue','the_cricketers','the_dumpling_tree','the_eagle','the_golden_curry','the_golden_palace','the_mill','the_olive_grove','the_phoenix','the_plough','the_punter','the_rice_boat','the_twenty_two','the_vaults','the_waterman','the_wrestlers','travellers_rest_beefeater','wildwood','zizzi'],'switch_near':['all_bar_one','avalon','burger_king','cafe_adriatic','cafe_brazil','cafe_rouge','cafe_sicilia','clare_hall','crowne_plaza_hotel','express_by_holiday_inn','rainbow_vegeterian_cafe','raja_indian_cuisine','ranch','the_bakers','the_portland_arms','the_rice_boat','the_six_bells','the_sorrento','yippee_noodle_bar'],'switch_pricerange':['cheap','high','less_than_20','moderate','more_than_30','20_25']}
#     checked_list = [['']*2,['']*6,['']*3,['']*2,['']*7,['']*34,['']*19,['']*6]
#     print(checked_list)
#     for k,v in result.items():
#         f_i = field_name.index(k)
#         v_i = value_name[f_i].index(v)
#         checked_list[f_i][v_i] = 'checked'
#     return 

@app.route('/')
def main():
    return render_template('hnlg.html')

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
    return render_template('hnlg.html', resultList=resultList, resultSent=resultSent, request=result)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=7777)
    # app.run(debug=True)
