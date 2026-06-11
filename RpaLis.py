"""
Time    : 2026/6/11
file    : RpaLis.py
Author : Li
Description: Windows系统RPA自动化工具 - 用于控制Windows应用程序
"""

import subprocess
import time
import os


class RpaWindowsTool:
    """Windows系统RPA工具类"""
    
    def __init__(self):
        """初始化Windows RPA工具"""
        print("Windows RPA工具已初始化")
    
    def open_application(self, exe_path, wait_time=3):
        """
        打开Windows应用程序
        :param exe_path: 应用程序的完整路径，如 D:\医生工作站\DocProject.exe
        :param wait_time: 等待应用启动的时间（秒）
        :return: 是否成功打开
        """
        try:
            # 检查文件是否存在
            if not os.path.exists(exe_path):
                print(f"错误: 文件不存在 - {exe_path}")
                return False
            
            # 使用subprocess启动程序
            subprocess.Popen([exe_path])
            print(f"已启动程序: {exe_path}")
            
            # 等待程序启动
            time.sleep(wait_time)
            return True
            
        except Exception as e:
            print(f"打开程序失败: {e}")
            return False
    
    def open_doctor_workstation(self, disk="D:", folder="医生工作站", exe_name="DocProject.exe"):
        """
        打开医生工作站程序
        :param disk: 磁盘盘符，默认 D:
        :param folder: 文件夹名称，默认 医生工作站
        :param exe_name: 可执行文件名，默认 DocProject.exe
        :return: 是否成功打开
        """
        # 构建完整路径
        exe_path = f"{disk}\\{folder}\\{exe_name}"
        
        print(f"正在打开医生工作站: {exe_path}")
        return self.open_application(exe_path, wait_time=5)
    
    def open_doctor_workstation_v2(self, disk="D:", folder="医生工作站", exe_name="DocProject2.exe"):
        """
        打开医生工作站程序 V2版本
        :param disk: 磁盘盘符，默认 D:
        :param folder: 文件夹名称，默认 医生工作站
        :param exe_name: 可执行文件名，默认 DocProject2.exe
        :return: 是否成功打开
        """
        # 构建完整路径
        exe_path = f"{disk}\\{folder}\\{exe_name}"
        
        print(f"正在打开医生工作站V2: {exe_path}")
        return self.open_application(exe_path, wait_time=5)
    
    def close_application(self, window_title):
        """
        关闭指定窗口标题的应用程序
        :param window_title: 窗口标题
        :return: 是否成功关闭
        """
        try:
            # 使用taskkill命令关闭窗口
            cmd = f'taskkill /F /FI "WINDOWTITLE eq {window_title}*"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"已关闭窗口: {window_title}")
                return True
            else:
                print(f"关闭窗口失败: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"关闭窗口异常: {e}")
            return False
    
    def activate_window(self, window_title):
        """
        激活指定窗口
        :param window_title: 窗口标题
        :return: 是否成功激活
        """
        try:
            import pygetwindow as gw
            windows = gw.getWindowsWithTitle(window_title)
            
            if windows:
                windows[0].activate()
                print(f"已激活窗口: {window_title}")
                return True
            else:
                print(f"未找到窗口: {window_title}")
                return False
                
        except ImportError:
            print("需要安装 pygetwindow: pip install pygetwindow")
            return False
        except Exception as e:
            print(f"激活窗口失败: {e}")
            return False
    
    def send_keys_to_window(self, window_title, keys):
        """
        向指定窗口发送按键
        :param window_title: 窗口标题
        :param keys: 要发送的按键或文本
        :return: 是否成功发送
        """
        try:
            import pyautogui
            
            # 先激活窗口
            if self.activate_window(window_title):
                time.sleep(1)
                
                # 发送按键
                pyautogui.typewrite(keys)
                print(f"已向窗口 '{window_title}' 发送: {keys}")
                return True
            else:
                return False
                
        except Exception as e:
            print(f"发送按键失败: {e}")
            return False
    
    def take_screenshot(self, filename=None):
        """
        截图
        :param filename: 保存的文件名
        :return: 文件路径
        """
        try:
            import pyautogui
            from datetime import datetime
            
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_{timestamp}.png"
            
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            print(f"截图已保存: {filename}")
            return filename
            
        except Exception as e:
            print(f"截图失败: {e}")
            return None
    
    def wait_for_window(self, window_title, timeout=30):
        """
        等待窗口出现
        :param window_title: 窗口标题
        :param timeout: 超时时间（秒）
        :return: 是否找到窗口
        """
        try:
            import pygetwindow as gw
            
            start_time = time.time()
            while time.time() - start_time < timeout:
                windows = gw.getWindowsWithTitle(window_title)
                if windows:
                    print(f"找到窗口: {window_title}")
                    return True
                time.sleep(1)
            
            print(f"等待超时，未找到窗口: {window_title}")
            return False
            
        except ImportError:
            print("需要安装 pygetwindow: pip install pygetwindow")
            return False
        except Exception as e:
            print(f"等待窗口失败: {e}")
            return False


# ==================== 使用示例 ====================

def example_open_doctor_workstation():
    """打开医生工作站示例"""
    rpa = RpaWindowsTool()
    
    print("\n" + "=" * 60)
    print("示例：打开医生工作站程序")
    print("=" * 60)
    
    # 方法1：直接指定完整路径
    # rpa.open_application(r"D:\医生工作站\DocProject.exe")
    
    # 方法2：使用便捷方法（推荐）
    success = rpa.open_doctor_workstation()
    
    if success:
        print("✓ 医生工作站已成功打开")
    else:
        print("✗ 打开医生工作站失败")
    
    print("\n任务完成！")


def example_open_doctor_workstation_v2():
    """打开医生工作站V2示例"""
    rpa = RpaWindowsTool()
    
    print("\n" + "=" * 60)
    print("示例：打开医生工作站V2程序")
    print("=" * 60)
    
    success = rpa.open_doctor_workstation_v2()
    
    if success:
        print("✓ 医生工作站V2已成功打开")
    else:
        print("✗ 打开医生工作站V2失败")
    
    print("\n任务完成！")


if __name__ == "__main__":
    print("=" * 60)
    print("Windows RPA工具 - 医生工作站自动化")
    print("=" * 60)
    print("\n可用功能:")
    print("1. open_application - 打开任意Windows程序")
    print("2. open_doctor_workstation - 打开医生工作站")
    print("3. open_doctor_workstation_v2 - 打开医生工作站V2")
    print("4. close_application - 关闭应用程序")
    print("5. activate_window - 激活窗口")
    print("6. send_keys_to_window - 向窗口发送按键")
    print("7. take_screenshot - 截图")
    print("8. wait_for_window - 等待窗口出现")
    print("\n运行示例...")
    
    # 运行打开医生工作站示例
    example_open_doctor_workstation()
    
    print("\n提示: 使用前请安装依赖包:")
    print("pip install pyautogui pygetwindow")
