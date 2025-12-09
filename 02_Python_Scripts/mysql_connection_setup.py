# CONNECT TO MYSQL
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='**********',
    database='ecommerce'
)
cursor = conn.cursor()
