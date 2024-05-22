from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        with open("Scores.txt", "r") as returnscore:
            finalscore = returnscore.read()
            return f"<html>\n<head>\n<title>Scores Game</title>\n</head>\n<body>\n<h1>The score is <div id=\"score\">{finalscore}</div></h1>\n</body>\n</html>"
    except Exception as error:
        return f"<html>\n<head>\n<title>Scores Game</title>\n</head>\n<body>\n<body>\n<h1><div id=\"score\" style=\"color:red\">{type(error).__name__}</div></h1>\n</body>\n</html>"

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8777)