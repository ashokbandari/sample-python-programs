import yaml

# Load YAML file
with open('file.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Extract server group data
servers = data.get('servers')

# Extract OpenAPI version
openapi_version = data.get('openapi')

# Extract API information
apis = data.get('paths')

# Print extracted data
print('Server group data:')
print(servers)
print('OpenAPI version:')
print(openapi_version)
print('APIs:')
print(apis)
