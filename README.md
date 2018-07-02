# globber

globber is a asynchronous logging tool.

## Installing

To install the tool just run the following command:
```bash
pip install globber
```

or

```bash
python3 -m pip install globber
```

## Example

```python

from globber.globber import Globber

log = Globber(('error', 'info'))

@log.listener
async def write_to_file(text):

```