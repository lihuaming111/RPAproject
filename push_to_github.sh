#!/bin/bash
# 快速推送到GitHub并触发Actions打包

echo "=========================================="
echo "推送RPA项目到GitHub"
echo "=========================================="
echo ""

cd /Users/li/PycharmProjects/RPAproject

echo "1. 检查Git状态..."
git status

echo ""
echo "2. 当前分支: $(git branch --show-current)"


echo ""
echo "3. 远程仓库: $(git remote get-url origin)"

echo ""
echo "4. 准备推送..."
echo ""
echo "⚠️  注意："
echo "   - 如果使用HTTPS，需要输入GitHub用户名和个人访问令牌(PAT)"
echo "   - 如果使用SSH，需要先配置SSH密钥到GitHub"
echo ""
echo " 获取个人访问令牌(PAT)的方法："
echo "   1. 访问: https://github.com/settings/tokens"
echo "   2. 点击 'Generate new token (classic)'"
echo "   3. 勾选 'repo' 权限"
echo "   4. 生成并复制令牌"
echo ""

read -p "按回车键开始推送（或按Ctrl+C取消）..."

echo ""
echo "开始推送..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ 推送成功！"
    echo "=========================================="
    echo ""
    echo "接下来："
    echo "1. 访问: https://github.com/lihuaming111/RPAproject/actions"
    echo "2. 等待 'Build Windows EXE' 完成（约3-5分钟）"
    echo "3. 下载生成的 RpaLis.exe"
    echo ""
else
    echo ""
    echo "=========================================="
    echo "✗ 推送失败"
    echo "=========================================="
    echo ""
    echo "可能的原因："
    echo "1. 认证失败 - 需要使用个人访问令牌而不是密码"
    echo "2. SSH密钥未配置 - 需要添加SSH公钥到GitHub"
    echo ""
    echo "建议：使用 GitHub Desktop 图形界面操作更简单"
    echo "下载地址: https://desktop.github.com/"
    echo ""
fi
