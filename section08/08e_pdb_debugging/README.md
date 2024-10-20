# pdb debugging

## Overview

pdb is Python's built-in debugger

## Invoking

Three methods to invoke pdb
1. Invoke as a script
1. Invoke in the interpreter (REPL)
1. Invoke within code

### Invoke as a Script

```bash
python -m pdb <name of script>
```

### Invoke in the Interpreter (REPL)

```python
>>> import pdb
>>> pdb.run('script name')
```

### Invoke within Code

#### Python 3.7 and later

As of Python 3.7, it is possible to simply specify a breakpoint() and pdb will
automatically be loaded.

Place the breakpoint at the point where the code should stop and activate the
debugger.

```python
breakpoint()
```

Then finally run the code. `python <name of script>`

#### Earlier than Python 3.7

Prior to Python 3.7, it was necessary to import pdb and set a trace.

Place the trace at the point the code should stop for debugging.

```python
import pdb; pdb.set_trace()
```

Then finally run the code. `python <name of script>`

## Using pdb

### pdb help

`(Pdb) help`

`(Pdb) help pdb`

Another example, `(Pdb) help break`

### Common pdb Command Reference

| Command | Description |
| :-----: | :----------- |
| c       | Continue
| s       | Step Forward (into the next layer of code)
| n       | Next (does not step into, but instead runs a function)
| b       | Breakpoint (ex: `b <line_num>`)
| p       | Print (ex: `p <variable_name>`)
| pp      | Pretty Print
| !       | Execute Statement (ex: `!x = 10`)
| l       | List Source
| ll      | Long List
| w       | Print Stack
| q       | Quit (otherwise use `Ctrl+d` or `exit()` to quit pdb)
| u       | Up (move up in the stack trace)
| d       | Down (move down in the stack trace)

[:sparkles: Debugger Commands](https://docs.python.org/3/library/pdb.html#debugger-commands)

![pdb command diagram](08e_pdb_debugging/pdb_command_diagram.png)
