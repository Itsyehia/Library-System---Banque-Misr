from flask import Flask, json, jsonify, request
from flask_cors import CORS

skills_app=Flask(__name__)


@skills_app.route("/")
def homepage():
    return render_template("homepage.html",pagetitle="HomePage")

@skills_app.route("/about")
def about():
    return  render_template("about.html",pagetitle="AboutPage")



if __name__=="__main__":
    skills_app.run(debug=True, port=9000)



#print("hello")