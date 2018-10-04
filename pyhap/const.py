"""This module contains constants used by other modules."""
MAJOR_VERSION = 2
MINOR_VERSION = 2
PATCH_VERSION = 2
__short_version__ = '{}.{}'.format(MAJOR_VERSION, MINOR_VERSION)
__version__ = '{}.{}'.format(__short_version__, PATCH_VERSION)
REQUIRED_PYTHON_VER = (3, 5)

# ### Misc ###
STANDALONE_AID = 1  # Standalone accessory ID (i.e. not bridged)


# ### Default values ###
DEFAULT_CONFIG_VERSION = 2
DEFAULT_PORT = 51827


# ### Category values ###
# Category is a hint to iOS clients about what "type" of Accessory this
# represents, for UI only.
CATEGORY_OTHER = 1
CATEGORY_BRIDGE = 2
CATEGORY_FAN = 3
CATEGORY_GARAGE_DOOR_OPENER = 4
CATEGORY_LIGHTBULB = 5
CATEGORY_DOOR_LOCK = 6
CATEGORY_OUTLET = 7
CATEGORY_SWITCH = 8
CATEGORY_THERMOSTAT = 9
CATEGORY_SENSOR = 10
CATEGORY_ALARM_SYSTEM = 11
CATEGORY_DOOR = 12
CATEGORY_WINDOW = 13
CATEGORY_WINDOW_COVERING = 14
CATEGORY_PROGRAMMABLE_SWITCH = 15
CATEGORY_RANGE_EXTENDER = 16
CATEGORY_CAMERA = 17
CATEGORY_VIDEO_DOOR_BELL = 18
CATEGORY_AIR_PURIFIER = 19


# ### HAP Permissions ###
HAP_PERMISSION_HIDDEN = 'hd'
HAP_PERMISSION_NOTIFY = 'ev'
HAP_PERMISSION_READ = 'pr'
HAP_PERMISSION_WRITE = 'pw'


# ### HAP representation ###
HAP_REPR_ACCS = 'accessories'
HAP_REPR_AID = 'aid'
HAP_REPR_CHARS = 'characteristics'
HAP_REPR_DESC = 'description'
HAP_REPR_FORMAT = 'format'
HAP_REPR_IID = 'iid'
HAP_REPR_MAX_LEN = 'maxLen'
HAP_REPR_PERM = 'perms'
HAP_REPR_SERVICES = 'services'
HAP_REPR_STATUS = 'status'
HAP_REPR_TYPE = 'type'
HAP_REPR_VALUE = 'value'
