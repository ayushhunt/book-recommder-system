from flask import Flask,render_template,request
import pickle

popular_df=pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
book = pickle.load(open('book.pkl','rb'))