source ~/.brianward92rc
INSTALLER_DIR=$(get_script_dir)
echo $INSTALLER_DIR
"$INSTALLER_DIR/install.sh" -a b++ -s "/usr/bin/python3 $INSTALLER_DIR/../common/cpp/b++.py"
