"""
User Stories:

You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple
containing a key-value pair

add_setting function should:

Convert the key and value to lowercase.
If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]'
added with value '[value]' successfully!.
The messages returned should have the key and value in lowercase.
You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple
containing a key-value pair.

update_setting function should:

Convert the key and value to lowercase.
If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to
'[value]' successfully!
If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
The messages returned should have the key and value in lowercase.
You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.

delete_setting function should:

Convert the key passed to lowercase.
If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]'
deleted successfully!
If the key setting does not exist, return Setting not found!
The messages returned should have the key in lowercase.
You should define a function named view_settings with one parameter representing a dictionary of settings.

view_settings function should:

Return No settings available. if the given dictionary of settings is empty.
If the dictionary contains any settings, return a string displaying the settings. The string should start with Current
User Settings: followed by the key-value pairs, each on a new line and with the key capitalized. For example,
view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:

Current User Settings:
Theme: dark
Notifications: enabled
Volume: high

For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.
"""

def add_setting(settings, keyval):
    key = keyval[0].lower()
    val = keyval[1].lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = val
        return f"Setting '{key}' added with value '{val}' successfully!"


def update_setting(settings, keyval):
    key = keyval[0].lower()
    val = keyval[1].lower()

    if key in settings:
        settings[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    formatted_items = ""
    if not settings:
        return "No settings available."
    else:
        for key, value in settings.items():
            formatted_items += f"{key.title()}: {value}\n"

        return f"Current User Settings:\n{formatted_items}"


test_settings = dict()
test_settings['theme'] = 'dark'
test_settings['notifications'] = 'enabled'
print(add_setting(test_settings, ('theme','light')))
print(add_setting(test_settings, ('menu','enabled')))
print(update_setting( test_settings,('theme','light')))
print(update_setting(test_settings, ('notifications','enabled')))
print(view_settings(test_settings))
print(delete_setting( test_settings,'theme'))
