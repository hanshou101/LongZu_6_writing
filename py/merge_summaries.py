import os

# 目录和目标文件
summary_dir = '前作梗概'
target_file = 'summary/梗概合集.md'

# 获取所有md文件，按文件名排序
files = sorted([f for f in os.listdir(summary_dir) if f.endswith('.md')])

all_content = []
for filename in files:
    filepath = os.path.join(summary_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    # 文件名作为标题
    all_content.append(f'# {filename}\n\n{content}\n')

# 需要先创建 summary 目录
os.makedirs(os.path.dirname(target_file), exist_ok=True)

# 合并内容并写入目标文件
with open(target_file, 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(all_content)) 