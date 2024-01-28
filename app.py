from flask import Flask, redirect, url_for, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/visit-counter")
def increment_cookie():
    cookie_count = request.cookies.get('cookie_count')
    if cookie_count is None:
        cookie_count = 0
    else:
        cookie_count = int(cookie_count)

    cookie_count += 1

    response = make_response(render_template('index.html', cookie_count=cookie_count))
    response.set_cookie('cookie_count', str(cookie_count), max_age=3600)

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)