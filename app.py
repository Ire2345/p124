from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
     { 
        'id': 1,
         'title': u'Buy groceries',
          'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
           'done': False 
           },
            { 
                'id': 2,
                 'title': u'Learn Python',
                  'description': u'Need to find a good Python tutorial on the web',
                   'done': False 
                   }
                    ]
@app.route("/get-data")
def gettask():
    return jsonify({
        "data":tasks
    })

@app.route("/")
def helloworld():
    return "helloworld"

if __name__ == "__main__":
    app.run()
