# -*- coding: utf-8 -*-
"""
离线依赖包下载脚本
用于在有外网的机器上下载所有需要的Python库，然后复制到无外网的Windows Server 2012上安装
"""

import subprocess
import os
import sys


def download_packages():
    """下载所有依赖包"""
    
    # 需要下载的包列表
    packages = [
        'pyautogui',
        'pygetwindow', 
        'Pillow',
        'pywin32',
        'PyInstaller'
    ]
    
    # 创建packages目录
    packages_dir = os.path.join(os.path.dirname(__file__), 'packages')
    if not os.path.exists(packages_dir):
        os.makedirs(packages_dir)
    
    print("=" * 60)
    print("开始下载离线依赖包...")
    print("=" * 60)
    print(f"\n下载目录: {packages_dir}")
    print(f"\n需要下载的包: {', '.join(packages)}\n")
    
    for package in packages:
        print(f"正在下载: {package} ...")
        try:
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'download', '-d', packages_dir, package],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"✓ {package} 下载成功\n")
            else:
                print(f"✗ {package} 下载失败")
                print(f"错误信息: {result.stderr}\n")
                
        except Exception as e:
            print(f"✗ {package} 下载异常: {e}\n")
    
    print("=" * 60)
    print("✓ 所有依赖包下载完成！")
    print("=" * 60)
    print(f"\n下载的包位于: {packages_dir}")
    print("\n下一步操作:")
    print("1. 将 'packages' 文件夹复制到 Windows Server 2012 机器上")
    print("2. 在目标机器上执行以下命令安装:")
    print(f"   pip install --no-index --find-links=./packages pyautogui pygetwindow Pillow pywin32 PyInstaller")
    print("\n3. 然后运行打包脚本或直接使用打包好的exe文件")


if __name__ == '__main__':
    download_packages()
