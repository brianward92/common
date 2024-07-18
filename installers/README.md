# Installers

## `install_b++.sh` to Install `b++`

This code provides a shorthand tool for compiling `C++` code`. It works like this
```linux
bward92@MacBook-Pro-5 ~ % b++ tmp/main.cpp
```
it then generates a binary in `bin/` to with the executable that takes the `.cpp` file name and removes the file extension.
In this case there will be an executable at `tmp/bin/main` that can be run directly.

To get access to this tool use the installer in `/PATH/TO/common/installers/install_b++.sh`. Doing so will check the user `~/.<SHELL>rc` file for an alias `b++`. If it finds one it will not overwrite it. In that case, remove it and re-run the installer. After that the user needs to open a new shell or explicitly source the config file. The command to do so is given to the user for convenience. E.g.
```linux
(base) bward92@MacBook-Pro-5 ~ % ./src/common/installers/install_b++.sh 
Alias b++ has been added to /Users/bward92/.zshrc
Installation complete. Please run 'source /Users/bward92/.zshrc' to reload your shell configuration and use the 'b++' command.
(base) bward92@MacBook-Pro-5 ~ % type b++
b++ not found
(base) bward92@MacBook-Pro-5 ~ % source ~/.zshrc
(base) bward92@MacBook-Pro-5 ~ % type b++
b++ is an alias for /usr/bin/python3 /Users/bward92/src/common/installers/../common/cpp/b++.py
(base) bward92@MacBook-Pro-5 ~ % 
```

The actual command is going to run a `python` script that only relies on `STL` from `python=3.8.2`, no third party libraries are necessary. That tool just takes the input path and manipulates it to call `g++` and fix the `-o` argument to this `bin/` sub-directory of where the `main.cpp` script lives.
