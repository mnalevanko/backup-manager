# this defines some criteria for file searching, and defines the blueprint for custom-made modules (or criteria)

from os import path

class BaseCriteria:
    def __init__(self, files, dir):
        """
        Give a list of (filename, subpath) and the main dir's path,
        filters the results into self.results
        :param files: list of (filename, subpath)
        :param dir: the main dir'a path
        """
        self.results = self.filter(self, files, dir)

    def __call__(self):
        return self.results

class ExtensionFilter(BaseCriteria):
    def __init__(self, files, dir, allowed_extensions):
        self.allowed_extensions = allowed_extensions
        super().__init__(self, files, dir)

    def filter(self, files, dir):
        results = []
        for file, subpath in files:
            if path.splitext(file)[1] in self.allowed_extensions:
                results.append( (file, subpath) )
        return results
