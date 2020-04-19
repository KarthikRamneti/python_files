import cx_Freeze
import os

executables = [cx_Freeze.Executable("snake.py")]

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'


cx_Freeze.setup(name = "KatRaj",

                options = {
                    "build_exe" : {
                        "packages" : ["pygame","random"],
                        "include_files" : ["apple.png","snakehead.png"]
                    }
                },

                description = "Katraj : play carefully...",

                executables = executables

                )