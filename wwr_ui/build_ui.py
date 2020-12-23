import glob
import os
from subprocess import call

for input_path in glob.glob('*.ui'):
  base_name = os.path.splitext(input_path)[0]
  output_path = "ui_%s.py" % base_name
  
  command = [
    "pyside2-uic",
    input_path,
    "-o", output_path
  ]
  result = call(command)
