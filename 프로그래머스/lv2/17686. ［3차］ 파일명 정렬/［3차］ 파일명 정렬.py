import re

def solution(files):
    def file_key(file):
        head, number, _ = re.match(r"([a-zA-Z\s\.\-]+)(\d{1,5})(.*)", file).groups()
        return (head.lower(), int(number))

    return sorted(files, key=file_key)
