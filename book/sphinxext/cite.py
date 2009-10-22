import re

# Define LaTeX math node:

if 0:
    from docutils.parsers.rst import Directive, directives

    class citaton_node(nodes.General, nodes.Element):
        pass

    def cite_role(role, rawtext, text, lineno, inliner,
                  options={}, content=[]):
        i = rawtext.find('`')
        latex = rawtext[i+1:-1]
        try:
            mathml_tree = parse_latex_math(latex, inline=True)
        except SyntaxError, msg:
            msg = inliner.reporter.error(msg, line=lineno)
            prb = inliner.problematic(rawtext, rawtext, msg)
            return [prb], [msg]
        node = latex_math(rawtext)
        node['latex'] = latex
        node['mathml_tree'] = mathml_tree
        return [node], []


    def XXXcite_role(app, docname, source):
        r"""Citaitons...
        """
        s = "\n".join(source)
        if s.find(":cite:") == -1:
            return

        pat = re.compile(r':cite:`(.*)`', re.MULTILINE)
        s_new = pat.sub(r'\[\1\]', s)
        source[:] = [s]

    def setup(app):
        app.add_node(latex_math)
        app.add_role('cite', cite_role)
