import glob
import os

def search_pdfs(root_folder, keyword):
    # 寻找子文件夹内的所有文件
    root_folder += r"\*\*"
    file_path = glob.glob(root_folder, recursive=True)
    for file_name in file_path:
        if keyword in file_name.upper():
            print("Find : " , file_name)

def main():
    root_folder = r"D:\Desktop\学习\论文"
    while True:
        keyword = input("请输入标题关键字，输入0退出：")
        keyword = keyword.strip().upper()
        if keyword == "0":
            break
        search_pdfs(root_folder, keyword)

if __name__ == "__main__":
    main()
