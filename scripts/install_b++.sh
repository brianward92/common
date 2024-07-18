# Determine the user's current shell
CURRENT_SHELL=$(basename "$SHELL")

# Get the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Determine the path to the b++ script
BPP_SCRIPT="/usr/bin/python3 $SCRIPT_DIR/b++.py"

# Determine the user's shell configuration file
if [ "$CURRENT_SHELL" = "zsh" ]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [ "$CURRENT_SHELL" = "bash" ]; then
    SHELL_CONFIG="$HOME/.bashrc"
else
    echo "Unsupported shell ($CURRENT_SHELL). Please run this script using either bash or zsh."
    exit 1
fi

# Create the shell configuration file if it doesn't exist
if [ ! -f "$SHELL_CONFIG" ]; then
    touch "$SHELL_CONFIG"
fi

# Check if the alias already exists
if grep -q "alias b++=" "$SHELL_CONFIG"; then
    echo "Alias b++ already exists in $SHELL_CONFIG"
else
    # Add the alias to the shell configuration file using double quotes
    echo "alias b++=\"$BPP_SCRIPT\"" >> "$SHELL_CONFIG"
    echo "Alias b++ has been added to $SHELL_CONFIG"
fi

echo "Installation complete. Please run 'source $SHELL_CONFIG' to reload your shell configuration and use the 'b++' command."
