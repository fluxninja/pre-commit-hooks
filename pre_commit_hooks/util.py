from __future__ import annotations

from typing import Any
import hashlib
import subprocess
import os

class CalledProcessError(RuntimeError):
    pass

know_error_hash = {
    'e6e2dc17c307997f8c64e381a5088efe' : 'Error: config compilation contains errors: [{All Workflows have been filtered from this Pipeline.} {No Jobs have been run.}]'
}

def cmd_output(*cmd: str, retcode: int | None = 0, **kwargs: Any) -> str:
    """
    cmd: The command to run
    retcode: This parameter acts as the code where you already that you are going to get this error code

    Note: We will skip the error for the know error hash
    """
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    stderr = stderr.decode()
    #Generating hash of the know error
    hash_val = hashlib.md5(stderr.encode())
    if hash_val.hexdigest() in know_error_hash:
        return stdout

    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout
