"""
Time    : 2026/6/11 20:57
人生的事情并不是一帆风顺，总会有碰碰磕磕的，但是你要坚持下来
file1    : RPAproject
file    : rpademo.py
Author : Li
"""

import pyautogui
import time
import keyboard
import pandas as pd
import os
from datetime import datetime
import json


class RPATool:
    """RPA自动化工具类"""
    
    def __init__(self):
        """初始化RPA工具"""
        pyautogui.FAILSAFE = True  # 启用故障保护（鼠标移到屏幕角落可停止）
        pyautogui.PAUSE = 0.5  # 每次操作后暂停0.5秒
        print("RPA工具已初始化")
    
    # ==================== 鼠标操作 ====================
    
    def click(self, x=None, y=None, clicks=1, button='left'):
        """
        点击鼠标
        :param x: X坐标，如果为None则使用当前位置
        :param y: Y坐标，如果为None则使用当前位置
        :param clicks: 点击次数
        :param button: 按钮类型 'left', 'right', 'middle'
        """
        if x is not None and y is not None:
            pyautogui.moveTo(x, y)
        pyautogui.click(clicks=clicks, button=button)
        print(f"鼠标{button}键点击 {clicks} 次")
    
    def double_click(self, x=None, y=None):
        """双击鼠标"""
        self.click(x, y, clicks=2, button='left')
        print("鼠标双击")
    
    def right_click(self, x=None, y=None):
        """右键点击"""
        self.click(x, y, clicks=1, button='right')
        print("鼠标右键点击")
    
    def move_to(self, x, y, duration=0.5):
        """
        移动鼠标到指定位置
        :param x: X坐标
        :param y: Y坐标
        :param duration: 移动耗时（秒）
        """
        pyautogui.moveTo(x, y, duration=duration)
        print(f"鼠标移动到 ({x}, {y})")
    
    def drag_to(self, x, y, duration=0.5):
        """
        拖拽鼠标到指定位置
        :param x: X坐标
        :param y: Y坐标
        :param duration: 拖拽耗时（秒）
        """
        pyautogui.dragTo(x, y, duration=duration)
        print(f"鼠标拖拽到 ({x}, {y})")
    
    def scroll(self, clicks):
        """
        滚动鼠标滚轮
        :param clicks: 滚动量，正数向上，负数向下
        """
        pyautogui.scroll(clicks)
        print(f"鼠标滚轮滚动 {clicks}")
    
    def get_mouse_position(self):
        """获取当前鼠标位置"""
        pos = pyautogui.position()
        print(f"当前鼠标位置: {pos}")
        return pos
    
    # ==================== 键盘操作 ====================
    
    def type_text(self, text, interval=0.1):
        """
        输入文本
        :param text: 要输入的文本
        :param interval: 每个字符之间的间隔（秒）
        """
        pyautogui.typewrite(text, interval=interval)
        print(f"输入文本: {text}")
    
    def press_key(self, key):
        """
        按下按键
        :param key: 按键名称，如 'enter', 'tab', 'esc' 等
        """
        pyautogui.press(key)
        print(f"按下按键: {key}")
    
    def hotkey(self, *keys):
        """
        按下组合键
        :param keys: 按键列表，如 ('ctrl', 'c')
        """
        pyautogui.hotkey(*keys)
        print(f"按下组合键: {'+'.join(keys)}")
    
    def key_down(self, key):
        """按住按键"""
        pyautogui.keyDown(key)
        print(f"按住按键: {key}")
    
    def key_up(self, key):
        """释放按键"""
        pyautogui.keyUp(key)
        print(f"释放按键: {key}")
    
    # ==================== 屏幕操作 ====================
    
    def screenshot(self, filename=None, region=None):
        """
        截图
        :param filename: 保存文件名，如果为None则自动生成
        :param region: 截图区域 (left, top, width, height)
        :return: 截图文件路径
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
        
        if region:
            img = pyautogui.screenshot(region=region)
        else:
            img = pyautogui.screenshot()
        
        img.save(filename)
        print(f"截图已保存: {filename}")
        return filename
    
    def locate_on_screen(self, image_path, confidence=0.9, timeout=10):
        """
        在屏幕上查找图像
        :param image_path: 图像文件路径
        :param confidence: 匹配置信度 (0-1)
        :param timeout: 超时时间（秒）
        :return: 找到的位置 (x, y) 或 None
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                if location:
                    center = pyautogui.center(location)
                    print(f"找到图像，位置: {center}")
                    return center
            except Exception as e:
                pass
            time.sleep(0.5)
        
        print(f"未找到图像: {image_path}")
        return None
    
    def wait_for_image(self, image_path, confidence=0.9, timeout=30):
        """
        等待图像出现
        :param image_path: 图像文件路径
        :param confidence: 匹配置信度
        :param timeout: 超时时间（秒）
        :return: 是否找到
        """
        result = self.locate_on_screen(image_path, confidence, timeout)
        return result is not None
    
    # ==================== 窗口操作 ====================
    
    def activate_window(self, window_title):
        """
        激活窗口
        :param window_title: 窗口标题
        """
        try:
            import pygetwindow as gw
            window = gw.getWindowsWithTitle(window_title)
            if window:
                window[0].activate()
                print(f"已激活窗口: {window_title}")
                return True
        except:
            print("需要安装 pygetwindow: pip install pygetwindow")
        return False
    
    def minimize_window(self, window_title):
        """最小化窗口"""
        try:
            import pygetwindow as gw
            window = gw.getWindowsWithTitle(window_title)
            if window:
                window[0].minimize()
                print(f"已最小化窗口: {window_title}")
        except:
            pass
    
    def maximize_window(self, window_title):
        """最大化窗口"""
        try:
            import pygetwindow as gw
            window = gw.getWindowsWithTitle(window_title)
            if window:
                window[0].maximize()
                print(f"已最大化窗口: {window_title}")
        except:
            pass
    
    # ==================== 数据处理 ====================
    
    def read_excel(self, filepath, sheet_name=0):
        """
        读取Excel文件
        :param filepath: Excel文件路径
        :param sheet_name: 工作表名称或索引
        :return: DataFrame
        """
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        print(f"读取Excel文件: {filepath}, 共 {len(df)} 行")
        return df
    
    def write_excel(self, df, filepath, sheet_name='Sheet1'):
        """
        写入Excel文件
        :param df: DataFrame数据
        :param filepath: 输出文件路径
        :param sheet_name: 工作表名称
        """
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"数据已写入: {filepath}")
    
    def read_csv(self, filepath, encoding='utf-8'):
        """
        读取CSV文件
        :param filepath: CSV文件路径
        :param encoding: 编码格式
        :return: DataFrame
        """
        df = pd.read_csv(filepath, encoding=encoding)
        print(f"读取CSV文件: {filepath}, 共 {len(df)} 行")
        return df
    
    def write_csv(self, df, filepath, encoding='utf-8-sig'):
        """
        写入CSV文件
        :param df: DataFrame数据
        :param filepath: 输出文件路径
        :param encoding: 编码格式
        """
        df.to_csv(filepath, index=False, encoding=encoding)
        print(f"数据已写入: {filepath}")
    
    def read_json(self, filepath):
        """读取JSON文件"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"读取JSON文件: {filepath}")
        return data
    
    def write_json(self, data, filepath):
        """写入JSON文件"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"数据已写入: {filepath}")
    
    # ==================== 文件操作 ====================
    
    def list_files(self, directory, pattern='*'):
        """
        列出目录下的文件
        :param directory: 目录路径
        :param pattern: 文件匹配模式
        :return: 文件列表
        """
        import glob
        files = glob.glob(os.path.join(directory, pattern))
        print(f"目录 {directory} 下找到 {len(files)} 个文件")
        return files
    
    def copy_file(self, src, dst):
        """复制文件"""
        import shutil
        shutil.copy2(src, dst)
        print(f"文件已复制: {src} -> {dst}")
    
    def move_file(self, src, dst):
        """移动文件"""
        import shutil
        shutil.move(src, dst)
        print(f"文件已移动: {src} -> {dst}")
    
    def delete_file(self, filepath):
        """删除文件"""
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"文件已删除: {filepath}")
        else:
            print(f"文件不存在: {filepath}")
    
    def create_directory(self, directory):
        """创建目录"""
        os.makedirs(directory, exist_ok=True)
        print(f"目录已创建: {directory}")
    
    # ==================== 等待和延时 ====================
    
    def wait(self, seconds):
        """等待指定秒数"""
        print(f"等待 {seconds} 秒...")
        time.sleep(seconds)
    
    def wait_until(self, condition_func, timeout=60, interval=1):
        """
        等待直到条件满足
        :param condition_func: 条件函数，返回True/False
        :param timeout: 超时时间（秒）
        :param interval: 检查间隔（秒）
        :return: 是否成功
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if condition_func():
                print("条件已满足")
                return True
            time.sleep(interval)
        print(f"等待超时: {timeout}秒")
        return False
    
    # ==================== 实用工具 ====================
    
    def get_current_time(self, format_str="%Y-%m-%d %H:%M:%S"):
        """获取当前时间字符串"""
        return datetime.now().strftime(format_str)
    
    def log_message(self, message, log_file="rpa_log.txt"):
        """
        记录日志
        :param message: 日志消息
        :param log_file: 日志文件路径
        """
        timestamp = self.get_current_time()
        log_entry = f"[{timestamp}] {message}\n"
        
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        
        print(log_entry.strip())
    
    def run_workflow(self, workflow_name, steps):
        """
        运行工作流程
        :param workflow_name: 工作流名称
        :param steps: 步骤列表，每个步骤是字典 {'action': 方法名, 'args': 参数}
        """
        self.log_message(f"开始执行工作流: {workflow_name}")
        
        for i, step in enumerate(steps, 1):
            action = step.get('action')
            args = step.get('args', {})
            
            self.log_message(f"步骤 {i}: {action}")
            
            if hasattr(self, action):
                try:
                    method = getattr(self, action)
                    method(**args)
                except Exception as e:
                    self.log_message(f"步骤 {i} 执行失败: {str(e)}")
                    raise
            else:
                self.log_message(f"未知操作: {action}")
        
        self.log_message(f"工作流 {workflow_name} 执行完成")
    
    # ==================== macOS 专用功能 ====================
    
    def open_chrome_on_mac(self):
        """
        在Mac上打开Chrome浏览器
        """
        import subprocess
        try:
            subprocess.run(['open', '-a', 'Google Chrome'], check=True)
            print("已打开Chrome浏览器")
            time.sleep(2)  # 等待浏览器启动
            return True
        except Exception as e:
            print(f"打开Chrome失败: {e}")
            return False
    
    def search_baidu(self, keyword):
        """
        在百度上搜索关键词
        :param keyword: 搜索关键词
        """
        # 激活Chrome窗口
        self.activate_window("Chrome")
        time.sleep(1)
        
        # 使用AppleScript打开百度并搜索
        import subprocess
        
        # 对关键词进行URL编码
        from urllib.parse import quote
        encoded_keyword = quote(keyword)
        baidu_url = f"https://www.baidu.com/s?wd={encoded_keyword}"
        
        # 使用AppleScript在Chrome中打开URL
        script = f'''
        tell application "Google Chrome"
            activate
            if (count of windows) is 0 then
                make new window
            end if
            set URL of active tab of front window to "{baidu_url}"
        end tell
        '''
        
        try:
            subprocess.run(['osascript', '-e', script], check=True)
            print(f"已在百度搜索: {keyword}")
            return True
        except Exception as e:
            print(f"搜索失败: {e}")
            return False
    
    def open_url_in_chrome(self, url):
        """
        在Chrome中打开指定URL
        :param url: 网址
        """
        import subprocess
        script = f'''
        tell application "Google Chrome"
            activate
            if (count of windows) is 0 then
                make new window
            end if
            set URL of active tab of front window to "{url}"
        end tell
        '''
        
        try:
            subprocess.run(['osascript', '-e', script], check=True)
            print(f"已打开URL: {url}")
            return True
        except Exception as e:
            print(f"打开URL失败: {e}")
            return False
    
    # ==================== 微信自动化功能 ====================
    
    def open_wechat_on_mac(self):
        """
        在Mac上打开微信
        """
        import subprocess
        try:
            subprocess.run(['open', '-a', 'WeChat'], check=True)
            print("已打开微信")
            time.sleep(3)  # 等待微信启动
            return True
        except Exception as e:
            print(f"打开微信失败: {e}")
            return False
    
    def send_wechat_message(self, contact_name, message):
        """
        向微信联系人发送消息
        :param contact_name: 联系人名称
        :param message: 要发送的消息内容
        """
        import subprocess
        
        # 对特殊字符进行转义，防止AppleScript出错
        escaped_contact = contact_name.replace('"', '\\"').replace('\\', '\\\\')
        escaped_message = message.replace('"', '\\"').replace('\\', '\\\\')
        
        # 使用AppleScript控制微信
        script = f'''
        tell application "WeChat"
            activate
        end tell
        
        delay 2
        
        tell application "System Events"
            tell process "WeChat"
                -- 点击搜索框 (Cmd+F)
                keystroke "f" using command down
                delay 1
                
                -- 清除搜索框内容 (Cmd+A, Delete)
                keystroke "a" using command down
                delay 0.3
                key code 51
                delay 0.5
                
                -- 使用剪贴板输入联系人名称（更可靠，支持中文）
                set the clipboard to "{escaped_contact}"
                delay 0.3
                keystroke "v" using command down
                delay 3
                
                -- 等待搜索结果加载
                delay 2
                
                -- 直接按回车选择第一个匹配结果（微信默认行为）
                key code 36
                delay 3
                
                -- 输入消息前切换到英文输入法
                key code 49 using control down
                delay 0.8
                
                -- 使用剪贴板输入消息（支持中文）
                set the clipboard to "{escaped_message}"
                delay 0.3
                keystroke "v" using command down
                delay 1
                
                -- 按回车发送消息
                key code 36
            end tell
        end tell
        '''
        
        try:
            subprocess.run(['osascript', '-e', script], check=True)
            print(f"已向 {contact_name} 发送消息: {message}")
            return True
        except Exception as e:
            print(f"发送消息失败: {e}")
            return False
    
    def search_wechat_contact(self, contact_name):
        """
        在微信中搜索联系人（不发送消息）
        :param contact_name: 联系人名称
        """
        import subprocess
        
        script = f'''
        tell application "WeChat"
            activate
        end tell
        
        delay 1
        
        tell application "System Events"
            tell process "WeChat"
                -- 点击搜索框 (Cmd+F)
                keystroke "f" using command down
                delay 0.5
                
                -- 输入联系人名称
                keystroke "{contact_name}"
                delay 1
                
                -- 按回车选择联系人
                key code 36
            end tell
        end tell
        '''
        
        try:
            subprocess.run(['osascript', '-e', script], check=True)
            print(f"已搜索联系人: {contact_name}")
            return True
        except Exception as e:
            print(f"搜索联系人失败: {e}")
            return False


# ==================== 使用示例 ====================

def example_basic_operations():
    """基础操作示例"""
    rpa = RPATool()
    
    # 获取鼠标位置
    rpa.get_mouse_position()
    
    # 移动鼠标并点击
    rpa.move_to(100, 100)
    rpa.click()
    
    # 输入文本
    rpa.type_text("Hello RPA!")
    
    # 按下回车键
    rpa.press_key('enter')
    
    # 截图
    rpa.screenshot("example.png")


def example_data_processing():
    """数据处理示例"""
    rpa = RPATool()
    
    # 创建示例数据
    data = {
        '姓名': ['张三', '李四', '王五'],
        '年龄': [25, 30, 35],
        '城市': ['北京', '上海', '广州']
    }
    df = pd.DataFrame(data)
    
    # 写入Excel
    rpa.write_excel(df, "output.xlsx")
    
    # 写入CSV
    rpa.write_csv(df, "output.csv")
    
    # 读取CSV
    df_read = rpa.read_csv("output.csv")
    print(df_read)


def example_workflow():
    """工作流示例"""
    rpa = RPATool()
    
    # 定义工作流步骤
    steps = [
        {
            'action': 'log_message',
            'args': {'message': '开始自动化任务'}
        },
        {
            'action': 'wait',
            'args': {'seconds': 2}
        },
        {
            'action': 'get_mouse_position',
            'args': {}
        },
        {
            'action': 'log_message',
            'args': {'message': '任务完成'}
        }
    ]
    
    # 执行工作流
    rpa.run_workflow("示例工作流", steps)


def example_send_wechat():
    """在Mac上打开微信并发送消息示例"""
    rpa = RPATool()
    
    print("\n" + "=" * 50)
    print("示例：向微信联系人'赵新光'发送消息")
    print("=" * 50)
    
    # 打开微信
    rpa.open_wechat_on_mac()
    
    # 向赵新光发送消息"好的"
    rpa.send_wechat_message("LHM", "rpa发送---你可以的，继续努力")

    print("\n任务完成！")


def example_send_wechat_periodic(contact_name="LHM", message="rpa发送---你可以的，继续努力", interval=60, count=10):
    """
    定时发送微信消息
    :param contact_name: 联系人名称
    :param message: 消息内容
    :param interval: 发送间隔（秒），默认60秒
    :param count: 发送次数，默认10次
    """
    rpa = RPATool()
    
    print("\n" + "=" * 60)
    print(f"定时任务：每 {interval} 秒向 '{contact_name}' 发送消息")
    print(f"消息内容：{message}")
    print(f"发送次数：{count} 次")
    print("=" * 60)
    
    # 打开微信（只需要打开一次）
    if not rpa.open_wechat_on_mac():
        print("打开微信失败，任务终止")
        return
    
    for i in range(1, count + 1):
        print(f"\n[{i}/{count}] 开始第 {i} 次发送...")
        print(f"时间: {rpa.get_current_time()}")
        
        # 发送消息
        success = rpa.send_wechat_message(contact_name, message)
        
        if success:
            print(f"✓ 第 {i} 次发送成功")
        else:
            print(f"✗ 第 {i} 次发送失败")
        
        # 如果不是最后一次，等待指定间隔
        if i < count:
            print(f"等待 {interval} 秒后发送下一次...")
            rpa.wait(interval)
    
    print("\n" + "=" * 60)
    print("定时任务完成！")
    print("=" * 60)


def example_search_baidu():
    """在Mac上打开Chrome并在百度搜索示例"""
    rpa = RPATool()
    
    print("\n" + "=" * 50)
    print("示例：在百度搜索'直播吧'")
    print("=" * 50)
    
    # 打开Chrome浏览器
    rpa.open_chrome_on_mac()
    
    # 在百度搜索"直播吧"
    rpa.search_baidu("直播吧")
    
    print("\n任务完成！")


if __name__ == "__main__":
    print("=" * 50)
    print("RPA自动化工具")
    print("=" * 50)
    print("\n可用功能:")
    print("1. 鼠标操作: click, move_to, drag_to, scroll")
    print("2. 键盘操作: type_text, press_key, hotkey")
    print("3. 屏幕操作: screenshot, locate_on_screen")
    print("4. 窗口操作: activate_window, minimize_window")
    print("5. 数据处理: read_excel, write_excel, read_csv, write_csv")
    print("6. 文件操作: list_files, copy_file, move_file")
    print("7. 工作流: run_workflow")
    print("8. macOS专用: open_chrome_on_mac, search_baidu, open_url_in_chrome")
    print("9. 微信自动化: open_wechat_on_mac, send_wechat_message, search_wechat_contact")
    print("\n运行示例...")
    
    # 运行定时发送消息示例（每60秒发一次，共发10次）
    # 你可以修改参数：
    # contact_name: 联系人名称
    # message: 消息内容
    # interval: 间隔时间（秒）
    # count: 发送次数
    example_send_wechat_periodic(
        contact_name="LHM",
        message="rpa发送---你可以的，继续努力",
        interval=30,  # 60秒 = 1分钟
        count=10      # 发送10次
    )
    
    print("\n提示: 使用前请安装依赖包:")
    print("pip install pyautogui pandas openpyxl keyboard pygetwindow")
    print("\n注意: 微信自动化需要在系统偏好设置中授予辅助功能权限")
