from models.engine.file_storage import FileStorage

# a unique FileStorage instance creation
storage = FileStorage()
# Call reload() method on this variable to load existing objects from the file
storage.reload()
