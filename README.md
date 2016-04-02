#Person Tracker
This is a tracker to keep track of incidental information gathered about people
#Data Structure
Data is stored in pickled dictionaries, one per file, in the following structure:
`'UUID': {
  'data field': 'value'
}`
The UUID is not stored in the file, but is the file's name.
The file structure is as follows:
```
-/
  -index.pickle
    this file is loaded first, and points to every record in the system. It also
    contains the name each person is usually known as for display purposes.
  -template.pickle
    this file contains every field currently in the system, so that it is easy
    to add a pre-made field to a record. Might change this later so there's a
    separate file for the default fields for a new record, least this gets
    too long.
  -/data
    -0.pickle
    -1.pickle
    -2.pickle
    ...
    -n.pickle
  ```

This folder contains each person's profile, one per file.
