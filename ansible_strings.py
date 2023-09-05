#!/usr/bin/env python3
import re
import yaml

# Function to clean up descriptions
def clean_description(description):
    return '\n'.join(re.sub(r'^#+\s*', '', line) for line in description.split('\n'))

# Read the Ansible Role defaults file
with open('defaults/main.yml', 'r') as yaml_file:
    yaml_content = yaml_file.read()

# Define a regular expression pattern to match comments with tags and content
comment_pattern = r'# @(\w+)(.*?)((?=# @)|$)'

# Find all matching comments in the YAML content
matches = re.findall(comment_pattern, yaml_content, re.DOTALL)

# Check if the YAML content contains the @ansible_strings tag
ansible_strings_present = any(tag == 'ansible_strings' for tag, _, _ in matches)

if not ansible_strings_present:
    print("The defaults file for this Ansible Role is not compatible with @ansible_strings. Exiting.")
    exit(1)

# Initialize metadata with default values
metadata = {
    'title': 'Ansible Role',
    'summary': 'Summary not provided',
    'description': 'Description not provided.',
    'requirements': [],  # Initialize as an empty list
    'parameters': {}
}

current_param_name = None  # Track the current parameter name
current_description = []  # Track the lines of the current description

# Parse the matched comments and update metadata
for tag, content, _ in matches:
    content = content.strip()  # Remove leading/trailing spaces
    if tag == 'title':
        metadata['title'] = content
    elif tag == 'summary':
        metadata['summary'] = content
    elif tag == 'description':
        metadata['description'] = clean_description(content)
    elif tag == 'requirements':
        # Parse requirements as lines within the comment and clean out leading '#' and spaces
        requirements_list = [req.strip('# ').strip() for req in content.strip().split('\n')]
        requirements = [req for req in requirements_list if req]
        metadata['requirements'].extend(requirements)  # Merge the lists
    elif tag == 'param':
        # Split the content into lines and remove leading/trailing spaces
        param_lines = [param.strip() for param in content.strip().split('\n')]
        last_line = param_lines[-1]
        param_name, default_value = [part.strip() for part in last_line.split(':')]
        current_param_name = param_name

        # Extract the parameter description lines
        description_lines = [line for line in param_lines if not line.startswith(param_name + ':')]
        metadata['parameters'][param_name] = {
            'description': clean_description('\n'.join(description_lines)),
            'default_value': default_value
        }

# Create the Markdown README.md content
markdown_content = f"# {metadata['title']}\n{metadata['summary']}\n\n"
markdown_content += f"## Description\n{metadata['description']}\n\n"
markdown_content += "## Requirements\n"
if metadata['requirements']:
    for req in metadata['requirements']:
        markdown_content += f"- {req}\n"
    markdown_content += "\n"

# Extracted parameters
parameters = metadata['parameters']
if parameters:
    markdown_content += "## Parameters\n\n"
    for param_name, param_data in parameters.items():
        markdown_content += f"### {param_name}\n"
        markdown_content += f"{param_data['description']}\n\n"
        markdown_content += f"Default Value: `{param_data['default_value']}`\n\n"

# Write the generated Markdown content to README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(markdown_content)

print("README.md generated successfully.")

