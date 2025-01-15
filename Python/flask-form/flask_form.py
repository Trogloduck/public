"""
Flask contact form, sanitizing and validating user input, and sending feedback to the user.
Each field of the form has specific requirements, such as the email field must contain an '@' symbol.
Error messages are displayed to the user if the input does not meet the requirements, next to the field that needs to be corrected.
"""

from flask import Flask, render_template, request
import regex as re


app = Flask(__name__)

# route to contact form
@app.route("/contact-form")
@app.route("/")
def form_page():
    return render_template("form.html")

# regex to check if email is valid
def is_email_valid(email:str):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

# regex to check if first_name, last_name is valid, preventing XSS attacks
def is_name_valid(name:str):
    if re.match(r"^[A-Za-z\s-]+$", name):
        return True
    return False

# regex to check if message is valid, preventing XSS attacks
def is_message_valid(message:str):
    if re.match(r"^[A-Za-z0-9\s\.,!?]+$", message):
        return True
    return False

# route to nicetry page
@app.route("/nicetry")
def nicetry_page():
    return render_template("nicetry.html")

# route to submit form
@app.route("/submit", methods=["POST"])
def submit_page():
    # Get the values from the form
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    region = request.form.get("region")
    subject = request.form.get("subject")
    message = request.form.get("message")
    fake_field = request.form.get("fake_field")

    # Check each field fits its requirements and displays error message if not
    if not is_name_valid(first_name):
        return render_template("form.html", first_name_error_message="Your first name can only contain letters, spaces and/or hyphens.")
    if not is_name_valid(last_name):
        return render_template("form.html", last_name_error_message="Your last name can only contain letters, spaces and/or hyphens.")
    if not is_email_valid(email):
        return render_template("form.html", email_error_message="Please enter a valid email address.")
    if not region:
        return render_template("form.html", region_error_message="Please select a region.")
    if not subject:
        return render_template("form.html", subject_error_message="Please select a subject.")
    if not is_message_valid(message):
        return render_template("form.html", message_error_message="Your message can only contain letters, numbers, spaces and/or punctuation.")

    # Check if the fake field is empty
    if fake_field:
        return render_template("nicetry.html")
    
    return render_template(
        "submit.html",
        first_name=request.form["first_name"],
        last_name=request.form["last_name"],
        email=request.form["email"],
        region=request.form["region"],
        subject=request.form["subject"],
        message=request.form["message"]
    )

# run app in debug mode
if __name__ == "__main__":
    app.run(debug=True)