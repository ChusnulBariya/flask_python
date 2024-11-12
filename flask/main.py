from flask import Flask

app = Flask(__name__)

# 1 Router 1 Fungsi
@app.route('/')
def hello():
    return 'Hello Bariya'

@app.route('/aboutme/<nama>')
def aboutme_nama(nama):
    return 'about me, its me' .format(nama)

if __name__ == '__main__':
    app.run(debug=True) # Method Run