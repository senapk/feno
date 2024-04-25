import subprocess
from subprocess import PIPE
# import markdown
from .css_style import CssStyle

class HTML:

    @staticmethod
    def remove_css_link_from_html(html_file: str):
        with open(html_file, "r") as f:
            content = f.read()
        output = []
        for line in content.split("\n"):
            if not line.startswith('  <link rel="stylesheet"'):
                output.append(line)
        with open(html_file, "w") as f:
            f.write("\n".join(output))



    @staticmethod
    def generate_html_with_pandoc(title: str, input_file: str, output_file: str, enable_latex: bool = True):
        fulltitle = title.replace('!', '\\!').replace('?', '\\?')
        cmd = ["pandoc", input_file, '--css', CssStyle.get_file(), '--metadata', 'pagetitle=' + fulltitle,
            '-s', '-o', output_file]
        if enable_latex:
            cmd.append("--mathjax")
        try:
            p = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            stdout, stderr = p.communicate()
            if stdout != "" or stderr != "":
                print(stdout)
                print(stderr)
            HTML.remove_css_link_from_html(output_file)

        except Exception as e:
            print("Erro no comando pandoc:", e)
            exit(1)

#     codehilite_css = """
# <style>

# pre { line-height: 125%; }
# td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
# span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
# td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
# span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
# .codehilite .hll { background-color: #ffffcc }
# .codehilite { background: #f8f8f8; }
# .codehilite .c { color: #3D7B7B; font-style: italic } /* Comment */
# .codehilite .err { border: 1px solid #FF0000 } /* Error */
# .codehilite .k { color: #008000; font-weight: bold } /* Keyword */
# .codehilite .o { color: #666666 } /* Operator */
# .codehilite .ch { color: #3D7B7B; font-style: italic } /* Comment.Hashbang */
# .codehilite .cm { color: #3D7B7B; font-style: italic } /* Comment.Multiline */
# .codehilite .cp { color: #9C6500 } /* Comment.Preproc */
# .codehilite .cpf { color: #3D7B7B; font-style: italic } /* Comment.PreprocFile */
# .codehilite .c1 { color: #3D7B7B; font-style: italic } /* Comment.Single */
# .codehilite .cs { color: #3D7B7B; font-style: italic } /* Comment.Special */
# .codehilite .gd { color: #A00000 } /* Generic.Deleted */
# .codehilite .ge { font-style: italic } /* Generic.Emph */
# .codehilite .ges { font-weight: bold; font-style: italic } /* Generic.EmphStrong */
# .codehilite .gr { color: #E40000 } /* Generic.Error */
# .codehilite .gh { color: #000080; font-weight: bold } /* Generic.Heading */
# .codehilite .gi { color: #008400 } /* Generic.Inserted */
# .codehilite .go { color: #717171 } /* Generic.Output */
# .codehilite .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
# .codehilite .gs { font-weight: bold } /* Generic.Strong */
# .codehilite .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
# .codehilite .gt { color: #0044DD } /* Generic.Traceback */
# .codehilite .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
# .codehilite .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
# .codehilite .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
# .codehilite .kp { color: #008000 } /* Keyword.Pseudo */
# .codehilite .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
# .codehilite .kt { color: #B00040 } /* Keyword.Type */
# .codehilite .m { color: #666666 } /* Literal.Number */
# .codehilite .s { color: #BA2121 } /* Literal.String */
# .codehilite .na { color: #687822 } /* Name.Attribute */
# .codehilite .nb { color: #008000 } /* Name.Builtin */
# .codehilite .nc { color: #0000FF; font-weight: bold } /* Name.Class */
# .codehilite .no { color: #880000 } /* Name.Constant */
# .codehilite .nd { color: #AA22FF } /* Name.Decorator */
# .codehilite .ni { color: #717171; font-weight: bold } /* Name.Entity */
# .codehilite .ne { color: #CB3F38; font-weight: bold } /* Name.Exception */
# .codehilite .nf { color: #0000FF } /* Name.Function */
# .codehilite .nl { color: #767600 } /* Name.Label */
# .codehilite .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
# .codehilite .nt { color: #008000; font-weight: bold } /* Name.Tag */
# .codehilite .nv { color: #19177C } /* Name.Variable */
# .codehilite .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
# .codehilite .w { color: #bbbbbb } /* Text.Whitespace */
# .codehilite .mb { color: #666666 } /* Literal.Number.Bin */
# .codehilite .mf { color: #666666 } /* Literal.Number.Float */
# .codehilite .mh { color: #666666 } /* Literal.Number.Hex */
# .codehilite .mi { color: #666666 } /* Literal.Number.Integer */
# .codehilite .mo { color: #666666 } /* Literal.Number.Oct */
# .codehilite .sa { color: #BA2121 } /* Literal.String.Affix */
# .codehilite .sb { color: #BA2121 } /* Literal.String.Backtick */
# .codehilite .sc { color: #BA2121 } /* Literal.String.Char */
# .codehilite .dl { color: #BA2121 } /* Literal.String.Delimiter */
# .codehilite .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
# .codehilite .s2 { color: #BA2121 } /* Literal.String.Double */
# .codehilite .se { color: #AA5D1F; font-weight: bold } /* Literal.String.Escape */
# .codehilite .sh { color: #BA2121 } /* Literal.String.Heredoc */
# .codehilite .si { color: #A45A77; font-weight: bold } /* Literal.String.Interpol */
# .codehilite .sx { color: #008000 } /* Literal.String.Other */
# .codehilite .sr { color: #A45A77 } /* Literal.String.Regex */
# .codehilite .s1 { color: #BA2121 } /* Literal.String.Single */
# .codehilite .ss { color: #19177C } /* Literal.String.Symbol */
# .codehilite .bp { color: #008000 } /* Name.Builtin.Pseudo */
# .codehilite .fm { color: #0000FF } /* Name.Function.Magic */
# .codehilite .vc { color: #19177C } /* Name.Variable.Class */
# .codehilite .vg { color: #19177C } /* Name.Variable.Global */
# .codehilite .vi { color: #19177C } /* Name.Variable.Instance */
# .codehilite .vm { color: #19177C } /* Name.Variable.Magic */
# .codehilite .il { color: #666666 } /* Literal.Number.Integer.Long */

# </style>
# """

#     @staticmethod
#     def fix_markdown_indentation(content):
#         last: int = -1
#         dist: int = -1
#         step: int = 0
#         inside_fences = False
#         output = []
#         for line in content.split("\n"):
#             line_init = line.lstrip()
#             line_dist = len(line) - len(line_init)
#             if not inside_fences and (line_init.startswith("- ") or line_init.startswith("* ")):
#                 if line_dist == 0: # primeiro
#                     last = 0
#                     dist = 0
#                 elif line_dist > dist:
#                     if last == 0: # segundo level
#                         step = line_dist
#                     last += 1 # proximo level
#                     dist = line_dist
#                 elif line_dist < dist:
#                     last -= int((dist - line_dist) / step)
#                     dist = line_dist
#                 line = " " * (4 * last) + line_init
#             if line.startswith("```"):
#                 inside_fences = not inside_fences
#             output.append(line)
#         return "\n".join(output)

#     @staticmethod
#     def generate_html_with_python(title: str, input_file: str, output_file: str):
#         with open(input_file) as f:
#             content = f.read()
#         lines = content.split("\n")
#         output = []
#         itemize = False
#         for line in lines:
#             if line.startswith("  - "):
#                 output.append("  " + line)
#             elif line.startswith("    - "):
#                 output.append("    " + line)
#             elif line.startswith("      - "):
#                 output.append("      " + line)
#             else:
#                 output.append(line)
#         content = "\n".join(output)
#         data = markdown.markdown(content,
#                                   extensions=['markdown_katex', 'md_in_html', 'fenced_code', 'codehilite', 'extra', 'nl2br', 'sane_lists', 'wikilinks', 'toc'],
#                                     extension_configs={
#                                         'markdown_katex': {
#                                             'no_inline_svg': True,  # fix for WeasyPrint
#                                             'insert_fonts_css': True,
#                                         },
#                                     })

#         with open(output_file, "w") as f:
#             f.write(data + HTML.codehilite_css)
