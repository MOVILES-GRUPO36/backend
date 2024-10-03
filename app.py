from flask import Flask, jsonify, request
import json
from models import Restaurant

app = Flask(__name__)

def load_data():
    with open('/home/srdsktp/Documents/moviles/backend/data,json', 'r') as file:
        rests_data = json.load(file)
        return [Restaurant.from_dict(rest) for rest in rests_data]

def save_data(rests):
    with open('data.json', 'w') as file:
        json.dump([rest.to_dict() for rest in rests], file, indent=4)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    rests = load_data()
    return jsonify([rest.to_dict() for rest in rests])

@app.route('/api/restaurants', methods=['POST'])
def add_restaurant():
    rests = load_data()
    newRestData = request.json

    newRest = Restaurant(id=len(rests) + 1,
                        name=newRest['name'],
                        latitude=newRest['latitude'],
                        longitude=newRest['longitude'],
                        photo=newRest['longitude'],
                        categories=newRest['categories'],
                        description=newRest['description'],
                        rating=newRest['rating'])
    
    rests.append(newRest)
    save_data(rests)
    return jsonify(newRest.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
