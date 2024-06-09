from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_operation():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':
            r = num1 + num2
            result = f'The sum of {num1} and {num2} is {r}'
        elif operation == 'subtract':
            r = num1 - num2
            result = f'The difference between {num1} and {num2} is {r}'
        elif operation == 'multiply':
            r = num1 * num2
            result = f'The product of {num1} and {num2} is {r}'
        elif operation == 'divide':
            if num2 != 0:
                r = num1 / num2
                result = f'The quotient when {num1} is divided by {num2} is {r}'
            else:
                result = 'Division by zero is not allowed'
        else:
            result = 'Invalid operation'

        return render_template('results.html', result=result)

@app.route('/via_postman', methods=['POST'])
def math_operation_via_postman():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == 'add':
            r = num1 + num2
            result = f'The sum of {num1} and {num2} is {r}'
        elif operation == 'subtract':
            r = num1 - num2
            result = f'The difference between {num1} and {num2} is {r}'
        elif operation == 'multiply':
            r = num1 * num2
            result = f'The product of {num1} and {num2} is {r}'
        elif operation == 'divide':
            if num2 != 0:
                r = num1 / num2
                result = f'The quotient when {num1} is divided by {num2} is {r}'
            else:
                result = 'Division by zero is not allowed'
        else:
            result = 'Invalid operation'

        return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
