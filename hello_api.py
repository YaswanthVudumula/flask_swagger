
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def get_root():
    print('sending root')
    return render_template('index.html')

@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')


@app.route('/api')
def get_api():
    hello_dict = {'en': 'Hello', 'es': 'Hola'}
    lang = request.args.get('lang')
    return jsonify(hello_dict[lang])


app.run(host='0.0.0.0',threaded=True,use_reloader=True, debug=False,port=5000 )
