

def read_url_file(file_name):
    lines = []
    with open(file_name) as f:
        for index, line in enumerate(f):
            lines.append(line.strip("\n"))
            print("Line {}: {}".format(index, line.strip()))

    return lines

