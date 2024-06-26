#!/usr/bin/env python3

import os
import subprocess
import contextlib
from setuptools import setup, Extension
from glob import glob
from exo_build_ext import cmake_build_ext


# Config
build_dir = os.path.join(os.getcwd(), "build")
env = dict(os.environ)
env["JOBS"] = str(os.cpu_count())
env["MPI"] = "NO"
subprocess.check_call(['./install-tpl.sh'], env=env)
with contextlib.suppress(Exception):
      os.mkdir("build")
subprocess.check_call(['../cmake-exodus'], cwd=build_dir, env=env)

s = setup(name='seacas-exodus',
      description='A python wrapper of the exodus library',
      version='1.21.1',
      url='https://github.com/sandialabs/seacas',
      py_modules=['exodus3', 'exomerge3'],
      package_dir={"":"build/packages/seacas/scripts"},
      cmdclass = {'build_ext': cmake_build_ext},
      ext_modules = [Extension("exodus", [""])]
)

wheels = os.listdir("dist")
platform = "linux_x86_64"
subprocess.run(["python", "-m", "pip", "install", "--user", "auditwheel", "patchelf>=0.14"])
for wheel in [x for x in wheels if x.endswith(".whl")]:
      subprocess.run(["python", "-m", "auditwheel", "repair", "--plat", platform, f"dist/{wheel}"])
