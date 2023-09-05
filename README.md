# Ansible Strings
This Python script is designed to generate README files for Ansible Roles based on
the information provided in the Ansible Role's `defaults/main.yml` file.
It uses special comment tags in the defaults file to extract metadata and generate
documentation in Markdown format.

Developed with Chat-GPT 3.5 :robot:

## Usage
To use this script, follow these steps:

1. Ensure you have PyYAML available.
   ```
   apt install python3-yaml
   ```

2. Run the script using the following command from the Ansible Role directory, assuming the script is in your PATH:

   ```bash
   cd <my ansible role>
   ansible_strings.py
   ```

3. After running the script, a `README.md` file will be generated in the same directory.

## Example File
Below is an example of a `defaults/main.yml` file with the special comment tags used by this script:

```yaml
---
# @ansible_strings
# @title Awesome Ansible Role
# @summary This is a sample Ansible Role that generates it's README from the defaults file
# @description
# This file contains default variables and settings for the Example Role. And it
# is rendered into a MarkDown formatted README.md file.
#
# And due to the magic of scripting, it can span quite some length
#
# Which also makes it easy to write a whole novel worth of information here.
#
# It also support lists! Like so:
#   - This
#   - is
#   - a
#   - list!
# @requirements
# Ansible version 2.10 or higher
# Python 3.x
# community.general
# community.crypto

# @param
# This is the first variable. It does something important.
example_variable1: 'value1'
# @param
# This is the second variable. It controls another aspect of the role.
# These descriptions can also span mutliple lines
example_variable2: 'value2'
# @param
# This is the third variable. It affects yet another aspect of the role.
# And this also does some magic with lists:
#  - Isn't
#  - that
#  - cool?
example_variable3: 'value3'
```

In this example, the `defaults/main.yml` file contains special comment tags that provide metadata about the Ansible Role.

## Explanation of Tags

- `@ansible_strings`: `Marks the defaults/main.yml` as compatible with this script.

- `@title`: Specifies the title of the Ansible Role.

  Example:
  ```
  # @title Ansible Role Example
  ```

- `@summary`: Provides a brief summary or description of the Ansible Role.

  Example:
  ```
  # @summary This is an example Ansible Role.
  ```

- `@description`: Offers a detailed description of the Ansible Role. This can span multiple lines and uses Markdown format.

  Example:
  ```
  # @description
  # This Ansible Role is an example of how to use the @description tag.
  # It includes descriptions of various parameters and requirements.
  ```

- `@requirements`: Lists the requirements for using the Ansible Role. Each requirement should be on a separate line.

  Example:
  ```
  # @requirements
  # Ansible 2.9+
  # Python 3.6+
  ```

- `@param`: Defines parameters for the Ansible Role. Each parameter tag includes a parameter name, default value, and a description. The parameter description can span multiple lines and uses Markdown format.

  Example:
  ```
  # @param
  #   This is an example parameter description.
  ExampleParam1: Default value for ExampleParam1.
  # @param
  #   This is another parameter description.
  ExampleParam2: Default value for ExampleParam2.
  ```
