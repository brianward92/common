# Scripts

## `b++.py`

Runs with only `STL` from `python=3.8.2` and does not need third party libraries.

It is a `C++` compilation helper to compile `<PROGRAM>.cpp` and redirect the binary to `bin/<PROGRAM>`.

It is kicked off by `/PATH/TO/common/common/cpp/b++` command.

### `install_b++.sh` to Install `b++`

This code provides a shorthand tool for compiling `C++` code. `It works like this
```linux
bward92@MacBook-Pro-5 ~ % b++ main.cpp
```
it then generates a binary in `bin/` to with the executable that takes the `.cpp` file name and removes the file extension.

To get this `b++` alias to the correct location, from `/PATH/TO/common/scripts` run `./install_b++.sh`. Be mindful of your default shell, it will add this alias to your `~/.bashrc` or `~/.zshrc` depending on that. If you already have added it manually or done this step before, it will do nothing.
