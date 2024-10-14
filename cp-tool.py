import os
import re
import sys

TEMPLATE_PATH = os.path.join(os.path.expanduser('~'), '.local/share/cp-tool/template.cpp')

def main(args):
    cur_directory = os.getcwd()

    # Command for creating contest files
    if len(args) > 3 and args[1] == 'contest' and args[2].isdigit():
        new_dir = create_contest(cur_directory, int(args[2]), ' '.join(args[3:]))
        print('Contest files created.')
        print_dir(new_dir)
    # Command for creating problem files
    elif len(args) > 2 and args[1] == 'problem':
        new_dir = create_problem(cur_directory, ' '.join(args[2:]))
        print('Problem files created.')
        print_dir(new_dir)
    # Command for creating template
    elif len(args) > 2 and args[1] == 'template':
        file_path = args[2]
        add_template(cur_directory, file_path, True)
        print('Template file created')
    # Help command
    elif len(args) == 2 and args[1] == 'help':
        print_help()
    # Unknown command
    else:
        print('Invalid usage:')
        print_help()

def create_contest(directory, num_problems, name):
    # Create directory with problems: "problem1.cpp", "problem2.cpp", ...
    new_path = create_directory(directory, name)
    for i in range(1, num_problems+1):
        problem_name = 'problem' + str(i)
        add_template(new_path, problem_name)
    return new_path

def create_problem(directory, name):
    new_path = create_directory(directory, name)
    add_template(new_path, name)
    return new_path

def add_template(directory, file_name, override=False):
    # Read template file
    ensure_exists(TEMPLATE_PATH)
    template_data = ""
    with open(TEMPLATE_PATH, 'r') as f:
        template_data = f.read()

    formatted_file_name = format_name(file_name)
    new_path = os.path.join(directory, formatted_file_name) + '.cpp'

    # Write template file
    if not override:
        ensure_not_exists(new_path)
    with open(new_path, 'w') as f:
        f.write(template_data)

def print_help():
    print('cpt help')
    print('cpt problem <name>')
    print('cpt contest <num_problems> <name>')
    print('cpt template <name>')

def create_directory(directory, directory_name):
    formatted_directory_name = format_name(directory_name)
    joined_path = os.path.join(directory, formatted_directory_name)
    ensure_not_exists(joined_path)

    os.mkdir(joined_path)
    return joined_path

def format_name(name):
    # Replace spaces and remove special characters
    formatted = name.replace(' ', '_')
    formatted = re.sub(r'[^\w]', '', formatted)
    formatted = formatted.rstrip('.cpp')
    return formatted

def print_dir(dir):
    print('dir=' + dir)

def ensure_exists(path):
    if not os.path.exists(path):
        crash_with_error(f'Error: {path} does not exist')

def ensure_not_exists(path):
    if os.path.exists(path):
        crash_with_error(f'Error: {path} exists')

def crash_with_error(message):
    print(message)
    sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)
