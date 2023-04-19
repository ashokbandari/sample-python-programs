import yaml

with open('file.yaml') as f:
    data = yaml.safe_load(f)

# Extract server group data
server_group = data['servers'][0]

# Extract OpenAPI version
openapi_version = data['openapi']

# Extract APIs
apis = data['paths']

# Extract components
components = data['components']

# Extract schemas, responses, and parameters
schemas = components.get('schemas', {})
responses = components.get('responses', {})
parameters = []

for path, methods in apis.items():
    for method, data in methods.items():
        method_params = data.get('parameters', [])
        parameters.extend(method_params)

# Extract descriptions
descriptions = {}

for path, methods in apis.items():
    for method, data in methods.items():
        if 'description' in data:
            descriptions.setdefault(path, {})[method] = data['description']

# Extract types and contents
types = {}
contents = {}

for path, methods in apis.items():
    for method, data in methods.items():
        for response_code, response_data in data.get('responses', {}).items():
            for content_type, content_data in response_data.get('content', {}).items():
                schema = content_data.get('schema')
                if schema:
                    type_ = schema.get('type')
                    if type_:
                        types.setdefault(path, {})[method] = type_
                        contents.setdefault(content_type, []).append((path, method))

# Extract patches
patches = {}

for path, methods in apis.items():
    for method, data in methods.items():
        if method == 'patch':
            patches.setdefault(path, []).append(data)

# Extract properties
properties = {schema_name: schema_data.get('properties', {})
              for schema_name, schema_data in schemas.items()}

# Print extracted data
print('Server group data:', server_group)
print('OpenAPI version:', openapi_version)
print('APIs:', apis)
print('Components:', components)
print('Schemas:', schemas)
print('Responses:', responses)
print('Parameters:', parameters)
print('Descriptions:', descriptions)
print('Types:', types)
print('Contents:', contents)
print('Patches:', patches)
print('Properties:', properties)
