# -*- coding: utf-8 -*-

def out_markdown(content):
    markdown = """
| Platform | build | runned | result | FailScene |
| :---: | :---: | :---: | :---: | :---: |
"""

    for line in content:
        markdown = markdown + """%s
""" % line
    print(f"::set-output name=details::{markdown}")
    txt = "afswewtw"
    print(f"::set-output name=msg::{markdown}")
    return markdown
    
    
    
    
content = ['| 1 | 4 | 5 | 353 | 43535 | ', '| 567575 | 3535 | 5675 | dgds | ghfs | '  ]
out_markdown(content)
