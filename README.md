# DingPy

Author: Tina Bu (http://medium.com/@tinabu/)

**DingPy** is a Python package that plays an audio alert when your program finishes. It is particularly useful for long running batch jobs or impatient developers.

- GitHub repo: https://github.com/Tina-Bu/dingpy
- Documentation:
- PyPI: https://pypi.org/project/dingpy/
- Medium post: 

Test audio downloaded from: http://soundbible.com/2185-Old-School-Bell.html

## Contents

1. [Examples](#example)
2. [Installation](#installation)
3. [TODO](#todo)
4. [Dependencies](#dependencies)
5. [Inspirations](#inspirations)

## Examples <a name="example"></a>
```
import dingpy

# a long running block
for i in range(100):
	sleep(1)

dingpy.main()
```

## Installation <a name="installation"></a>

Tested on Python 3. **DingPy** can be installed using the following command.

```
pip install dingpy
```

## TODO <a name="todo"></a>
- package alarm_audio file into package build

## Dependencies <a name="dependencies"></a>

**DingPy**'s Python dependencies are listed in the `requirements.txt` file. 

## Inspirations <a name="inspirations"></a>

https://github.com/Shahor/dingdingdong

https://github.com/xxv/ding/



