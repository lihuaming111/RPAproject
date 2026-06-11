# RPA程序 Windows Server 2012 离线打包部署指南

## 📋 概述

本指南说明如何将 RpaLis.py 打包成可在 Windows Server 2012（无外网环境）上运行的 exe 文件。

---

## 🎯 方案选择

### 方案一：直接打包成exe（推荐）
**优点**：目标机器无需安装Python和依赖库，直接运行exe即可  
**缺点**：exe文件较大（约50-100MB）

### 方案二：离线安装依赖后运行py文件
**优点**：文件较小，便于更新代码  
**缺点**：需要在目标机器上安装Python和依赖库

---

## 🚀 方案一：打包成exe文件

### 步骤1：在有外网的机器上准备环境

1. **安装必要工具**
```bash
pip install pyinstaller pyautogui pygetwindow Pillow pywin32
```

2. **下载打包脚本**
确保以下文件在项目目录中：
- `RpaLis.py` - 主程序
- `build_exe.py` - 打包脚本

### 步骤2：执行打包

在有外网的Windows机器上执行：
```bash
python build_exe.py
```

或在项目目录右键使用PyInstaller：
```bash
pyinstaller --onefile --windowed RpaLis.py
```

### 步骤3：获取生成的exe文件

打包完成后，在 `dist` 目录下找到 `RpaLis.exe`

### 步骤4：部署到Windows Server 2012

1. 将 `RpaLis.exe` 复制到 Windows Server 2012
2. 双击运行即可

**注意**：如果程序需要访问特定路径（如 D:\医生工作站），请确保该路径存在且有相应权限。

---

## 🔧 方案二：离线安装依赖

### 步骤1：在有外网的机器上下载依赖包

1. **执行下载脚本**
```bash
python download_packages.py
```

这会创建 `packages` 文件夹，包含所有需要的 .whl 文件

2. **或者手动下载**
```bash
mkdir packages
pip download -d ./packages pyautogui pygetwindow Pillow pywin32 PyInstaller
```

### 步骤2：复制依赖包到目标机器

将整个 `packages` 文件夹复制到 Windows Server 2012

### 步骤3：在Windows Server 2012上安装Python

1. 下载 Python 3.8+ 安装包（从其他机器拷贝）
2. 安装Python，勾选 "Add Python to PATH"
3. 验证安装：
```bash
python --version
pip --version
```

### 步骤4：离线安装依赖包

在 `packages` 文件夹所在目录执行：
```bash
pip install --no-index --find-links=./packages pyautogui pygetwindow Pillow pywin32
```

### 步骤5：运行程序

```bash
python RpaLis.py
```

---

## ⚠️ 常见问题解决

### 问题1：Windows Server 2012缺少Visual C++运行库

**症状**：运行exe时报错 "找不到 VCRUNTIME140.dll"

**解决方案**：
1. 从有外网的机器下载 Visual C++ Redistributable for Visual Studio 2015-2022
2. 复制到目标机器并安装
3. 下载地址：https://aka.ms/vs/17/release/vc_redist.x64.exe

### 问题2：权限不足

**症状**：无法打开 D:\医生工作站 或截图失败

**解决方案**：
1. 右键 exe 文件 → "以管理员身份运行"
2. 或修改文件夹权限，允许当前用户访问

### 问题3：窗口控制功能失效

**症状**：activate_window 或 send_keys_to_window 不工作

**解决方案**：
1. 确保安装了 pywin32
2. 检查是否有多个同名窗口
3. 增加等待时间

### 问题4：打包后的exe体积过大

**解决方案**：
1. 使用 `--exclude-module` 排除不需要的模块
2. 示例：
```bash
pyinstaller --onefile --windowed --exclude-module=tkinter --exclude-module=PIL._tkinter_finder RpaLis.py
```

---

## 📦 完整的离线部署包结构

```
RPA_Deployment/
── dist/
│   └── RpaLis.exe              # 打包好的可执行文件
├── packages/                    # 离线依赖包（方案二需要）
│   ├── pyautogui-xxx.whl
│   ├── pygetwindow-xxx.whl
│   ├── Pillow-xxx.whl
│   └── pywin32-xxx.whl
├── RpaLis.py                   # 源代码
├── build_exe.py                # 打包脚本
├── download_packages.py        # 依赖下载脚本
└── README_DEPLOY.txt           # 本文档
```

---

## ✅ 验证部署成功

在 Windows Server 2012 上运行后，应该看到：

1. ✓ 程序正常启动
2. ✓ 能够打开 D:\医生工作站\DocProject.exe
3. ✓ 能够进行窗口控制和截图
4. ✓ 没有报错信息

---

## 📞 技术支持

如遇问题，请检查：
1. Python版本是否兼容（建议 3.8+）
2. 所有依赖是否正确安装
3. 文件路径是否正确
4. 是否有足够的系统权限

---

## 🔄 更新程序

如果需要更新程序代码：

**方案一（exe）**：重新执行打包流程，替换旧的exe文件

**方案二（py）**：直接替换 RpaLis.py 文件即可

---

*最后更新: 2026/6/11*
