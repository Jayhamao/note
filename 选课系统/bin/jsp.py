import os, sys
sys.path.append('/path/to')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

sys.path.insert(0, dir)     #添加路径


from core import main

if __name__ == "__main__":
    obj = main.Manage_center()
    obj.run()