import re
import sys
import os

TEMPLATE_PATH = os.path.join(os.path.expanduser('~'), '.local/share/cp-tool/template.cpp')

def format_name(name):
    formatted = name.replace(' ', '_')
    formatted = re.sub(r'[^\w]', '', formatted)
    return formatted

def check_exists(directory):
    if os.path.exists(directory):
        print('Error: file exists')
        sys.exit(1)

def add_template(directory, file_name):
    template_data = ""
    with open(TEMPLATE_PATH, 'r') as f:
        template_data = f.read()

    formatted_file_name = format_name(file_name)
    new_path = os.path.join(directory, formatted_file_name) + '.cpp'
    check_exists(new_path)

    with open(new_path, 'w') as f:
        f.write(template_data)


def create_directory(directory, directory_name):
    formatted_directory_name = format_name(directory_name)
    joined_path = os.path.join(directory, formatted_directory_name)
    check_exists(joined_path)

    os.mkdir(joined_path)
    return joined_path

def create_problem(directory, name):
    new_path = create_directory(directory, name)
    add_template(new_path, name)
    return new_path

def create_contest(directory, num_problems, name):
    new_path = create_directory(directory, name)
    for i in range(1, num_problems+1):
        problem_name = 'problem' + str(i)
        add_template(new_path, problem_name)
    return new_path

cur_directory = os.getcwd()

if len(sys.argv) > 3 and sys.argv[1] == 'contest' and sys.argv[2].isdigit():
    new_dir = create_contest(cur_directory, int(sys.argv[2]), ' '.join(sys.argv[3:]))
    print('Contest files created.')
    print('dir=' + new_dir)
elif len(sys.argv) > 2 and sys.argv[1] == 'problem':
    new_dir = create_problem(cur_directory, ' '.join(sys.argv[2:]))
    print('Problem files created.')
    print('dir=' + new_dir)
else:
    print('Invalid usage:')
    print('cpt problem <name>')
    print('cpt contest <num_problems> <name>')

