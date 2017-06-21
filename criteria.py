# this defines some criteria for file searching, and defines the blueprint for custom-made modules (or criteria)

from os import path

class BaseCriteria:
    def __init__(self, files):
        """
        Give a list of (filename, subpath)
        filters the results into self.results
        :param files: list of (filename, subpath)
        """
        self.results = self.filter(files)

    def __call__(self):
        return self.results

class ExtensionFilter(BaseCriteria):
    def __init__(self, files, allowed_extensions):
        self.allowed_extensions = allowed_extensions
        super().__init__(files)

    def filter(self, files):
        results = []
        for file, subpath in files:
            if path.splitext(file)[1] in self.allowed_extensions:
                results.append( (file, subpath) )
        return results
