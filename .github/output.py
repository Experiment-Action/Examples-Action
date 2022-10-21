# -*- coding: utf-8 -*-

import os


env_file = os.getenv('GITHUB_ENV')
output_file = os.getenv('GITHUB_OUTPUT')
hello='^0^ 我是测试的 ^0^'


def out_markdown(content):
    markdown = '''<br/>| Platform | build | runned | result | FailScene | <br/> | :---: | :---: | :---: | :---: | :---: | <br/> '''

    for line in content:
        markdown = markdown + line + '<br/>'
    #print(f"::set-output name=details::{markdown}")
    txt = "afswewtw"
    #print(f"::set-output name=msg::{txt}")
    #with open(env_file, "a") as f:
    #    f.write(f"wahah={hello}")

    with open(output_file, "a") as f:
        f.write(f"wahah={hello}\n")
        f.write(f"details={markdown}\n")
        f.write(f"msg={txt}")
    
    return markdown
    





content = ['| 1 | 4 | 5❌ | 353 | 43535✅ | ', '| 567575 | 3535 | 5675 | [dgds](http://lan-jenkins.cocos.org/job/CocosGitHub/job/PR_Action/job/windows/682/artifact/image/compareimage-android-group01/advance_widget_startplay_1.png) | ghfs ☑ | '  ]
out_markdown(content)
