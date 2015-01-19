__author__ = 'Alex Gusev <alex@flancer64.com>'
import prxgt.App


class Attribute:
    """In-memory model for one attribute"""
    name = None
    type = None
    value = None

    def __repr__(self):
        result = "[" + self.name + "@" + self.type
        if self.value is not None and \
                        self.type == prxgt.App.App.ATTR_TYPE_TXT:
            result += "=" + self.value[:4] + "..."
        else:
            result += "=" + repr(self.value)
        result += "]"
        return result