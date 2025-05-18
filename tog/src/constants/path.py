import os

# ----------------
# Path constants.
# ----------------


class Path:

    CONSTANTS_FOLDER = os.path.dirname(__file__)
    SRC_FOLDER = os.path.abspath(os.path.join(CONSTANTS_FOLDER, '..'))
    SOURCES_FOLDER = os.path.abspath(os.path.join(
        SRC_FOLDER, 'public', 'sources')) + os.path.sep
