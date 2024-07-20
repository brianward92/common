source ~/.brianward92rc
INSTALLER_DIR=$(get_script_dir)
echo $INSTALLER_DIR
"$INSTALLER_DIR/install.sh" -a fs -s "/usr/bin/osascript $INSTALLER_DIR/../common/applescript/fs.applescript"
