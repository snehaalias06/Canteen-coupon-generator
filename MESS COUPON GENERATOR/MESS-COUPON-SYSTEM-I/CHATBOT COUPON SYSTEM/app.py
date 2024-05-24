from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    department = data.get('department')
    meal = data.get('meal')
    preference = data.get('preference')

    return jsonify({
        "name": name,
        "department": department,
        "meal": meal,
        "preference": preference
    })

@app.route('/coupon')
def coupon():
    name = request.args.get('name')
    department = request.args.get('department')
    meal = request.args.get('meal')
    preference = request.args.get('preference')

    return render_template('coupon.html', name=name, department=department, meal=meal, preference=preference)

if __name__ == '__main__':
    app.run(debug=True)
