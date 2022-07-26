# -*- coding: utf-8 -*-

def out_markdown(content):
    markdown = """
| Platform | build | runned | result | FailScene |
| :---: | :---: | :---: | :---: | :---: |
"""

    for line in content:
        markdown = markdown + """%s\%0A""" % line
    #print(f"::set-output name=report::{markdown}")
    print(f"::set-output name=msg::{markdown}")
    return markdown
    
    
    
    
content = ['| 1 | 4 | 5 | 353 | 43535 | ', '| 567575 | 3535 | 5675 | dgds | ghfs | '  ]
out_markdown(content)
