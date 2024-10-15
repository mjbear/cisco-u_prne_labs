python -c 'import privy'

pip list | grep privy

python -m pip install --upgrade pip

pip install privy

privy_cmd=$(cat <<EOF
import privy
encrypted_pw = privy.hide(b'password', b'decrypt')
print()
print(encrypted_pw)
print()
print(privy.peek(encrypted_pw, b'decrypt'))
print(privy.peek(encrypted_pw, b'decrypt').decode('utf-8'))
print()
enc = privy.hide('cisco'.encode(), 'decrypt'.encode())
print(enc)
print()
print(privy.peek(enc, 'decrypt'.encode()).decode())
EOF
)

python -c "$privy_cmd"
# could also just pipe here doc direct to python binary