from flask import Flask, render_template, request
import math
app = Flask(__name__)

@app.route("/")

@app.route("/index", methods = ["GET", "POST"])

def index():

    if request.method == "POST":



        side_a = request.form.get("side_a")
        side_b = request.form.get("side_b")
        side_c = request.form.get("side_c")
        angle_a = request.form.get("angle_a")
        angle_b = request.form.get("angle_b")
        angle_c = 90

        
        submit = request.form.get("submit")
        clear = request.form.get("clear")

       


        if submit is not None:

            if side_a is not "" and side_b is not "":

                if float(side_a) > 0 and float(side_b) > 0:
                    
                    side_c = str(round((math.sqrt((float(side_a) ** 2) + (float(side_b) ** 2))),8))

                    return render_template("index.html", side_c = side_c)

            elif side_c is not "" and side_b is not "":

                if float(side_b) > 0 and float(side_c) > 0:

                    side_a = str(round((math.sqrt((float(side_c) ** 2) - (float(side_b) ** 2))),8))

                    return render_template("index.html", side_a = side_a)                 
            
            elif side_a is not "" and side_c is not "":

                if float(side_c) > 0 and float(side_a) > 0:

                    side_b = str(round((math.sqrt((float(side_c) ** 2) - (float(side_a) ** 2))),8))  

                return render_template("index.html", side_b = side_b)               



    return render_template("index.html")

if __name__ == "__main__":

    app.run(debug=True)