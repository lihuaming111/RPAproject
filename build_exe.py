# -*- coding: utf-8 -*-
"""
PyInstaller 打包配置文件
用于将 RpaLis.py 打包成 Windows 可执行文件
"""

import PyInstaller.__main__
import sys
import os

def build_exe():
    """构建exe文件"""
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # PyInstaller 参数
    args = [
        'RpaLis.py',                          # 主程序文件
        '--name=RpaLis',                      # 生成的exe名称
        '--onefile',                          # 打包成单个exe文件
        '--windowed',                         # 不显示控制台窗口（如果需要看到输出，去掉这个参数）
        '--icon=NONE',                        # 图标文件（可选）
        f'--distpath={os.path.join(current_dir, "dist")}',  # 输出目录
        f'--workpath={os.path.join(current_dir, "build")}', # 临时工作目录
        '--clean',                            # 清理临时文件
        '--noconfirm',                        # 不询问确认
    ]
    
    print("=" * 60)
    print("开始打包 RpaLis.exe...")
    print("=" * 60)
    print(f"\n打包参数:")
    for arg in args:
        print(f"  {arg}")
    print()
    
    try:
        # 执行打包
        PyInstaller.__main__.run(args)
        
        print("\n" + "=" * 60)
        print("✓ 打包完成！")
        print("=" * 60)
        print(f"\n生成的文件位于: {os.path.join(current_dir, 'dist', 'RpaLis.exe')}")
        print("\n注意事项:")
        print("1. 在目标Windows Server 2012上运行前，需要安装以下Python库:")
        print("   - pyautogui")
        print("   - pygetwindow")
        print("   - Pillow (pyautogui的依赖)")
        print("   - pywin32 (Windows特定功能)")
        print("\n2. 如果目标机器没有外网，请提前下载这些库的whl文件:")
        print("   pip download -d ./packages pyautogui pygetwindow Pillow pywin32")
        print("\n3. 在目标机器上离线安装:")
        print("   pip install --no-index --find-links=./packages pyautogui pygetwindow Pillow pywin32")
        
    except Exception as e:
        print(f"\n✗ 打包失败: {e}")
        sys.exit(1)


if __name__ == '__main__':
    build_exe()
