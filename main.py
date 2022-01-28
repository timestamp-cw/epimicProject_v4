# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from crawl import spider
from display import show

def print_start():
    # 在下面的代码行中使用断点来调试脚本。
    print(f'start crawl')  # 按 Ctrl+F8 切换断点。

def print_end():
    print("successful crawl")


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_start()

    # 抓取数据
    # spider()

    # 可视化数据
    show()

    print_end()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助