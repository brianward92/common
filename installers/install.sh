#!/bin/bash

source ~/.brianward92rc

# Parse command line arguments for alias and script
while getopts "a:s:" opt; do
  case $opt in
    a)
      ALIAS_NAME=$OPTARG
      ;;
    s)
      SCRIPT_PATH=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

# Check if both alias and script arguments are provided
if [ -z "$ALIAS_NAME" ] || [ -z "$SCRIPT_PATH" ]; then
  echo "Usage: $0 -a alias_name -s script_path"
  exit 1
fi

# Get the directory of the current script
INSTALLER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH=$(echo "$SCRIPT_PATH" | sed "s|\$INSTALLER_DIR|$INSTALLER_DIR|g")

# Determine the shell configuration file
SHELL_CONFIG=$(get_shell_config)

# Add the alias to the shell configuration file
add_alias_to_shell_config "$ALIAS_NAME" "$SCRIPT_PATH" "$SHELL_CONFIG"

echo "Installation complete. Please run 'source $SHELL_CONFIG' to reload your shell configuration and use the '$ALIAS_NAME' command."

