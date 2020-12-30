import re

def extract_year(file_name):
    if match := re.search("(20[0-9]{2})", file_name, re.IGNORECASE):
        return(match.group(1))
    else:
        raise ValueError('No year detected on file name. Bad file somewhere in there?')


def extract_month(file_name):
    if match := re.search("20[0-9]{2}-([0-9]{2}).*", file_name, re.IGNORECASE):
        return(match.group(1))
    else:
        raise ValueError('No month detected on file name. Bad file somewhere in there?')