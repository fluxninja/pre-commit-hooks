from __future__ import annotations

import subprocess
from typing import Any


class CalledProcessError(RuntimeError):
    pass

def cmd_output(*cmd: str, retcode: int | None = 0,okcode:int= 0, **kwargs: Any) -> str:
    """
    okcode: This parameter acts as the code where you already that you are going to get this error code
    """
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and (proc.returncode != retcode or proc.returncode  == okcode ):
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout
