import json
from models.base_model import BaseModel
# ... other imports

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    # ... other methods

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

    def close(self):
        """Call the reload method."""
        self.reload()
