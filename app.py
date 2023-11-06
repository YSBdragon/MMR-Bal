from flask import Flask, request, render_template

app = Flask(__name__)

# Create an empty list to store form data
data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        mmr = request.form['mmr']

        # Add data to the list
        data.append({'Name': name, 'MMR': mmr})

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
