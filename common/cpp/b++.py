import os, sys

if __name__ == "__main__":
    script_file = os.path.abspath(os.path.expanduser(sys.argv[1]))
    code_dir, script_name = os.path.split(script_file)
    program_name = script_name.replace(".cpp", "")
    bin_dir = os.path.join(code_dir, "bin")
    program_file = os.path.join(bin_dir, program_name)
    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir)
    os.system("g++ {} -o {}".format(script_file, program_file))
