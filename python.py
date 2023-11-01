import yaml
import json

with open('input.yaml', 'r')as file:
	data = yaml.safe_load(file)

jsonStrData = json.dumps(data) 
print(jsonStrData)

#Set Output Variable
#output_value = data.get('R_VERSION')
print(f"::set-output name=data::{jsonStrData}")
