import datetime, re

LOG_FILE_NAME = "mylog.log"


def parse_log_file():
    log_content = read_file(LOG_FILE_NAME)
    files_from_log = parse_files_from_log(log_content)
    return files_from_log


def parse_files_from_log(log_content):
    files_from_log = []

    for line in log_content:
        if line_is_a_file(line):
            date_time = parse_date_from_line(line)
            file_details = parse_filepath_from_line(line)

            file = {
                "date_time": date_time,
                "name": file_details["name"],
                "extension": file_details["extension"],
                "path": file_details["full_path"],
            }

            files_from_log.append(file)

    return files_from_log


def parse_date_from_line(line):
    regex = re.compile(r"\d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}")
    date_time = regex.search(line).group()
    date_time = datetime.datetime.strptime(date_time, "%Y/%m/%d %H:%M:%S")
    return date_time


def parse_filepath_from_line(line):
    line = remove_line_break_from_line(line)
    full_path = line.split("+ ")[1]
    name = full_path.split("/")[-1].rsplit(".", 1)[0]
    extension = full_path.split(".")[-1]
    return {"full_path": full_path, "name": name, "extension": extension}


def line_is_a_file(line):
    return "+++ " in line and "." in line


def remove_line_break_from_line(line):
    return line.replace("\n", "")


def read_file(file):
    with open(LOG_FILE_NAME) as log_file:
        return log_file.readlines()