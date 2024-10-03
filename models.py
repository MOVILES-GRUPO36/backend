import uuid

class Restaurant:
    def __init__(self, id, name, latitude, longitude, photo, categories, description, rating):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude 
        self.photo = photo
        self.categories = categories
        self.description = description 
        self.rating = rating

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "photo": self.photo,
            "categories": self.categories,
            "description": self.description,
            "rating": self.rating
        }

    @staticmethod
    def from_dict(data):
        return Restaurant(
            id=str(uuid.uuid4()),  
            name=data['name'],  
            latitude=data['latitude'],
            longitude=data['longitude'],
            photo=data['photo'],
            categories=data['categories'],
            description=data['description'],
            rating=data['rating']
        )

