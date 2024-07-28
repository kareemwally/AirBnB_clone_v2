from models.base_model import BaseModel
from models.city import City
from models import storage

class State(BaseModel):
    # ... other methods and attributes

    @property
    def cities(self):
        """Return the list of City objects from storage linked to the current State."""
        all_cities = storage.all(City)
        state_cities = [city for city in all_cities.values() if city.state_id == self.id]
        return state_cities
