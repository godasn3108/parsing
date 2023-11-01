import yaml

with open('input.yaml', 'r')as file:
	data = yaml.safe_load(file)
print(data)
#Set Output Variable
#output_value = data.get('R_VERSION')
print(f"::set-output name=data::{data}")
