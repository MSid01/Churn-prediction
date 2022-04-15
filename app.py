from flask import Flask, request
from flask.templating import render_template
import joblib

app = Flask(__name__)

model = joblib.load("./model_joblib")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        # get the data from the form
        data = request.form
        geolocation = int(data.get("geolocation"))
        gender = int(data.get("gender"))
        creditScore = int(data.get("credit-score"))
        age = int(data.get("age"))
        tenure = int(data.get("tenure"))
        balance = int(data.get("balance"))
        numOfProducts = int(data.get("numOfProducts"))
        hasCrCard = int(data.get("hasCrCard"))
        isActiveMember = int(data.get("isActiveMember"))
        estimatedSalary = float(data.get("estimatedSalary"))
        germany = 1 if geolocation == 2 else 0
        spain = 1 if geolocation == 1 else 0
        output = (
            model.predict(
                [
                    [
                        creditScore,
                        age,
                        tenure,
                        balance,
                        numOfProducts,
                        hasCrCard,
                        isActiveMember,
                        estimatedSalary,
                        germany,
                        spain,
                        gender,
                    ]
                ]
            ),
        )
        # print(creditScore, age, tenure, balance, numOfProducts, hasCrCard, isActiveMember, germany, spain, gender)

        # make prediction
        print(output[0][0])

        isUpToMark = output[0][0] == 1
        return "Will not leave company" if isUpToMark else "Will leave company"


if __name__ == "__main__":
    app.run(debug=True)
