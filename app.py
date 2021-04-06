from flask import Flask, request, jsonify
app = Flask(__name__)

#test get method
@app.route('/getmsg/',methods=['GET'])
def get_something():
    name = request.args.get("name",None)
    print(f"got name {name}")
    
    response = {}
    
    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

#test post method
@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    
    if param: 
        return jsonify({
            "Message":f"Welcome {name} to our awesome platform",
            "METHOD":"POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name." 
        })

#home page
@app.route('/')
def index():
	return "Welcome! this is my first Flask web page"
	
if __name__ == '__main__':
	app.run()