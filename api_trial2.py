#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 02:10:06 2020

@author: shalinimustala
"""
import flask
from flask import request, jsonify

def tempbymonth1(month, year, countryname):
    
    from mysql import connector

    cnx = connector.connect(user='shalini1', password='hello', host='18.188.12.200', database='551project')

    cursor = cnx.cursor()

    query = 'select AverageTemperature, city from tempbycity where dt like '  + "'" + str(year) +  '-' + str(month) + "-%'"  + " and country = " + "'" + countryname + "'"

    #query = "select AverageTemperature, city from tempbycity where dt like '2012-12-%' and country = 'India'"
#query = "select distinct city from tempbycity where country = 'India'"
    temp_all = []
    cursor.execute(query)

    for row in cursor:
        temp_all.append(row)
    return temp_all

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/temp', methods=['GET'])
def api_filter():
    query_parameters = request.args

    countryname = query_parameters.get('countryname')
    month = query_parameters.get('month')
    year = query_parameters.get('year')

    temp_all = tempbymonth1(month, year, countryname)

    return jsonify(temp_all)

app.run()

#USE API : http://127.0.0.1:5000/api/temp?month=12&year=2012&countryname=India

