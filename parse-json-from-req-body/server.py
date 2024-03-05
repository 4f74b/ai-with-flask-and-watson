from data import data
from flask import Flask, request
app= Flask(__name__)

@app.route('/person', methods=['POST'])
def add_by_uuid():
    new_person=request.json
    # if failed status=422 -> Invalid input parameter
    if not new_person:
        return {"msg": "Invalid input parameter"}, 422

    # if added status=200 -> added i
    try:

        # data length before adding new person
        print("Before adding new person: ",len(data))

        # add new person
        data.append(new_person)

        # data length after adding new person
        print("After adding new person: ",len(data))

    except NameError:
        return {"msg": "data not defined"}, 500

    return {"msg": f"person with id: {new_person.get('id')} is added"}