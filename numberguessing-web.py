from flask import Flask, request, render_template_string, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a random string

HTML = """
<!doctype html>
<title>Number Guessing Game</title>
<h1>Guess a number between 1 and 100</h1>
{% if message %}
    <p>{{ message }}</p>
{% endif %}
<form method="post">
    <input type="number" name="guess" min="1" max="100" required>
    <input type="submit" value="Guess">
</form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)
        session["attempts"] = 0

    message = ""
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            session["attempts"] += 1
            secret_number = session["secret_number"]
            if guess < secret_number:
                message = "Too low! Try again."
            elif guess > secret_number:
                message = "Too high! Try again."
            else:
                message = f"Congratulations! You guessed the number in {session['attempts']} tries."
                session.pop("secret_number")
                session.pop("attempts")
        except ValueError:
            message = "Please enter a valid number."
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(debug=True, port=5001)