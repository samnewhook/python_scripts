#!/usr/bin/python3
import glob
import os
import datetime
from subprocess import call


def get_latest_date(file_list: list) -> datetime.datetime:
    """
    Usage: Passing in a list of filenames of the format:
        FULLDAYNAME_DAY_MONTHNAME_YEAR.todo
        Wednesday_15_April_2020.todo
    will return the datetime.datetime object representing
    that date.
    """
    date_list = [date_time_from_filename(f) for f in file_list]
    return sorted(date_list)[-1]


def date_time_from_filename(file_name):
    """
    Return a datetime.datetime object from the file name with
    the format specified as:
        FULLDAYNAME_DAY_MONTHNAME_YEAR.todo
        Wednesday_15_April_2020.todo
    """
    f_name = os.path.splitext(os.path.basename(file_name))[0]
    day_month_year = f_name.split('_')
    return datetime.datetime(
            int(day_month_year[3]),
            datetime.datetime.strptime(day_month_year[2], '%B').month,
            int(day_month_year[1]))


if __name__ == "__main__":
    """
    Usage: running this file creates a new todo list based on a copy of
    the most recent todo list available.
    """
    todo_file_path_dir = os.path.join("/home", "snewhook", "todo_lists")
    todo_file_path = os.path.join(todo_file_path_dir,  "*.todo")
    todo_files = glob.glob(todo_file_path)
    today = datetime.datetime.now()
    formatting_string = '%A_%d_%B_%Y'
    today_formatted = today.strftime(formatting_string)
    latest_todo_list = get_latest_date(todo_files)
    EDITOR = os.environ.get('EDITOR', 'vim')
    latest_file_name = os.path.join(
            todo_file_path_dir,
            ''.join((latest_todo_list.strftime(formatting_string), ".todo")))
    new_file_name = os.path.join(
            todo_file_path_dir,
            ''.join((today_formatted, ".todo")))
    if datetime.datetime.now().date() == latest_todo_list.date():
        call([EDITOR, latest_file_name])
    else:
        with open(latest_file_name) as latest_file:
            with open(new_file_name, "w+") as todays_file:
                for line in latest_file:
                    todays_file.write(line)
        call([EDITOR, new_file_name])
