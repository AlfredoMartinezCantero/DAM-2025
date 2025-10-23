from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route("/")
def cv():
    with open("Curriculum.json", encoding="utf-8") as f:
        data = json.load(f)
    dp = data["datos personales"]
    
    with open("Curriculum.html", encoding="utf-8") as f:
        html = f.read()
    
    return render_template_string(html, **dp)

if __name__ == "__main__":
    app.run(debug=True)
