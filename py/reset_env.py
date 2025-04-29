import os
import shutil

def clear_directory(dir_path):
    """删除指定目录下的所有文件和子目录"""
    if not os.path.exists(dir_path):
        print(f"目录不存在，无需清理: {dir_path}")
        return
    if not os.path.isdir(dir_path):
        print(f"提供的路径不是一个目录: {dir_path}")
        return

    for item_name in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item_name)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                print(f"已删除文件: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"已删除目录及其内容: {item_path}")
        except Exception as e:
            print(f"删除 {item_path} 时出错: {e}")

def delete_file(file_path):
    """删除指定文件"""
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"已删除文件: {file_path}")
        elif not os.path.exists(file_path):
             print(f"文件不存在，无需删除: {file_path}")
        else:
            print(f"提供的路径不是一个文件: {file_path}")
    except Exception as e:
        print(f"删除文件 {file_path} 时出错: {e}")

if __name__ == "__main__":
    # 获取脚本所在目录的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. 清理【新作总结】目录
    summary_new_dir = os.path.join(script_dir, "../新作总结")
    print(f"\n开始清理目录: {summary_new_dir}")
    clear_directory(summary_new_dir)

    # 2. 清理【写作中】目录
    writing_dir = os.path.join(script_dir, "../写作中_原文")
    print(f"\n开始清理目录: {writing_dir}")
    clear_directory(writing_dir)

    # 3. 删除【summary/新作_总结合集.md】文件
    summary_file = os.path.join(script_dir, "../summary", "新作_总结合集.md")
    print(f"\n开始删除文件: {summary_file}")
    delete_file(summary_file)

    print("\n清理操作完成。") 