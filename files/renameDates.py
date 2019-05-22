#! python3

import shutil, os, re

date_pattern = re.compile(r"""
    ^(.*?)
    ((0|1)?d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

#
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    if mo == None:
        continue

    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = before_part + day_part + '-' + month_part + '-' + \
        year_part + after_part

    print('Renaming "{}" to "{}...'.format(amer_filename, euro_filename))
    # shutil.move(amer_filename, euro_filename)

