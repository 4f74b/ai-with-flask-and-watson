# An important part of back-end programming is creating APIs. An API is a contract between a provider and a user. It is common to create RESTful APIs that can be called by the front end or other clients. In a REST based API, the resource information is sent as part of the request URL. For example, with your resource or persons, the client can send the following request:

# GET http://localhost/person/unique_identifier
# This request asks for a person with a unique identifier. 

# Another example is:

# DELETE http://localhost/person/unique_identifier
# In this case, the client asks to delete the person with this unique identifier.


# In this file I will create a simple GET route that returns the number of entries in 'data' array and another DELETE route to delete an item 


from flask import Flask
app=Flask(__name__)

from data import data


# route to GET length of all data
@app.route('/count', methods=['GET'])
def get_count():
    if (data and len(data)):
        return {"length": len(data)}, 200
    
    return {'message': 'Data is not loaded'}, 404


# GET person by uuid
@app.route('/person/<id>', methods=['GET'])
def find_by_uuid(id):
    for person in data:
        if id==person.get('id'):
            return person, 200    
    
    return {"message": f"person with id: {id} is not found"}, 404

# DELETE person by id route
@app.route('/person/<id>', methods=['DELETE'])
def find_by_uuid_and_delete(id):
    # use request object to access id of person to be deleted
    
    for person in data:
        if id==person.get('id'):
            # length of array before deletion
            print(len(data))

            data.remove(person)

            #length of array after deletion 
            print(len(data))
            
            return {"message": f"person {person.get('first_name')} with id: {id} is deleted"}, 200
        
    return {"message": f"no person with id: {id} is found"},404