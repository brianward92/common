import os, sys

if __name__ == "__main__":
    script_name = sys.argv[1]
    program_name = script_name.replace(".cpp", "")
    if not os.path.exists("./bin"):
        os.makedirs("./bin")
    os.system("g++ {} -o bin/{}".format(script_name, program_name))
