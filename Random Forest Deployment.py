# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:54:41 2021

@author: HP
"""
from flask import Flask, request, url_for, render_template
import pickle

app=Flask(__name__)
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Predict', methods=['POST'])
def Predict():
    #if request.method == 'POST':
    danceability = request.form['danceability']
    energy = request.form['energy']
    key = request.form['key']
    speechiness = request.form['speechiness']
    acousticness = request.form['acousticness']
    instrumentalness = request.form['instrumentalness']
    liveness = request.form['liveness']
    valence = request.form['valence']
    tempo = request.form['tempo']
    duration = request.form['duration']
    loudness = request.form['loudness']
    my_prediction = classifier.predict([[danceability,energy,key,speechiness,acousticness,
                                    instrumentalness,liveness,valence,tempo,duration,loudness]])
    return render_template('results.html', prediction = my_prediction)
    #return "Hello The answer is"+str(my_prediction)



if __name__=='__main__':    
    app.run()