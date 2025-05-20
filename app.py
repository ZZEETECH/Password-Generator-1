from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_characters=True):
    # Define the character sets based on user preferences
    lowercase_letters = string.ascii_lowercase if use_lowercase else ''
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special_characters else ''

    # Combine the character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 12 characters
    length = max(length, 12)

    # Generate the password randomly
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password_length = int(request.form["password_length"])
        use_lowercase = "use_lowercase" in request.form
        use_uppercase = "use_uppercase" in request.form
        use_digits = "use_digits" in request.form
        use_special_characters = "use_special_characters" in request.form

        generated_password = generate_password(
            length=password_length,
            use_lowercase=use_lowercase,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_special_characters=use_special_characters,
        )
        return render_template("result.html", password=generated_password)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    