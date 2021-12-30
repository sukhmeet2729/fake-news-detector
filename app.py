from flask import Flask, escape, request, render_template
import pickle

cv = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("finalized_model.pkl", 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = request.form['news']
        predict = model.predict(cv.transform([news]))[0]
        print(predict)
        return render_template("index.html", prediction_text = "News headline is - {}".format(predict))

if __name__ == '__main__':
    app.run()