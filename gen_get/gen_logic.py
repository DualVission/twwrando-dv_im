import os
from collections import OrderedDict

import yaml

from class_ms import YamlOrderedDictLoader
from paths import LOGIC_PATH, TRICK_PATH, TYPE_PATH

forbidden_keys = ["Paths","Original item","Mode"]
path_input = LOGIC_PATH
path_output = TYPE_PATH
source_file = "item_locations.txt"
file_details = ["LagoLunatic","Standard","The regular TWW Logic","standard.dv_im"]
format_title = '<inject Creator="{}" Type="{}" Description="{}" Change="{}" File="{}" Chechsum="{}">\n'


with open(os.path.join(path_input, source_file)) as f:
  item_locations = yaml.load(f, YamlOrderedDictLoader)

final_locations = ''
change=0
for location in item_locations:
  add_text = f' Name="{location}"'
  change+=1
  try:
    mode = item_locations[location]["Mode"]
    add_text = add_text+(' Mode="{}"').format(mode)
  except:
    add_text = add_text+(' {}="{}"').format("Mode","o")
  for key, value in item_locations[location].items():
    if(key in forbidden_keys):
      continue
    if(key=="Need" or key=="Gltiches"):
      splitStr = value.split('"')
      result = "'".join(splitStr)
      splitStr = result.split('&')
      result = "AND".join(splitStr)
      splitStr = result.split('|')
      result = "OR".join(splitStr)
      value = result
    add_text = add_text+(' {}="{}"').format(key,value)
  final_locations+=f'  <check{add_text}/>\n'
checksum = (((len(file_details[0]))**((change%2)*((len(file_details[2]))%6+1)))%(len(file_details[1])))
format_title = format_title.format(file_details[0],file_details[1],file_details[2],change,file_details[3],checksum)
doc_cont = format_title+final_locations+"</inject>"
print(doc_cont)
doc_cont.encode(encoding='UTF-8',errors='strict')

try:
  with open(os.path.join(path_output, file_details[3]),'x') as g:
    g.write(doc_cont)
except:
  with open(os.path.join(path_output, file_details[3]),'w') as g:
    g.write(doc_cont)
