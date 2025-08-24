#!/usr/bin/env python3
"""
创建 macOS 应用程序包的脚本
"""

import os
import shutil
import subprocess
from pathlib import Path

def create_app_bundle():
    """创建 macOS 应用程序包"""
    
    app_name = "Qoder Reset Tool"
    bundle_name = f"{app_name}.app"
    
    # 创建应用程序包结构
    app_path = Path(bundle_name)
    contents_path = app_path / "Contents"
    macos_path = contents_path / "MacOS"
    resources_path = contents_path / "Resources"
    
    # 清理旧的包
    if app_path.exists():
        shutil.rmtree(app_path)
    
    # 创建目录结构
    macos_path.mkdir(parents=True)
    resources_path.mkdir(parents=True)
    
    # 创建 Info.plist
    info_plist = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>qoder_reset_gui</string>
    <key>CFBundleIdentifier</key>
    <string>com.local.qoder-reset-tool</string>
    <key>CFBundleName</key>
    <string>{app_name}</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.9</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>NSRequiresAquaSystemAppearance</key>
    <false/>
</dict>
</plist>"""
    
    with open(contents_path / "Info.plist", 'w') as f:
        f.write(info_plist)
    
    # 创建启动脚本
    launcher_script = f"""#!/bin/bash
cd "$(dirname "$0")/../Resources"

# 设置环境变量
export TK_SILENCE_DEPRECATION=1

# 启动GUI程序
if [ -f "qoder_reset_gui.py" ]; then
    echo "启动 Qoder Reset GUI..."
    python3 qoder_reset_gui.py
else
    echo "错误: 未找到GUI程序文件"
    exit 1
fi
"""
    
    launcher_path = macos_path / "qoder_reset_gui"
    with open(launcher_path, 'w') as f:
        f.write(launcher_script)
    
    # 设置执行权限
    os.chmod(launcher_path, 0o755)
    
    # 复制资源文件
    files_to_copy = [
        "qoder_reset_gui.py",
        "README.md"
    ]
    
    for file_name in files_to_copy:
        if Path(file_name).exists():
            shutil.copy2(file_name, resources_path)
    
    print(f"✅ 应用程序包已创建: {bundle_name}")
    print(f"📁 位置: {app_path.absolute()}")
    print("\n使用方法:")
    print(f"1. 双击 {bundle_name} 启动应用程序")
    print("2. 或者拖拽到应用程序文件夹中")
    
    return app_path

def main():
    """主函数"""
    print("=" * 50)
    print("创建 Qoder Reset Tool 应用程序包")
    print("=" * 50)
    
    # 检查必要文件
    required_files = ["qoder_reset_gui.py"]
    missing_files = [f for f in required_files if not Path(f).exists()]
    
    if missing_files:
        print(f"❌ 缺少必要文件: {', '.join(missing_files)}")
        return False
    
    try:
        app_path = create_app_bundle()
        
        # 询问是否要移动到应用程序文件夹
        response = input("\n是否要将应用程序移动到 /Applications 文件夹? (y/N): ")
        if response.lower() in ['y', 'yes']:
            apps_dir = Path("/Applications")
            target_path = apps_dir / app_path.name
            
            if target_path.exists():
                print(f"⚠️  {target_path} 已存在，正在替换...")
                shutil.rmtree(target_path)
            
            shutil.move(str(app_path), str(apps_dir))
            print(f"✅ 应用程序已移动到: {target_path}")
            print("现在可以从启动台或应用程序文件夹启动了！")
        
        return True
        
    except Exception as e:
        print(f"❌ 创建应用程序包失败: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
