

class NonExistentDataFileException(Exception):
    def __init__(self, fname: str):
        self.message = f"The file {fname} has not been found in the data directory! "
        super().__init__(self.message)
