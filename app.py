from flask import Flask, request, jsonify

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/bfhl', methods=['POST'])
def process_data():
    incoming_data = request.get_json()
    data_array = incoming_data.get("data", [])
    
    numbers = []
    alphabets = []
    
    for item in data_array:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            
    response = {
        "is_success": True,
        "user_id": "shanu_khandala_31072004",
        "email": "shanukhandala230686@acropolis.in",
        "roll_number": "0827ci231122",
        "numbers": numbers,
        "alphabets": alphabets
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
