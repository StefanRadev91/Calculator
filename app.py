from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    N1 = int(request.form['N1'])
    N2 = int(request.form['N2'])
    operator = request.form['operator']

    result = 0
    sum_type = ""
    remainder = 0

    if operator == "+":
        result = N1 + N2
    elif operator == "-":
        result = N1 - N2
    elif operator == "*":
        result = N1 * N2
    elif operator == "/":
        if N2 == 0:
            return render_template('result.html', message=f"Cannot divide {N1} by zero")
        result = N1 / N2
        return render_template('result.html', message=f"{N1} / {N2} = {result:.2f}")
    elif operator == "%":
        if N2 == 0:
            return render_template('result.html', message=f"Cannot divide {N1} by zero")
        remainder = N1 % N2
        return render_template('result.html', message=f"{N1} % {N2} = {remainder}")

    if result % 2 == 0:
        sum_type = "even"
    else:
        sum_type = "odd"

    return render_template('result.html', message=f"{N1} {operator} {N2} = {result} - {sum_type}")

if __name__ == '__main__':
    app.run(debug=True)