# Domain data

## Overview
Domain data file contains description for all attributes (names and types) and data itself (instances with attributes
values). Domain data file can be saved to the file and can be used in various tests. 

## Structure

    {
      "meta": {
        "a0": {"type": "int"},
        "a1": {"type": "decimal"},
        "a2": {"type": "string"},
        "a3": {"type": "text"}
      },
      "data": {
        "1": {
          "a0": 4
        },
        "2": {
          "a0": 6,
          "a2": "value"
        },
        "3": {
          "a1": 23.43,
          "a2": "other value",
          "a3": "text with more than 255 characters length."
        }
      }
    }