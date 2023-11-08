import yaml
 
# Parse the YAML file

with open('input.yaml', 'r') as file:

    data = yaml.safe_load(file)
 
# Write the data to a .env file

with open('.env', 'w') as file:

    for key, value in data.items():

        file.write(f'{key}={value}\n')
