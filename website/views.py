from flask import Blueprint, render_template

views = Blueprint('views')


@views.route('/')
def home():
    return render_template("home.html")
    
    If ___name___ == "___main___" 
    Debug=true