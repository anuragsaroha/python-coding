class BadVersion:
    def __init__(self, b):
        self.bad = b

    def is_bad_version(self, version):
        return version >= self.bad
