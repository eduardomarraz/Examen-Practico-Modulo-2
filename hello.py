from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'<h1>Hello, {name}!</h1>'
    return render_template('form2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
