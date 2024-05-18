"""
    This module initialize the model module
    and set storage variable for our input and
    output opération on file.json
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
