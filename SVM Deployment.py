import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("SVMclassifier.pkl","rb")
classifier=pickle.load(pickle_in)
  

def Welcome():
    return "welcome All"

def predict_song(danceability,energy,key,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms):
        
     
       prediction=classifier.predict([[danceability,energy,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms]])
       print(prediction)
       return prediction
   
    
def main():
        st.title("spotify song")
        html_temp="""
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:centre;">streamlit spotify song ML app</h2>
        </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
        danceability = st.text_input("danceability","Type_here")
        energy = st.text_input("energy","Type_here")
        key = st.text_input("key","Type_here")
        loudness = st.text_input("loudness","Type_here")
        speechiness = st.text_input("speechiness","Type_here")
        acousticness = st.text_input("acousticness","Type_here")
        instrumentalness= st.text_input("intrumentalness","Type_here")
        liveness= st.text_input("liveness","Type_here")
        valence= st.text_input("valence","Type_here")
        tempo= st.text_input("tempo","Type_here")
        duration_ms= st.text_input("duration","Type_here")
        result=" "
        if st.button("predict"):
            result=predict_song(danceability,energy,key,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms)
        st.success('The output is {}'.format(result))
              
if __name__=='__main__':
    main()


       
          
           
              
            
         
           
                   
    
                 
                    
