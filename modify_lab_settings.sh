#!/usr/bin/env bash

profiles_path='org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:'
prof=$(gsettings get org.gnome.Terminal.ProfilesList default | awk -F\' '{print $2}')
name=$(gsettings get "$profiles_path/:$prof/" visible-name)

font="'Monospace 20'"

echo -e "Setting the font for terminal profile $name to $font\n"

# gnome-terminal font size
echo -e "$profiles_path/:$prof/"
gsettings set "$profiles_path/:$prof/" use-system-font false
gsettings set "$profiles_path/:$prof/" font "$font"

echo -e "Setting the gedit font to $font\n"

# gedit editor font size
gsettings set org.gnome.gedit.preferences.editor use-default-font false
gsettings set org.gnome.gedit.preferences.editor editor-font "$font"
