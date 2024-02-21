import sys
import glob
import importlib
import logging
from pathlib import Path
from sys import argv
from Rudra import *
from Rudra import Rudra1, Rudra2, Rudra3, Rudra4, Rudra5

def load_plugs(plugname):
    modules = Path(f"Rudra/plugins/{plugname}.py")
    myfiles = f"Rudra.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["Rudra.plugins." + plugname] = load
    print("RudraSpamBot - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "Rudra/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import Rudra
import Rudra.userNeeds
import Rudra.help
import Rudra.helpers.callbackQuery

print("\n\nRudra Spam Bot Deployed Successfully!\n\n")

if len(argv) not in (1, 3, 4):
    try:
        Rudra1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Rudra2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Rudra3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Rudra4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        Rudra5.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        Rudra1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Rudra2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Rudra3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Rudra4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        Rudra5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass