# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('logistic_fin.pkl', 'rb'))

@app.route('/')

def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    #print("sakshi")
    try:
        if request.method ==  'POST':
            #print("sakshi")
            gender = request.form['gender']
            print(gender)
            married = request.form['married']
            dependents = request.form['dependents']
            education = request.form['education']
            employed = request.form['employed']
            credit = float(request.form['credit'])
            area = request.form['area']
            ApplicantIncome = float(request.form['ApplicantIncome'])
            CoapplicantIncome = float(request.form['CoapplicantIncome'])
            LoanAmount = float(request.form['LoanAmount'])
            Loan_Amount_Term = float(request.form['Loan_Amount_Term'])

            # gender
            if (gender == "Male"):
                gender_male=1
                gender_female=0

            else:
                gender_male=0
                gender_female=1

            # married
            if(married=="Yes"):
                married_yes = 1
                married_no = 0
            else:
                married_yes=0
                married_no = 1
            # dependents
            if(dependents=='1'):
                dependents_0 = 0
                dependents_1 = 1
                dependents_2 = 0
                dependents_3 = 0
            elif(dependents == '2'):
                dependents_0 = 0
                dependents_1 = 0
                dependents_2 = 1
                dependents_3 = 0
            elif(dependents=="3"):

                dependents_1 = 0

                dependents_2 = 0
                dependents_3 = 1
                dependents_0 = 0
            elif(dependents=="0"):
                dependents_0 = 1
                dependents_1 = 0
                dependents_2 = 0
                dependents_3 = 0
            else:
                dependents_0 = 0
                dependents_1 = 0
                dependents_2 = 0
                dependents_3 = 0

            # education
            if (education=="Not Graduate"):
                not_graduate=1
                Graduate=0
            else:
                not_graduate=0
                Graduate=1

            # employed
            if (employed == "Yes"):
                employed_yes=1
                employed_no= 0
            else:
                employed_yes=0
                employed_no= 1
            # property area

            if(area=="Semiurban"):
                semiurban=1
                urban=0
                rural=0
            elif(area=="Urban"):
                semiurban=0
                urban=1
                rural=0
            elif(area=="Rural"):
                semiurban=0
                urban=0
                rural=1
            else:
                semiurban=0
                urban=0
                rural=0

            print("sakshi")#np.array([[ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,credit,gender_female, gender_male, married_no, married_yes, dependents_3, dependents_0, dependents_1, dependents_2, Graduate, not_graduate, employed_no, employed_yes, rural, semiurban, urban ]]))
            print([ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,credit,gender_female, gender_male, married_no, married_yes, dependents_3, dependents_0, dependents_1, dependents_2, Graduate, not_graduate, employed_no, employed_yes, rural, semiurban, urban])
            prediction = model.predict(np.array([[ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,credit,gender_female, gender_male, married_no, married_yes, dependents_3, dependents_0, dependents_1, dependents_2, Graduate, not_graduate, employed_no, employed_yes, rural, semiurban, urban ]]))
            #prediction = model.predict(np.array([[Dependents_0, CoapplicantIncome, Dependents_3, Property_Area_Semiurban, Self_Employed_No, Dependents_1, Married_Yes, Property_Area_Rural, Education_Graduate, Credit_History, Gender_Female, Self_Employed_Yes, Gender_Male, ApplicantIncome, Loan_Amount_Term, Dependents_2, Married_No, Education_Not Graduate, LoanAmount, Property_Area_Urban]]))
            #print(prediction)


            if(prediction== 0):
                prediction="Not Approved :("
            else:
                prediction="Approved :)"



            return render_template("prediction.html", prediction_text="Your loan will be {}".format(prediction))


        else:
            #return render_template("prediction.html")
            return render_template("prediction.html", prediction_text="Enter your Details")
    except:
            #print("Enter Valid Fields")
            return render_template("prediction.html", prediction_text="Please Enter Valid Details")


if __name__ == "__main__":
    app.run(debug=True)
