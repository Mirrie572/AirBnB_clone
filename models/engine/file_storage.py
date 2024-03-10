import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj_dict['__class__'] = class_name
                    if class_name == 'BaseModel':
                        from models.base_model import BaseModel
                        obj = BaseModel(**obj_dict)
                    elif class_name == 'User':
                        from models.user import User
                        obj = User(**obj_dict)
                    else:
                        continue
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
