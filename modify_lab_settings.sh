#!/usr/bin/env bash

profiles_path='org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:'
prof=$(gsettings get org.gnome.Terminal.ProfilesList default | awk -F\' '{print $2}')
name=$(gsettings get "$profiles_path/:$prof/" visible-name)

size=20
font="'Monospace $size'"

# echo -e "$profiles_path/:$prof/"

# gnome-terminal font size
echo -e "Setting the font for terminal profile $name to $font\n"
gsettings set "$profiles_path/:$prof/" use-system-font false
gsettings set "$profiles_path/:$prof/" font "$font"


# gedit editor font size
echo -e "Setting the gedit font to $font\n"
gsettings set org.gnome.gedit.preferences.editor use-default-font false
gsettings set org.gnome.gedit.preferences.editor editor-font "$font"


# vscode editor and terminal font size
echo -e "Setting VS Code editor and terminal font size\n"
# code_font=$(cat <<EOF
#     "editor.fontSize": $size,
#     "terminal.integrated.fontSize": $size,
# }
# EOF
# )
# sed -i.dist -e "s/^}/$code_font/" ~/.config/Code/User/settings.json

# stop gap
sed -i.dist -e '/^}/d' ~/.config/Code/User/settings.json
cat >> ~/.config/Code/User/settings.json <<EOF
    "editor.fontSize": $size,
    "terminal.integrated.fontSize": $size,
}
EOF


# set git editor
git config --global core.editor vim

# create a git alias for 'switch' if the git version is older than 2.23
git_ver=$(git --version | awk '{split($3, array, "."); print array[1] array[2]}')
if [ $git_ver -lt 223 ]; then
    git config --global alias.switch checkout
fi
