from sqlalchemy.orm import sessionmaker, scoped_session
# ... other imports

class DBStorage:
    __engine = None
    __session = None

    # ... other methods

    def close(self):
        """Call remove() method on the private session attribute."""
        self.__session.remove()
