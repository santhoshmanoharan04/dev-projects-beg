from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Pipeline using Jenkins and Docker is Working!"

@app.route("/about")
def about():
    return "This is a DevOps demo project."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)