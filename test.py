from flask import Flask, render_template, request
import pymysql
from dynaconf import Dynaconf
import flask_login
import requests
import csv
import json

# Config settings and secrets
conf = Dynaconf(
    settings_file = ["settings.toml"]
)

def connect_db():
    """Connect to the phpMyAdmin database (LOCAL STEAM NETWORK ONLY)"""
    conn = pymysql.connect(
        host = "db.steamcenter.tech",
        database = "apollo",
        user = "kchapman",
        password = conf.password,
        autocommit = True,
        cursorclass = pymysql.cursors.DictCursor
    )
    return conn
