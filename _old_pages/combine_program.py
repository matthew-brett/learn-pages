import os.path as op
from subprocess import check_call

all_content = []

for i in range(13):
    day = f'day_{i:02d}'
    lab = f'lab_{i:02d}'
    for root in day, lab:
        fname = root + '.rst'
        if not op.exists(fname):
            continue
        with open(fname, 'rt') as fobj:
            lines = fobj.readlines()
        marker = '=' * len(root)
        header = ['\n'.join([marker, root, marker, '', ''])]
        all_content += header + lines + ['\n\n']

with open('all_classes.rst', 'wt') as fobj:
    fobj.write(''.join(all_content))

# https://github.com/executablebooks/rst-to-myst
check_call(['rst2myst', 'convert', 'all_classes.rst'])
