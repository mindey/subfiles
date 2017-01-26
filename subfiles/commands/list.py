"""The list command."""


from json import dumps

from .base import Base

from .utils import files_by_extensions

import sys

class List(Base):

    def run(self):

        level = 2

        if len(sys.argv) == 3:
            try:
                print 'CHANGING LEVEL'
                level = int(sys.argv[-1])
            except:
                pass

        results = files_by_extensions('.', level)

        for key, val in enumerate(results):
            print("[*.{key}]".format(**{'key':val}))
            for item in results[val]:
                print(item)
            print("\n"),