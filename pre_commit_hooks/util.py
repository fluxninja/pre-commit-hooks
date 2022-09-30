from __future__ import annotations

from typing import Any
import hashlib
import subprocess

class CalledProcessError(RuntimeError):
    pass

def cmd_output(*cmd: str, retcode: int | None = 0, **kwargs: Any) -> str:
    """
    okcode: This parameter acts as the code where you already that you are going to get this error code
    """
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    stderr = stderr.decode()
    #Generating hash of the know error
    hash_val = hashlib.md5(stderr.encode())
    if hash_val.hexdigest() == '46cb3d2ca973ded51e63cd2a8966a41d':
        return stdout

    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout
