import hashlib


class HashGenerator:

    @classmethod
    def generate_sha256(cls, string):
        return hashlib.sha256(string.encode('utf-8')).hexdigest()

    @classmethod
    def generate_md5(cls, string):
        return hashlib.md5(string.encode('utf-8')).hexdigest()
