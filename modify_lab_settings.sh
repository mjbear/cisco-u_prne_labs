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
file="$HOME/.config/Code/User/settings.json"
array=(
    editor.fontSize
    terminal.integrated.fontSize
)
new_settings=''

# more likely to be mostly idempotent
for i in ${array[@]}
do
    grep -q $i $file
    if [ $? -eq 0 ]
    then
        sed -i -E "/.+\"$i\".+/s/[0-9]+,/$size,/" $file
    else
        new_settings="$new_settings\n    \"$i\": $size,"
    fi
done

if [ ${#new_settings} -gt 0 ]
then
    # must drop leading newline and escape first space so sed honors the
    #   leading spaces
    new_settings='\'$(echo "$new_settings" | sed -e 's/^\\n//g')
    sed -i.dist -e "/^}/i$new_settings" $file
fi

# not working due to newline in herestring
# code_font=$(cat <<EOF
#     "editor.fontSize": $size,
#     "terminal.integrated.fontSize": $size,
# EOF
# )
# sed -i.dist -e "/^}/i\\$code_font" $file

# stop gap, doesn't check for existing font settings
# sed -i.dist -e '/^}/d' $file
# cat >> $file <<EOF
#     "editor.fontSize": $size,
#     "terminal.integrated.fontSize": $size,
# }
# EOF


# set git editor
git config --global core.editor vim

# create a git alias for 'switch' if the git version is older than 2.23
git_ver=$(git --version | awk '{split($3, array, "."); print array[1] array[2]}')
if [ $git_ver -lt 223 ]; then
    git config --global alias.switch checkout
fi
