from flask import Flask, jsonify, request

flaskapp = Flask(__name__)

contacts =[
        {
            "Contact": "9987644456",
            "Name": "Raju",
            "done": False,
            "id": 1
        },
        {
            "Contact": "9876543222",
            "Name": "Rahul",
            "done": False,
            "id": 2

        }
    
]

        

@flaskapp.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

contact = {
    'id': contacts[-1]['id'] + 1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact',""),
    'done': False
}
    

@flaskapp.route("/get-data")
def get_contact():
    return jsonify({
        "data":contacts
    })

if (__name__ == "__main__"):
    flaskapp.run()