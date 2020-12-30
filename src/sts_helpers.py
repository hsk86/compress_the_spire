import re

def apply_schema(df, schema):
    # Fill cols
    for key in schema:
        try:
            df[key]
        except (KeyError, TypeError) as e:
            if schema[key] == "str":
                df[key] = ""
            if schema[key] == "int64":
                df[key] = -99999

    # Fill schemas
    fill_vals = {}
    for key in schema:
        if schema[key] == "str":
            fill_vals[key] = ""
        if schema[key] == "int64":
            fill_vals[key] = -99999
        else:
            fill_vals[key] = ""

    df_proc = df.fillna(fill_vals).astype(schema)
    df_proc = df_proc[[col for col in schema]]
    return(df_proc)


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