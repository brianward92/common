source ~/.commonrc
INSTALLER_DIR=$(get_script_dir)
echo $INSTALLER_DIR
"$INSTALLER_DIR/install.sh" -a oj -s "/usr/bin/python3 $INSTALLER_DIR/../common/writing/oj.py"
