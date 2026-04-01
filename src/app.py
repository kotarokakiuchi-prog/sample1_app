from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def calc_det(matrix):
    arr = np.array(matrix, dtype=int)
    return np.linalg.det(arr)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        matrix_text = request.form["matrix"]

        # 行列文字列 → 配列変換
        rows = matrix_text.strip().split("\n")
        matrix = [row.split() for row in rows]

        result = calc_det(matrix)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)