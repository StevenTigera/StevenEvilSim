import os
import subprocess
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def get_ping():
    return "pong"


def get_md5(filepath: str) -> str:
    md5_info = subprocess.getoutput(f"md5sum {filepath}")
    md5 = md5_info.split(" ")[0]
    return md5


def get_sha1(filepath: str) -> str:
    sha1_info = subprocess.getoutput(f"shasum {filepath}")
    sha1 = sha1_info.split(" ")[0]
    return sha1


def get_sha256(filepath: str) -> str:
    sha256_info = subprocess.getoutput(f"sha256sum {filepath}")
    sha256 = sha256_info.split(" ")[0]
    return sha256


@app.post("/bad")
def post_bad_stuff(stuff: str = "Gib money!", filepath: Optional[str] = "ransomware", relative: bool = False):
    with open(filepath, "w") as f:
        f.write("#!/bin/sh\n")
        f.write("echo 'Encrypting disk. Bip bop'\n")
        f.write("echo " + stuff)

    os.chmod(filepath, 0o764)

    md5 = get_md5(filepath)
    sha1 = get_sha1(filepath)
    sha256 = get_sha256(filepath)


    hashes = dict(md5=md5, sha1=sha1, sha256=sha256)
    if not relative:
        filepath = os.path.join(os.getcwd(), filepath)
    subprocess.Popen((filepath,), stdout=subprocess.PIPE)
    return {"hashes": hashes}