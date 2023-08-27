#!/usr/bin/env python

# Copyright 2023 distjr_
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import markdown

def getmarkhtml(markdown_text):
    return """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width">
    <script src="https://cdn.bootcdn.net/ajax/libs/babel-polyfill/7.12.1/polyfill.min.js"></script>
    <script>
        MathJax = {
            tex: {inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]}
        };
    </script>
    <script id="MathJax-script" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-chtml.min.js"></script>
</head>
<body>
""" + markdown.markdown(markdown_text) + """</body>"""\


def runtimee(timee):
    return "%04d年%02d月%02d日%02d时%02d分%02d秒" % (timee[0],timee[1],timee[2],timee[3],timee[4],timee[5])
