from flask import Flask, render_template, request
import pymysql
from dynaconf import Dynaconf
import flask_login
import requests
import csv
import json

def requestinfo(schoolstate, schoolcity):

    # conn=connect_db()
    # cursor=conn.cursor()

    # schoolname=request.form['schoolname']
    # schoolstate=request.form['schoolstate']

    count=0

    api="https://api.data.gov/ed/collegescorecard/v1/schools?api_key=fEZsVdtKgtVU4ODIpjHcP8vDttDK0ftSGZaWDcAk"

    queries={}
    request=''
    
    if schoolstate:
        queries.update({"school.state":(f"{schoolstate}")})

    if schoolcity:
            queries.update({"school.ciry":(f"{schoolcity}")})

    for query in queries:
        request+=(f"{query}={queries[query]}")
        count+=1
    
    request=f"{api}&{request}"

    test=requests.get(request).json()

    for key in test:{ 
        print(key,":", test[key]) 
    }
        
    return request

print(requestinfo("Harvard university", "Massachusetts"))