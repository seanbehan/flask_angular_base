from flask import Flask, render_template as render, jsonify, request

app = Flask(__name__, static_url_path='')

@app.route('/users.json')
def users():
    return jsonify(
        users = [
            { 'name' : 'sean' },
            { 'name' : 'bob' },
            { 'name' : 'jamie' }
        ]
    )

@app.route('/users.json', methods=['POST'])
def add_user():
    return jsonify(request.json['user'])

@app.route('/')
def home():
    return render('home.html')

if __name__=='__main__':
    app.run(debug=True)
