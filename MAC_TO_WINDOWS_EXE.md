# Mac用户打包Windows EXE的3种方法

##  方法对比

| 方法 | 难度 | 速度 | 推荐度 | 说明 |
|------|------|------|--------|------|
| GitHub Actions | ⭐ | 快 | ⭐⭐⭐⭐⭐ | **最推荐**，完全自动化 |
| 在线Windows虚拟机 | ⭐ | 中 | ⭐⭐⭐⭐ | 简单直接 |
| Docker交叉编译 | ⭐⭐⭐⭐ | 慢 | ⭐⭐ | 复杂，不推荐 |

---

## ✅ 方法一：GitHub Actions（强烈推荐）

### 优点
- ✓ 不需要Windows机器
- ✓ 完全自动化
- ✓ 每次提交代码自动打包
- ✓ 免费使用

### 操作步骤

#### 1. 将代码上传到GitHub

```bash
# 初始化git（如果还没有）
cd /Users/li/PycharmProjects/RPAproject
git init
git add .
git commit -m "Initial commit"

# 在GitHub上创建新仓库，然后关联
git remote add origin https://github.com/你的用户名/RPAproject.git
git push -u origin main
```

#### 2. 触发自动打包

**方式A：推送代码自动触发**
```bash
git push origin main
```

**方式B：手动触发**
1. 进入GitHub仓库页面
2. 点击 "Actions" 标签
3. 点击左侧 "Build Windows EXE"
4. 点击右侧 "Run workflow" → "Run workflow"

#### 3. 下载生成的EXE

1. 等待打包完成（约3-5分钟）
2. 点击 "Actions" → 最新的运行记录
3. 在页面底部找到 "Artifacts"
4. 点击 "RpaLis-Windows-EXE" 下载
5. 解压后得到 `RpaLis.exe`

### 配置文件已创建
我已经为你创建了 `.github/workflows/build-windows.yml`，直接使用即可！

---

## ✅ 方法二：使用在线Windows虚拟机

### 推荐服务

#### 1. GitHub Codespaces（免费）
- 网址：https://github.com/codespaces
- 每月免费60小时
- 操作：
  1. 在GitHub仓库点击 "Code" → "Codespaces" → "Create codespace"
  2. 选择Windows环境（如果有）或使用远程桌面连接真实Windows
  3. 在终端执行：
     ```bash
     pip install pyinstaller pyautogui pygetwindow Pillow pywin32
     pyinstaller --onefile --windowed RpaLis.py
     ```
  4. 下载 `dist/RpaLis.exe`

#### 2. Azure DevTest Labs（有免费额度）
- 网址：https://azure.microsoft.com/free/
- 注册Azure免费账号
- 创建Windows Server虚拟机
- 远程桌面连接后打包

#### 3. AWS WorkSpaces（试用）
- 网址：https://aws.amazon.com/workspaces/
- 有免费试用期
- 创建Windows工作空间后打包

---

## ⚠️ 方法三：Docker交叉编译（不推荐）

### 缺点
- 配置复杂
- 打包速度慢
- 可能遇到兼容性问题

### 如果你一定要用

```bash
# 构建Docker镜像
docker build -f Dockerfile.windows -t rpa-windows-builder .

# 运行打包
docker run -v $(pwd):/app rpa-windows-builder

# 获取生成的exe
ls dist/RpaLis.exe
```

---

## 🚀 快速开始（推荐流程）

### 使用GitHub Actions的完整流程

```bash
# 1. 确保项目目录有以下文件
cd /Users/li/PycharmProjects/RPAproject
ls -la
# 应该看到：
# - RpaLis.py
# - .github/workflows/build-windows.yml

# 2. 初始化Git并推送到GitHub
git init
git add .
git commit -m "Add RPA project with GitHub Actions"

# 3. 在GitHub创建仓库（网页操作）
#    - 访问 https://github.com/new
#    - 创建名为 RPAproject 的仓库
#    - 不要勾选 "Initialize this repository with a README"

# 4. 关联远程仓库并推送
git remote add origin https://github.com/你的用户名/RPAproject.git
git branch -M main
git push -u origin main

# 5. 查看打包进度
#    - 访问 https://github.com/你的用户名/RPAproject/actions
#    - 等待3-5分钟

# 6. 下载EXE
#    - 在Actions页面点击下载artifact
#    - 解压得到 RpaLis.exe
```

---

## 💡 提示

1. **首次使用GitHub Actions需要授权**
   - 推送代码后，GitHub会询问是否启用Actions
   - 点击 "Enable" 即可

2. **如果打包失败**
   - 检查 `.github/workflows/build-windows.yml` 是否正确
   - 查看Actions页面的日志输出
   - 确保 `RpaLis.py` 没有语法错误

3. **更新程序后重新打包**
   - 修改代码后执行：
     ```bash
     git add .
     git commit -m "Update RpaLis"
     git push
     ```
   - GitHub Actions会自动重新打包

4. **下载的文件**
   - GitHub Actions生成的是zip压缩包
   - 解压后得到 `RpaLis.exe`
   - 可以直接在Windows Server 2012上运行

---

##  常见问题

### Q: 我没有GitHub账号怎么办？
A: 注册一个免费的GitHub账号：https://github.com/signup

### Q: GitHub Actions收费吗？
A: 对公开仓库完全免费，私有仓库每月有2000分钟免费额度。

### Q: 打包后的exe能在Windows Server 2012运行吗？
A: 可以，但可能需要安装Visual C++ Redistributable（从其他Windows机器拷贝安装）。

### Q: 如何测试打包是否成功？
A: 
1. 下载exe后在任意Windows机器上双击运行
2. 看是否能正常打开医生工作站
3. 或找一台Windows虚拟机测试

---

##  总结

**对于Mac用户，最佳方案是GitHub Actions：**
1. ✓ 不需要Windows机器
2. ✓ 配置简单（我已经帮你创建好了）
3. ✓ 完全自动化
4. ✓ 免费使用

现在你只需要：
1. 将代码推送到GitHub
2. 等待自动打包完成
3. 下载exe文件

就这么简单！
