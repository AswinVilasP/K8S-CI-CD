from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """<!DOCTYPE html>
    <html>
        <head>
            <title>Centered Content</title>
            <style>
                body {
                    background-color: #7879FF;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                p {
                    font-size: 50px;
                }
            </style>
        </head>
        <body>
            <p>Hi Welcome To Flask &#128512;!</p>
        </body>
    </html>"""

if __name__ == '__main__':
    app.run('0.0.0.0')


