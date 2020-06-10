from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/#thankyou')
    else:
        return 'something went wrong. try again.'


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        fieldnames = ['name', 'email', 'message']
        writer = csv.DictWriter(database, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
