import bottle

app = application = bottle.Bottle()

@app.route('/hello')
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(port=8080, debug=True)