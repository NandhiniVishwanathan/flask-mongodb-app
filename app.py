from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    display = ""

    if request.method == "POST":
        display = request.form.get("display", "")
        button = request.form.get("button")

        try:
            if button == "AC":
                display = ""

            elif button == "DEL":
                display = display[:-1]

            elif button == "=":
                if display:
                    display = str(eval(
                        display,
                        {"__builtins__": None},
                        {"sqrt": math.sqrt}
                    ))

            elif button == "√":
                if display:
                    display = f"sqrt({display})"

            elif button == "%":
                if display:
                    display = str(float(display) / 100)

            else:
                display += button

        except:
            display = "Error"

    return render_template("index.html", display=display)

if __name__ == "__main__":
    app.run(debug=True)
