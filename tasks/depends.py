from tasks.storage import JSONStorage, Storage


def get_storage() -> Storage:
    """Return a Storage object by creating and returning a new instance of JSONStorage"""
    return JSONStorage()
