# -*- coding: utf-8 -*-

def out_markdown(content):
    markdown = """%0A%0A| Platform | build | runned | result | FailScene | %0A| :---: | :---: | :---: | :---: | :---: | %0A"""

    for line in content:
        markdown = markdown + line + '%0A'
    print(f"::set-output name=details::{markdown}")
    txt = "afswewtw"
    print(f"::set-output name=msg::{txt}")
    return markdown
    
    
    
    
content = ['| 1 | 4 | 5❌ | 353 | 43535✅ | ', '| 567575 | 3535 | 5675 | [dgds](http://lan-jenkins.cocos.org/job/CocosGitHub/job/PR_Action/job/windows/682/artifact/image/compareimage-android-group01/advance_widget_startplay_1.png) | ghfs ☑ | '  ]
out_markdown(content)
