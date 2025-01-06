"""
保存当前文件夹下的所有文件 （包括子文件夹）
使hugo检测到文件变化
否则没法渲染
"""

import os
import shutil
import time

# 保证深的先被保存
def save_deep_first(path):
    if os.path.isdir(path):
        for sub in os.listdir(path):
            dir = os.path.join(path, sub)
            if os.path.isdir(dir):
                save_deep_first(dir)
        for sub in os.listdir(path):
            dir = os.path.join(path, sub)
            if os.path.isfile(dir):
                os.utime(dir, None)
                time.sleep(0.7)
                # print(dir)

save_deep_first(os.getcwd())
