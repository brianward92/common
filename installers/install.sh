#!/bin/bash

source ~/.brianward92rc

# Parse command line arguments for alias, script, and name
while getopts "a:s:n:" opt; do
  case $opt in
    a)
      ALIAS_NAME=$OPTARG
      ;;
    s)
      SCRIPT_PATH=$OPTARG
      ;;
    n)
      ENV_NAME=$OPTARG
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

# Prompt for value if name is provided
if [ ! -z "$ENV_NAME" ]; then
  read -p "Enter the value for $ENV_NAME: " ENV_VALUE
fi

# Get the shell configuration file
SHELL_CONFIG=$(get_shell_config)

# Check if name is set, then get value from user and add environment variable
if [ ! -z "$ENV_NAME" ]; then
  read -p "Enter the value for $ENV_NAME: " ENV_VALUE
  add_env_var_to_shell_config "$ENV_NAME" "$ENV_VALUE" "$SHELL_CONFIG"
fi

# Check if alias and script are provided and add the alias
if [ ! -z "$ALIAS_NAME" ] && [ ! -z "$SCRIPT_PATH" ]; then
  INSTALLER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  SCRIPT_PATH=$(echo "$SCRIPT_PATH" | sed "s|\$INSTALLER_DIR|$INSTALLER_DIR|g")
  add_alias_to_shell_config "$ALIAS_NAME" "$SCRIPT_PATH" "$SHELL_CONFIG"
fi

echo "Installation complete. Please run 'source $SHELL_CONFIG' to reload your shell configuration."
