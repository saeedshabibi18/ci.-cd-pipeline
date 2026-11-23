

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
		return """<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Hello</title>
		<style>
			body {
				min-height: 100vh;
				margin: 0;
				display: grid;
				place-items: center;
				font-family: Arial, sans-serif;
			}
			h1 { font-size: clamp(4rem, 18vw, 12rem); }
		</style>
	</head>
	<body><h1>Hello</h1></body>
</html>"""


if __name__ == "__main__":
		app.run(host="0.0.0.0", port=5000)

