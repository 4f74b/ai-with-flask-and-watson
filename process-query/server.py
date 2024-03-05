from flask import Flask, request
from data import data
app=Flask(__name__)

# We can use the args dictionary inside the request object to find query (if any) 
@app.route('/first-name')
def name_search():
    query=request.args.get('q')
    
    # If no query found in the url
    if not query:
        return {"message":"Invalid input parameter"}, 422
    
    for person in data:
        if query.lower() in person['first_name'].lower():
            return person
    
    
    return {"message": f"No person with name {query} was found"}, 404
