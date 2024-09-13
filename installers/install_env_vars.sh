source ~/.brianward92rc
INSTALLER_DIR=$(get_script_dir)
echo $INSTALLER_DIR
"$INSTALLER_DIR/install.sh" -n DATABENTO_API_KEY
