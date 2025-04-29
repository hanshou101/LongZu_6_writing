import os
from pathlib import Path

# 定义源目录和目标文件
source_dir = Path("新作总结")
target_file = Path("summary/新作_总结合集.md")

# 确保源目录存在
if not source_dir.is_dir():
    print(f"错误：源目录 '{source_dir}' 不存在或不是一个目录。")
    exit()

# 清空或创建目标文件，准备写入
with open(target_file, 'w', encoding='utf-8') as outfile:
    outfile.write(f"""# 第{source_dir.name}本《龙族》 内容合集

""") # 添加一个主标题

# 递归遍历源目录及其子目录下的所有 .md 文件
# 使用 sorted() 确保处理顺序相对固定，先按目录再按文件名排序
markdown_files = sorted(source_dir.rglob('*.md'))

if not markdown_files:
    print(f"警告：在目录 '{source_dir}' 及其子目录下未找到任何 .md 文件。")
    exit()

current_book_dir = None

for source_file_path in markdown_files:
    print(f"正在处理文件: {source_file_path}")

    # 获取相对于 source_dir 的路径，用于生成标题
    relative_path = source_file_path.relative_to(source_dir)
    book_dir = relative_path.parts[0] # 获取第一级子目录名（如 '6'）

    # 读取源文件内容
    with open(source_file_path, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # 追加到目标文件
    with open(target_file, 'a', encoding='utf-8') as outfile:
        # 如果是新的书籍目录，添加一级标题
        if book_dir != current_book_dir:
            outfile.write(f"""
# 第{book_dir}本《龙族》

""")
            current_book_dir = book_dir

        # 使用文件名（不含扩展名）作为二级标题
        file_stem = source_file_path.stem
        outfile.write(f"""## {file_stem}

""") # 添加文件名作为二级标题
        outfile.write(content)
        outfile.write(f"""

---

""") # 添加分隔符

print(f"所有 .md 文件已成功合并到 '{target_file}'") 