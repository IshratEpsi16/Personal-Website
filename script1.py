
from flask import Flask,render_template    #from flask library we import flask class object,
                                            #rebder_template access html file
app=Flask(__name__) #this app is from procfile script1:app
@app.route('/') #this / means url or homepage. It's a deorator
def home():
    return render_template("home.html")
@app.route('/about/')
def about():
    return render_template("about.html")
if __name__ == "__main__":
     app.run(debug=True)

