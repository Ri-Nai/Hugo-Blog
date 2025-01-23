import os

dir = r"D:\Code\Ri-Nai.github.io\public"
# delete all files in the directory except for the .git folder
# 2025\01-06-离散数学复习笔记 2025\01-06-数据结构与算法设计复习笔记 public\2024\12-16-大学物理aii复习笔记

exclude = (
    r"D:\Code\Ri-Nai.github.io\public\2025\01-06-数据结构与算法设计复习笔记",
    r"D:\Code\Ri-Nai.github.io\public\2024\12-16-大学物理aii复习笔记",
    r"D:\Code\Ri-Nai.github.io\public\2025\01-06-离散数学复习笔记",
    r"D:\Code\Ri-Nai.github.io\public\.git",
)

for root, dirs, files in os.walk(dir, topdown=False):
    
    if any(
        s in root
        for s in exclude
    ):
        for name in files:
            if any(
                name.endswith(s)
                for s in ("jpg", "png")
            ):
                # print(os.path.join(root, name))
                os.remove(os.path.join(root, name))
        continue
    for name in files:
        os.remove(os.path.join(root, name))
        # print(root, name)
        # print(os.path.join(root, name))
        # 0-0


