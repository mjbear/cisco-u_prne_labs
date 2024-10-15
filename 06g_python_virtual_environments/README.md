There's not actually a lab for this, but it's handy

If done just from the Python REPL...
```python
import site
print(site.getsitepackages())
```

Otherwise pipe code into Python
```bash
python <<EOF
import site
print(site.getsitepackages())
EOF
```

Create and work with a Python virtual environment (venv)
```bash
python -m venv ProjectB

# MSFT Windows
ProjectB\Scripts\activate

# GNU/Linux
source ProjectB/bin/activate

pip list

pip freeze > requirements.txt

pip install -r requirements.txt

deactivate
```
