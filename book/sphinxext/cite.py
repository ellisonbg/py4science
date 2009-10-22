import re

def cite_role(app, docname, source):
    r"""Citaitons...
    """
    s = "\n".join(source)
    if s.find(":cite:") == -1:
        return

    pat = re.compile(r':cite:`(.*)`', re.MULTILINE)
    s_new = pat.sub(r'\[\1\]', s)
    source[:] = [s]

def setup(app):
    app.connect("source-read", cite_role)
