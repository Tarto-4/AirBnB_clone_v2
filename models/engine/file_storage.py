import json

class FileStorage:
    # ... (Other class attributes and methods remain the same)

    def delete(self, obj=None):
        """Deletes an object from the storage (if it exists)."""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None)  # Safely remove if present
            self.save()  # Persist the changes to the JSON file

    def all(self, cls=None):
        """Returns a dictionary of objects in storage, filtered by class (optional)."""
        if cls is None:
            return FileStorage.__objects  # Return all objects
        else:
            class_objects = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    class_objects[key] = obj
            return class_objects 
