from flask import Flask

app = Flask(__name__)

@app.route("/satellites")
def satellites():
    return {"satellites": ["satellite1", "satellite2", "satellite3"]}

if __name__ == "__main__":
    app.run(debug=True)
