#Person Tracker
This is a tracker to keep track of incidental information gathered about people
#Data Structure
Data is stored in pickled dictionaries, one per file, in the following structure:
`'UUID': {
  'data field': 'value'
}`
The file structure is as follows:
-/
  -index.pickle
    this file is loaded first, and points to every file in the system. It also
    contains the name each person is usually known as for display purposes.
  -template.pickle
    this file contains every field currently in the system, so that it is easy
    to add a premade field to a person's profile
  -/data
    -000.pickle
    -001.pickle
    -002.pickle
    ...
    -nnn.pickle
    this folder contains each person's profile
