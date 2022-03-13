from flask import Flask
from flask import render_template
from flask import request
import requests



app=Flask(__name__)

@app.route('/')
def about():
  return render_template('about.html')
  
  
if __name__=="__main__":
  app.run()
