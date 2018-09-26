from flask import render_template

from app import app, db


@app.route('/')
def login_page():
    return render_template('app/templates/template.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
