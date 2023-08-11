# cp-tool
CLI for creating competitive programming problem files

# Installation
Probably just clone this repo and then symlink cpt to /usr/bin or something
Also do not forget to symlink cpt-tool.py to /usr/bin or something as well

# Configuration
Copy your .cpp template to '~/.local/share/cp-tool/template.cpp'
(If you are on Windows or Mac then [install Linux](https://github.com/Amog-OS/AmogOS))

# Commands
`cpt problem <name>`
    -- creates folder with template\
`cpt contest <num_problems> <name>`
    -- creates folder with `<num_problems>` problems

# Automatic chdir
In case you do not want to manually cd to new directories created by cp-tool, run the command with `source cpt <arguments>` or alias `cpt` to `source cpt` in your shell profile

