"""
This file is used to generate reStructuredText tables for Group and Model references.
"""
import os
import andes

if not (os.path.isfile('modelref.rst') and os.path.isfile('configref.rst')):

    ss = andes.prepare(nomp=True)

    # write the top-level index file

    out = """.. _modelref:

****************
Model references
****************

Use the left navigation pane to locate the group and model
and view details.

"""

    out += ss.supported_models(export='rest')

    out += '\n'
    out += '.. toctree ::\n'
    out += '    :maxdepth: 2\n'
    out += '    :hidden:\n'
    out += '\n'

    file_tpl = '    groupdoc/{}\n'

    for group in ss.groups.values():
        out += file_tpl.format(group.class_name)

    with open('modelref.rst', 'w') as f:
        f.write(out)

    # write individual files

    os.makedirs('groupdoc', exist_ok=True)

    for group in ss.groups.values():
        with open(f'groupdoc/{group.class_name}.rst', 'w') as f:
            f.write(group.doc_all(export='rest'))

    # Config Reference Section

    out = ''
    out += '.. _configref:\n\n'
    out += '*****************\n'
    out += 'Config references\n'
    out += '*****************\n'
    out += '\n'

    out += ss.config.doc(export='rest', target=True, symbol=False)

    for r in ss.routines.values():
        out += r.config.doc(export='rest', target=True, symbol=False)

    with open('configref.rst', 'w') as f:
        f.write(out)
