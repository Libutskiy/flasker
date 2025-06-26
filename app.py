from flask import Flask, render_template, abort

app = Flask(__name__)

names = [
    "James",
    "Mary",
    "John",
    "Patricia",
    "Robert",
    "Jennifer",
    "Michael",
    "Linda",
    "William",
    "Cyril"
]

@app.route("/check_on_list/<target_name>")
def greet(target_name):
    target_name = target_name.capitalize()
    is_on_the_list = target_name.capitalize() in names
    return render_template("user.html",
                           names = names,
                           target_name = target_name,
                           is_on_the_list = is_on_the_list)

@app.errorhandler(404)
def page_not_found(e):
    error_code = 404
    error_message = "Page not found... Try again."
    page_title = "Error 404"
    return render_template("error.html",
                           error_code=error_code,
                           error_message=error_message,
                           page_title=page_title), 404

@app.errorhandler(500)
def problems_on_server(e):
    error_code = 500
    error_message = "Something is wrong on the server... Come in later!"
    page_title = "Error 500"
    return render_template("error.html",
                           error_code=error_code,
                           error_message=error_message,
                           page_title=page_title), 500


app.run(debug=1)