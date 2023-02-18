from application import app, db
from flask import request, render_template, flash, redirect, url_for, get_flashed_messages
from application.form import UserInputForm, PredictUserInputForm
from application.models import AvgMonthlyIncome
# from application.model import get_label_encode
import pandas as pd
import numpy as np
import pickle
import json





@app.route("/")
def index():
    entries = AvgMonthlyIncome.query.order_by(AvgMonthlyIncome.timestamp.desc()).all()
    return render_template("index.html", title="index", entries = entries)

@app.route("/add", methods = ["GET", "POST"])
def add_income():
    form = UserInputForm()
    if form.validate_on_submit():
        entry =AvgMonthlyIncome(name = form.name.data, country = form.country.data, age = form.age.data,
                                email = form.email.data, address = form.address.data, phonenumber = form.phonenumber.data, 
                                gender = form.gender.data, satisfactionrate = form.satisfactionrate.data, income = form.income.data
                                ) 

        
        
        db.session.add(entry)
        db.session.commit()
        

        flash("Successful entry added!", "success")
        return redirect(url_for("index"))
    return render_template("add.html",title="add", form=form)




@app.route("/delete/<int:entry_id>")
def delete(entry_id):
    entry = AvgMonthlyIncome.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Deletion was successful!", "success")
    return redirect(url_for("index"))

@app.route("/predict", methods = ["GET", "POST"])
def predict_income():
    form = PredictUserInputForm()
    # model = pickle.load(open('model.pkl','rb'))

    # if form.validate_on_submit() and request.method == "POST":

    #     int_features = [get_label_encode(x) for x in request.form.values()]
    #     final_features = [np.array(int_features)]
    #     prediction = model.predict(final_features)

    #     output = round(prediction[0], 2)

    
    
    #     # We now pass on the input from the from and the prediction to the predict page
    #     return render_template("predict.html", title="predict", form=form, result = '$ {}'.format(output))


    return render_template("predict.html",title="predict", form=form)



@app.route("/dashboard")
def dashboard():
    male_vs_female_income = db.session.query(db.func.sum(AvgMonthlyIncome.income), AvgMonthlyIncome.gender).group_by(AvgMonthlyIncome.gender).order_by(AvgMonthlyIncome.gender).all()

    dates = db.session.query(db.func.count(AvgMonthlyIncome.id), AvgMonthlyIncome.timestamp).group_by(AvgMonthlyIncome.timestamp).order_by(AvgMonthlyIncome.timestamp).all()

    mvf_income = []

    for total_income,_ in male_vs_female_income:
        mvf_income.append(total_income)

    over_time_responses = []
    dates_labels = []

    for response,date in dates:
        over_time_responses.append(response)
        dates_labels.append(date.strftime("%d-%m-%y"))




    

    return render_template("dashboard.html", male_vs_female_income = json.dumps(mvf_income),
     over_time_responses = json.dumps(over_time_responses),
     dates_labels = json.dumps(dates_labels))