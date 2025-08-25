#!/usr/bin/env python3
"""
Qoder Reset Tool - 现代化GUI版本
使用PyQt5实现，完全按照用户原型图设计
"""

import os
import sys
import json
import uuid
import shutil
import hashlib
import subprocess
import webbrowser
import platform
from pathlib import Path
from datetime import datetime

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
except ImportError:
    print("错误: 未安装PyQt5")
    print("请运行: pip install PyQt5")
    sys.exit(1)

class QoderResetGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_language = 'zh'  # 默认中文
        self.init_translations()
        self.init_ui()
    
    def init_translations(self):
        """初始化多语言字典"""
        self.translations = {
            'zh': {  # 中文
                'window_title': 'Qoder-Free',
                'intro_text': 'Qoder-Free主要用于重置Qoder应用程序的用户身份信息',
                'operation_area': '操作区域:',
                'one_click_config': '一键修改配置',
                'close_qoder': '关闭Qoder',
                'reset_machine_id': '重置机器ID',
                'reset_telemetry': '重置遥测数据',
                'deep_identity_clean': '深度身份清理',
                'login_identity_clean': '清理登录身份',
                'advanced_options': '高级选项',
                'preserve_chat': '保留对话记录',
                'operation_log': '操作日志:',
                'clear_log': '清空日志',
                'github': 'Github',
                'language': '语言',
                
                # 日志消息
                'tool_started': 'Qoder-Free 重置工具已启动',
                'log_cleared': '日志已清空',
                'qoder_running': 'Qoder正在运行',
                'qoder_not_running': 'Qoder未运行',
                'qoder_directory_exists': 'Qoder目录存在',
                'machine_id': '机器ID',
                'telemetry_machine_id': '遥测机器ID',
                'device_id': '设备ID',
                'cache_directories_found': '个缓存目录',
                'chat_directories_found': '个对话相关目录',
                'identity_files_found': '个身份识别文件',
                'status_check_complete': '状态检查完成，可以开始操作',
                
                # 对话框消息
                'qoder_detected_running': '检测到 Qoder 正在运行',
                'please_close_qoder': '请手动关闭 Qoder 应用程序',
                'confirm_one_click': '确认一键修改',
                'confirm_deep_clean': '确认深度清理',
                'confirm_login_clean': '确认清理登录身份',
                'operation_complete': '操作完成',
                'operation_failed': '操作失败',
                'error': '错误',
                'success': '成功',
                'warning': '警告',
                'status_check': '状态检查'
            },
            'en': {  # English
                'window_title': 'Qoder-Free',
                'intro_text': 'Qoder-Free is mainly used to reset user identity information of Qoder application',
                'operation_area': 'Operation Area:',
                'one_click_config': 'One-Click Configuration',
                'close_qoder': 'Close Qoder',
                'reset_machine_id': 'Reset Machine ID',
                'reset_telemetry': 'Reset Telemetry',
                'deep_identity_clean': 'Deep Identity Cleanup',
                'login_identity_clean': 'Clean Login Identity',
                'advanced_options': 'Advanced Options',
                'preserve_chat': 'Preserve Chat History',
                'operation_log': 'Operation Log:',
                'clear_log': 'Clear Log',
                'github': 'Github',
                'language': 'Language',
                
                # Log messages
                'tool_started': 'Qoder-Free reset tool started',
                'log_cleared': 'Log cleared',
                'qoder_running': 'Qoder is running',
                'qoder_not_running': 'Qoder is not running',
                'qoder_directory_exists': 'Qoder directory exists',
                'machine_id': 'Machine ID',
                'telemetry_machine_id': 'Telemetry Machine ID',
                'device_id': 'Device ID',
                'cache_directories_found': 'cache directories found',
                'chat_directories_found': 'chat-related directories found',
                'identity_files_found': 'identity files found',
                'status_check_complete': 'Status check completed, ready to operate',
                
                # Dialog messages
                'qoder_detected_running': 'Qoder Detected Running',
                'please_close_qoder': 'Please close Qoder application manually',
                'confirm_one_click': 'Confirm One-Click Reset',
                'confirm_deep_clean': 'Confirm Deep Cleanup',
                'confirm_login_clean': 'Confirm Login Identity Cleanup',
                'operation_complete': 'Operation Complete',
                'operation_failed': 'Operation Failed',
                'error': 'Error',
                'success': 'Success',
                'warning': 'Warning',
                'status_check': 'Status Check'
            },
            'ru': {  # Русский
                'window_title': 'Qoder-Free',
                'intro_text': 'Qoder-Free в основном используется для сброса пользовательской информации приложения Qoder',
                'operation_area': 'Область операций:',
                'one_click_config': 'Одним кликом',
                'close_qoder': 'Закрыть Qoder',
                'reset_machine_id': 'Сбросить ID машины',
                'reset_telemetry': 'Сбросить телеметрию',
                'deep_identity_clean': 'Глубокая очистка',
                'login_identity_clean': 'Очистить вход',
                'advanced_options': 'Дополнительно',
                'preserve_chat': 'Сохранить чат',
                'operation_log': 'Журнал операций:',
                'clear_log': 'Очистить журнал',
                'github': 'Github',
                'language': 'Язык',

                # Log messages
                'tool_started': 'Инструмент сброса Qoder-Free запущен',
                'log_cleared': 'Журнал очищен',
                'qoder_running': 'Qoder запущен',
                'qoder_not_running': 'Qoder не запущен',
                'qoder_directory_exists': 'Папка Qoder существует',
                'machine_id': 'ID машины',
                'telemetry_machine_id': 'ID машины телеметрии',
                'device_id': 'ID устройства',
                'cache_directories_found': 'папок кеша найдено',
                'chat_directories_found': 'папок чата найдено',
                'identity_files_found': 'файлов идентификации найдено',
                'status_check_complete': 'Проверка статуса завершена, готов к работе',

                # Dialog messages
                'qoder_detected_running': 'Обнаружен запущенный Qoder',
                'please_close_qoder': 'Пожалуйста, закройте приложение Qoder вручную',
                'confirm_one_click': 'Подтвердить сброс одним кликом',
                'confirm_deep_clean': 'Подтвердить глубокую очистку',
                'confirm_login_clean': 'Подтвердить очистку входа',
                'operation_complete': 'Операция завершена',
                'operation_failed': 'Операция не удалась',
                'error': 'Ошибка',
                'success': 'Успех',
                'warning': 'Предупреждение',
                'status_check': 'Проверка статуса'
            },
            'pt-br': {  # Português (Brasil)
                'window_title': 'Qoder-Free',
                'intro_text': 'Qoder-Free é principalmente usado para redefinir as informações de identidade do usuário do aplicativo Qoder',
                'operation_area': 'Área de Operações:',
                'one_click_config': 'Configuração com um clique',
                'close_qoder': 'Fechar Qoder',
                'reset_machine_id': 'Redefinir ID da Máquina',
                'reset_telemetry': 'Redefinir Telemetria',
                'deep_identity_clean': 'Limpeza Profunda de Identidade',
                'login_identity_clean': 'Limpar Login',
                'advanced_options': 'Opções Avançadas',
                'preserve_chat': 'Preservar Histórico do chat',
                'operation_log': 'Log de Operações:',
                'clear_log': 'Limpar Log',
                'github': 'Github',
                'language': 'Idioma',

                # Log messages
                'tool_started': 'Ferramenta de redefinição Qoder-Free iniciada',
                'log_cleared': 'Log limpo',
                'qoder_running': 'Qoder está em execução',
                'qoder_not_running': 'Qoder não está em execução',
                'qoder_directory_exists': 'Diretório Qoder existe',
                'machine_id': 'ID da Máquina',
                'telemetry_machine_id': 'ID da Máquina de Telemetria',
                'device_id': 'ID do Dispositivo',
                'cache_directories_found': 'diretórios de cache encontrados',
                'chat_directories_found': 'diretórios relacionados ao chat encontrados',
                'identity_files_found': 'arquivos de identidade encontrados',
                'status_check_complete': 'Verificação de status concluída, pronto para operar',

                # Dialog messages
                'qoder_detected_running': 'Qoder Detectado em Execução',
                'please_close_qoder': 'Por favor, feche o aplicativo Qoder manualmente',
                'confirm_one_click': 'Confirmar Redefinição com um clique',
                'confirm_deep_clean': 'Confirmar Limpeza Profunda',
                'confirm_login_clean': 'Confirmar Limpeza de Identidade de Login',
                'operation_complete': 'Operação Concluída',
                'operation_failed': 'Operação Falhou',
                'error': 'Erro',
                'success': 'Sucesso',
                'warning': 'Aviso',
                'status_check': 'Verificação de Status'
            }
        }
    
    def tr(self, key):
        """获取当前语言的翻译文本"""
        return self.translations.get(self.current_language, {}).get(key, key)
    
    def init_ui(self):
        """初始化用户界面"""
        self.setWindowTitle(self.tr('window_title'))
        self.setFixedSize(800, 1000)
        self.setStyleSheet("background-color: white;")
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 30, 40, 30)
        main_layout.setSpacing(20)
        
        # 添加右上角语言切换组件
        top_layout = QHBoxLayout()
        top_layout.addStretch()  # 推到右侧
        
        # 语言标签
        lang_label = QLabel(self.tr('language') + ":")
        lang_label.setStyleSheet("""
            QLabel {
                font-size: 11px;
                color: #666666;
                margin-right: 5px;
            }
        """)
        top_layout.addWidget(lang_label)
        
        # 语言下拉框
        self.language_combo = QComboBox()
        self.language_combo.addItems(['中文', 'English', 'Русский', 'Português (BR)'])
        self.language_combo.setFixedSize(90, 25)
        self.language_combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #dadce0;
                border-radius: 3px;
                padding: 2px 8px;
                font-size: 10px;
                color: #333333;
            }
            QComboBox::drop-down {
                border: none;
                width: 18px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 4px solid #666;
                margin-top: 2px;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                border: 1px solid #dadce0;
                selection-background-color: #e8f0fe;
                font-size: 10px;
            }
        """)
        self.language_combo.currentTextChanged.connect(self.change_language)
        top_layout.addWidget(self.language_combo)
        
        main_layout.addLayout(top_layout)
        
        # 1. 标题
        self.title_label = QLabel(self.tr('window_title'))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: black;
                margin-bottom: 10px;
            }
        """)
        main_layout.addWidget(self.title_label)
        
        # 2. 说明文字
        self.intro_label = QLabel(self.tr('intro_text'))
        self.intro_label.setAlignment(Qt.AlignCenter)
        self.intro_label.setStyleSheet("""
            QLabel {
                font-size: 12px;
                color: #666666;
                margin-bottom: 20px;
            }
        """)
        main_layout.addWidget(self.intro_label)
        
        # 3. 操作区域标题
        self.operation_title = QLabel(self.tr('operation_area'))
        self.operation_title.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: black;
                margin-bottom: 10px;
            }
        """)
        main_layout.addWidget(self.operation_title)
        
        # 4. 蓝色横幅按钮
        self.one_click_btn = QPushButton(self.tr('one_click_config'))
        self.one_click_btn.setFixedSize(300, 40)  # 设置固定宽度300px，高度40px
        self.one_click_btn.setStyleSheet("""
            QPushButton {
                background-color: #4285f4;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3367d6;
            }
            QPushButton:pressed {
                background-color: #2851a3;
            }
        """)
        self.one_click_btn.clicked.connect(self.one_click_reset)
        
        # 将按钮居中显示
        button_center_layout = QHBoxLayout()
        button_center_layout.addStretch()
        button_center_layout.addWidget(self.one_click_btn)
        button_center_layout.addStretch()
        main_layout.addLayout(button_center_layout)
        
        # 5. 四个操作按钮（扩展为2x2布局）
        button_layout = QVBoxLayout()
        
        # 第一行按钮
        button_row1 = QHBoxLayout()
        button_row1.setSpacing(15)
        
        # 关闭Qoder按钮 (红色)
        self.close_qoder_btn = QPushButton(self.tr('close_qoder'))
        self.close_qoder_btn.setFixedSize(150, 40)
        self.close_qoder_btn.setStyleSheet("""
            QPushButton {
                background-color: #ea4335;
                color: white;
                font-size: 12px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #d33b2c;
            }
            QPushButton:pressed {
                background-color: #b52d20;
            }
        """)
        self.close_qoder_btn.clicked.connect(self.close_qoder)
        button_row1.addWidget(self.close_qoder_btn)
        
        # 重置机器ID按钮 (蓝色)
        self.reset_machine_id_btn = QPushButton(self.tr('reset_machine_id'))
        self.reset_machine_id_btn.setFixedSize(150, 40)
        self.reset_machine_id_btn.setStyleSheet("""
            QPushButton {
                background-color: #4285f4;
                color: white;
                font-size: 12px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3367d6;
            }
            QPushButton:pressed {
                background-color: #2851a3;
            }
        """)
        self.reset_machine_id_btn.clicked.connect(self.reset_machine_id)
        button_row1.addWidget(self.reset_machine_id_btn)
        
        button_layout.addLayout(button_row1)
        
        # 第二行按钮
        button_row2 = QHBoxLayout()
        button_row2.setSpacing(15)
        
        # 重置遥测数据按钮 (蓝色)
        self.reset_telemetry_btn = QPushButton(self.tr('reset_telemetry'))
        self.reset_telemetry_btn.setFixedSize(150, 40)
        self.reset_telemetry_btn.setStyleSheet("""
            QPushButton {
                background-color: #4285f4;
                color: white;
                font-size: 12px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3367d6;
            }
            QPushButton:pressed {
                background-color: #2851a3;
            }
        """)
        self.reset_telemetry_btn.clicked.connect(self.reset_telemetry)
        button_row2.addWidget(self.reset_telemetry_btn)
        
        # 深度身份清理按钮 (橙色，新增)
        self.deep_clean_btn = QPushButton(self.tr('deep_identity_clean'))
        self.deep_clean_btn.setFixedSize(150, 40)
        self.deep_clean_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff9800;
                color: white;
                font-size: 12px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #f57c00;
            }
            QPushButton:pressed {
                background-color: #e65100;
            }
        """)
        self.deep_clean_btn.clicked.connect(self.deep_identity_cleanup)
        button_row2.addWidget(self.deep_clean_btn)
        
        # 第三行按钮（新增）
        button_row3 = QHBoxLayout()
        button_row3.setSpacing(15)
        
        # 清理登录身份按钮 (紫色，新增)
        self.login_clean_btn = QPushButton(self.tr('login_identity_clean'))
        self.login_clean_btn.setFixedSize(150, 40)
        self.login_clean_btn.setStyleSheet("""
            QPushButton {
                background-color: #673ab7;
                color: white;
                font-size: 12px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5e35b1;
            }
            QPushButton:pressed {
                background-color: #512da8;
            }
        """)
        self.login_clean_btn.clicked.connect(self.login_identity_cleanup)
        button_row3.addWidget(self.login_clean_btn)
        
        # 占位按钮（保持布局均衡）
        self.placeholder_btn = QPushButton(self.tr('advanced_options'))
        self.placeholder_btn.setFixedSize(150, 40)
        self.placeholder_btn.setEnabled(False)
        self.placeholder_btn.setStyleSheet("""
            QPushButton {
                background-color: #e0e0e0;
                color: #9e9e9e;
                font-size: 12px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
        """)
        button_row3.addWidget(self.placeholder_btn)
        
        button_layout.addLayout(button_row3)
        main_layout.addLayout(button_layout)

        # 5.5. 保留对话记录勾选框
        self.preserve_chat_checkbox = QCheckBox(self.tr('preserve_chat'))
        self.preserve_chat_checkbox.setChecked(True)  # 默认勾选
        self.preserve_chat_checkbox.setStyleSheet("""
            QCheckBox {
                color: black;
                font-size: 12px;
                font-weight: bold;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #4285f4;
                border-radius: 3px;
                background-color: white;
            }
            QCheckBox::indicator:checked {
                background-color: #4285f4;
                border: 2px solid #4285f4;
            }
            QCheckBox::indicator:checked:hover {
                background-color: #3367d6;
                border: 2px solid #3367d6;
            }
        """)

        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(self.preserve_chat_checkbox)
        checkbox_layout.addStretch()
        main_layout.addLayout(checkbox_layout)

        # 6. 操作日志区域
        self.log_title = QLabel(self.tr('operation_log'))
        self.log_title.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: black;
                margin-top: 10px;
                margin-bottom: 10px;
            }
        """)
        main_layout.addWidget(self.log_title)
        
        # 日志文本框
        self.log_text = QTextEdit()
        self.log_text.setFixedHeight(380)  # 设置固定高度以显示更多日志行
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #f8f9fa;
                color: #333333;
                border: 1px solid #dadce0;
                border-radius: 5px;
                font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
                font-size: 11px;
                padding: 10px;
            }
        """)
        self.log_text.setReadOnly(True)
        main_layout.addWidget(self.log_text)
        
        # 清空日志按钮 (右下角)
        clear_layout = QHBoxLayout()
        clear_layout.addStretch()
        
        self.clear_log_btn = QPushButton(self.tr('clear_log'))
        self.clear_log_btn.setFixedSize(100, 30)
        self.clear_log_btn.setStyleSheet("""
            QPushButton {
                background-color: #9aa0a6;
                color: white;
                font-size: 11px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #80868b;
            }
            QPushButton:pressed {
                background-color: #5f6368;
            }
        """)
        self.clear_log_btn.clicked.connect(self.clear_log)
        clear_layout.addWidget(self.clear_log_btn)
        
        main_layout.addLayout(clear_layout)
        
        # 7. 底部GitHub链接
        self.github_btn = QPushButton(self.tr('github'))
        self.github_btn.setFixedSize(120, 40)
        self.github_btn.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                color: white;
                font-size: 11px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QPushButton:pressed {
                background-color: #222222;
            }
        """)
        self.github_btn.clicked.connect(self.open_github)
        
        github_layout = QHBoxLayout()
        github_layout.addStretch()
        github_layout.addWidget(self.github_btn)
        github_layout.addStretch()
        main_layout.addLayout(github_layout)
        
        # 添加初始日志
        self.log(self.tr('tool_started'))
        self.log("=" * 50)
        self.initialize_status_check()
    
    def change_language(self, language_text):
        """切换语言"""
        language_map = {
            '中文': 'zh',
            'English': 'en',
            'Русский': 'ru',
            'Português (BR)': 'pt-br'
        }
        
        new_language = language_map.get(language_text, 'zh')
        if new_language != self.current_language:
            self.current_language = new_language
            self.update_ui_text()
    
    def update_ui_text(self):
        """更新界面文本"""
        # 更新窗口标题
        self.setWindowTitle(self.tr('window_title'))
        
        # 更新标签文本
        self.title_label.setText(self.tr('window_title'))
        self.intro_label.setText(self.tr('intro_text'))
        self.operation_title.setText(self.tr('operation_area'))
        self.log_title.setText(self.tr('operation_log'))
        
        # 更新按钮文本
        self.one_click_btn.setText(self.tr('one_click_config'))
        self.close_qoder_btn.setText(self.tr('close_qoder'))
        self.reset_machine_id_btn.setText(self.tr('reset_machine_id'))
        self.reset_telemetry_btn.setText(self.tr('reset_telemetry'))
        self.deep_clean_btn.setText(self.tr('deep_identity_clean'))
        self.login_clean_btn.setText(self.tr('login_identity_clean'))
        self.placeholder_btn.setText(self.tr('advanced_options'))
        self.clear_log_btn.setText(self.tr('clear_log'))
        self.github_btn.setText(self.tr('github'))
        
        # 更新复选框文本
        self.preserve_chat_checkbox.setText(self.tr('preserve_chat'))
        
        # 清空日志并重新初始化
        self.log_text.clear()
        self.log(self.tr('tool_started'))
        self.log("=" * 50)
    
    def log(self, message):
        """添加日志消息"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        self.log_text.append(log_message)

        # 自动滚动到最新日志
        scrollbar = self.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def clear_log(self):
        """清空日志"""
        self.log_text.clear()
        self.log(self.tr('log_cleared'))

    def initialize_status_check(self):
        """初始化时检查各项状态"""
        try:
            # 1. 检查Qoder进程状态
            self.log("1. 检查Qoder进程状态...")
            is_running, pids = self.check_qoder_running()
            if is_running:
                self.log(f"   ✅ Qoder正在运行 (PID: {', '.join(pids)})")
            else:
                self.log("   ✅ Qoder未运行")

            # 2. 检查Qoder目录
            self.log("2. 检查Qoder目录...")
            home_dir = Path.home()
            qoder_support_dir = home_dir / "Library/Application Support/Qoder"

            if qoder_support_dir.exists():
                self.log(f"   ✅ Qoder目录存在")

                # 3. 检查机器ID文件
                self.log("3. 检查机器ID文件...")
                machine_id_file = qoder_support_dir / "machineid"
                if machine_id_file.exists():
                    try:
                        with open(machine_id_file, 'r') as f:
                            current_id = f.read().strip()
                        self.log(f"   ✅ 机器ID: {current_id}")
                    except Exception as e:
                        self.log(f"   ❌ 读取机器ID失败: {e}")
                else:
                    self.log("   ❌ 机器ID文件不存在")

                # 4. 检查遥测数据文件
                self.log("4. 检查遥测数据文件...")
                storage_json_file = qoder_support_dir / "User/globalStorage/storage.json"
                if storage_json_file.exists():
                    try:
                        with open(storage_json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)

                        if 'telemetry.machineId' in data:
                            machine_id = data['telemetry.machineId']
                            self.log(f"   ✅ 遥测机器ID: {machine_id[:16]}...")
                        else:
                            self.log("   ⚠️  未找到遥测机器ID")

                        if 'telemetry.devDeviceId' in data:
                            device_id = data['telemetry.devDeviceId']
                            self.log(f"   ✅ 设备ID: {device_id}")
                        else:
                            self.log("   ⚠️  未找到设备ID")

                    except Exception as e:
                        self.log(f"   ❌ 读取遥测数据失败: {e}")
                else:
                    self.log("   ❌ 遥测数据文件不存在")

                # 5. 检查缓存目录
                self.log("5. 检查缓存目录...")
                cache_dirs = [
                    "Cache", "blob_storage", "Code Cache", "SharedClientCache",
                    "GPUCache", "DawnGraphiteCache", "DawnWebGPUCache"
                ]

                cache_count = 0
                for cache_dir in cache_dirs:
                    cache_path = qoder_support_dir / cache_dir
                    if cache_path.exists():
                        cache_count += 1

                self.log(f"   ✅ 发现 {cache_count}/{len(cache_dirs)} 个缓存目录")

                # 6. 检查对话记录相关目录
                self.log("6. 检查对话记录...")
                chat_dirs = [
                    "User/workspaceStorage", "User/History", "logs", "CachedData"
                ]

                chat_count = 0
                for chat_dir in chat_dirs:
                    chat_path = qoder_support_dir / chat_dir
                    if chat_path.exists():
                        chat_count += 1

                self.log(f"   ✅ 发现 {chat_count}/{len(chat_dirs)} 个对话相关目录")
                
                # 7. 检查身份识别文件（新增）
                self.log("7. 检查身份识别文件...")
                identity_files = [
                    "Network Persistent State", "Cookies", "SharedStorage", 
                    "Trust Tokens", "TransportSecurity", "Preferences"
                ]
                
                identity_count = 0
                for identity_file in identity_files:
                    file_path = qoder_support_dir / identity_file
                    if file_path.exists():
                        identity_count += 1
                
                self.log(f"   ✅ 发现 {identity_count}/{len(identity_files)} 个身份识别文件")
                
                # 8. 检查 SharedClientCache 内部文件
                self.log("8. 检查 SharedClientCache 内部文件...")
                shared_cache = qoder_support_dir / "SharedClientCache"
                if shared_cache.exists():
                    critical_files = [".info", ".lock", "mcp.json"]
                    shared_count = 0
                    for file_name in critical_files:
                        if (shared_cache / file_name).exists():
                            shared_count += 1
                    
                    # 检查 index 目录
                    if (shared_cache / "index").exists():
                        shared_count += 1
                    
                    self.log(f"   ✅ SharedClientCache 内部文件: {shared_count}/4 个")
                else:
                    self.log("   ⚠️  SharedClientCache 目录不存在")
                
                # 9. 检查 Keychain 和证书存储（新增）
                self.log("9. 检查 Keychain 和证书存储...")
                keychain_files = [
                    "cert_transparency_reporter_state.json",
                    "Certificate Revocation Lists",
                    "SSLCertificates"
                ]
                
                keychain_count = 0
                for keychain_file in keychain_files:
                    file_path = qoder_support_dir / keychain_file
                    if file_path.exists():
                        keychain_count += 1
                
                self.log(f"   ✅ 发现 {keychain_count}/{len(keychain_files)} 个证书/安全文件")
                
                # 10. 检查用户活动记录（新增）
                self.log("10. 检查用户活动记录...")
                activity_files = [
                    "ActivityLog", "EventLog", "UserActivityLog",
                    "Login Credentials", "Web Data", "Web Data-journal"
                ]
                
                activity_count = 0
                for activity_file in activity_files:
                    file_path = qoder_support_dir / activity_file
                    if file_path.exists():
                        activity_count += 1
                
                self.log(f"   ✅ 发现 {activity_count}/{len(activity_files)} 个活动记录文件")
                
                # 11. 检查设备指纹相关文件（新增）
                self.log("11. 检查设备指纹相关文件...")
                fingerprint_files = [
                    "DeviceMetadata", "HardwareInfo", "SystemInfo",
                    "QuotaManager", "QuotaManager-journal",
                    "databases/Databases.db", "databases/Databases.db-journal"
                ]
                
                fingerprint_count = 0
                for fingerprint_file in fingerprint_files:
                    file_path = qoder_support_dir / fingerprint_file
                    if file_path.exists():
                        fingerprint_count += 1
                
                self.log(f"   ✅ 发现 {fingerprint_count}/{len(fingerprint_files)} 个设备指纹文件")

            else:
                self.log("   ❌ Qoder目录不存在")
                self.log("   请确保已安装Qoder应用程序")

            self.log("=" * 50)
            self.log("状态检查完成，可以开始操作")

        except Exception as e:
            self.log(f"❌ 状态检查失败: {e}")
            self.log("=" * 50)
    
    def check_qoder_running(self):
        """检查Qoder是否正在运行"""
        try:
            result = subprocess.run(['pgrep', '-f', 'Qoder'],
                                  capture_output=True, text=True)
            if result.returncode == 0:
                pids = result.stdout.strip().split('\n')
                return True, pids
        except:
            pass
        return False, []

    def close_qoder(self):
        """关闭Qoder"""
        self.log("正在检查 Qoder 运行状态...")

        is_running, pids = self.check_qoder_running()

        if is_running:
            self.log(f"检测到 Qoder 正在运行 (PID: {', '.join(pids)})")
            self.log("请手动关闭 Qoder 应用程序")
            QMessageBox.information(self, "检测到 Qoder 正在运行",
                                  f"检测到 Qoder 正在运行 (PID: {', '.join(pids)})\n\n"
                                  "请手动关闭 Qoder 应用程序：\n"
                                  "1. 使用 Cmd+Q 快捷键\n"
                                  "2. 或从菜单选择 Qoder → 退出 Qoder")
        else:
            self.log("Qoder 未运行")
            QMessageBox.information(self, "状态检查", "Qoder 当前未运行")

    def login_identity_cleanup(self):
        """专门清理登录相关身份信息"""
        self.log("开始清理登录相关身份信息...")

        # 检查Qoder是否在运行
        is_running, pids = self.check_qoder_running()
        if is_running:
            reply = QMessageBox.question(self, "检测到 Qoder 正在运行",
                                       f"检测到 Qoder 正在运行 (PID: {', '.join(pids)})\n\n"
                                       "登录身份清理需要先关闭 Qoder。\n"
                                       "请手动关闭后点击'Yes'继续。",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply != QMessageBox.Yes:
                self.log("用户取消操作")
                return

            # 再次检查
            is_running, _ = self.check_qoder_running()
            if is_running:
                self.log("Qoder 仍在运行，操作取消")
                QMessageBox.critical(self, "错误", "请先完全关闭 Qoder 应用程序")
                return

        # 确认操作
        reply = QMessageBox.question(self, "确认清理登录身份",
                                   f"登录身份清理将：\n\n"
                                   f"• 清除所有登录证书和 Cookies\n"
                                   f"• 清除 SharedClientCache 登录状态\n"
                                   f"• 清除网络状态和会话存储\n"
                                   f"• 清除设备认证信息\n"
                                   f"• 清除 nonce 和 challenge 相关数据\n\n"
                                   f"这将使 Qoder 无法识别之前的登录状态，确定继续吗？",
                                   QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            self.log("用户取消登录身份清理")
            return

        try:
            home_dir = Path.home()
            qoder_support_dir = home_dir / "Library/Application Support/Qoder"
            
            if not qoder_support_dir.exists():
                raise Exception("未找到 Qoder 应用数据目录")
            
            self.log("=" * 40)
            self.log("开始登录身份清理")
            self.log("=" * 40)
            
            # 执行登录身份清理
            self.perform_login_identity_cleanup(qoder_support_dir)
            
            self.log("=" * 40)
            self.log("登录身份清理完成！")
            self.log("=" * 40)
            
            QMessageBox.information(self, "完成", "登录身份清理完成！\n现在可以重新启动 Qoder。")
            
        except Exception as e:
            self.log(f"登录身份清理失败: {e}")
            QMessageBox.critical(self, "错误", f"登录身份清理失败: {e}")
    
    def perform_login_identity_cleanup(self, qoder_support_dir):
        """执行登录相关身份清理"""
        try:
            self.log("开始清理登录相关身份信息...")
            cleaned_count = 0
            
            # 1. 清理 SharedClientCache 中的登录状态文件
            self.log("1. 清理 SharedClientCache 登录状态...")
            shared_cache = qoder_support_dir / "SharedClientCache"
            if shared_cache.exists():
                # 清理关键的登录相关文件
                login_files = [".info", ".lock", "mcp.json", "server.json", "auth.json"]
                for file_name in login_files:
                    file_path = shared_cache / file_name
                    if file_path.exists():
                        try:
                            file_path.unlink()
                            self.log(f"   已清除: SharedClientCache/{file_name}")
                            cleaned_count += 1
                        except Exception as e:
                            self.log(f"   清除失败 {file_name}: {e}")
                
                # 清理所有临时文件
                import glob
                temp_pattern = str(shared_cache / "tmp*")
                temp_files = glob.glob(temp_pattern)
                for temp_file in temp_files:
                    try:
                        Path(temp_file).unlink()
                        self.log(f"   已清除: {Path(temp_file).name}")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 {Path(temp_file).name}: {e}")
            
            # 2. 清理登录证书和认证文件
            self.log("2. 清理登录证书和认证文件...")
            auth_files = [
                "Login Credentials", "Login Data", "Login Data-journal",
                "Cookies", "Cookies-journal",
                "Network Persistent State",
                "cert_transparency_reporter_state.json",
                "TransportSecurity",
                "Trust Tokens", "Trust Tokens-journal"
            ]
            
            for auth_file in auth_files:
                file_path = qoder_support_dir / auth_file
                if file_path.exists():
                    try:
                        file_path.unlink()
                        self.log(f"   已清除: {auth_file}")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 {auth_file}: {e}")
            
            # 3. 清理会话和状态存储
            self.log("3. 清理会话和状态存储...")
            session_dirs = [
                "Session Storage",
                "Local Storage",
                "WebStorage",
                "SharedStorage",
                "Shared Dictionary"
            ]
            
            for session_dir in session_dirs:
                dir_path = qoder_support_dir / session_dir
                if dir_path.exists():
                    try:
                        shutil.rmtree(dir_path)
                        self.log(f"   已清除: {session_dir}")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 {session_dir}: {e}")
            
            # 4. 清理用户配置中的登录相关信息
            self.log("4. 清理用户配置中的登录信息...")
            storage_json_file = qoder_support_dir / "User/globalStorage/storage.json"
            if storage_json_file.exists():
                try:
                    with open(storage_json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # 清除登录相关的配置键
                    login_keys = []
                    for key in data.keys():
                        if any(keyword in key.lower() for keyword in [
                            'login', 'auth', 'token', 'credential', 'session',
                            'nonce', 'challenge', 'device', 'account', 'user'
                        ]):
                            login_keys.append(key)
                    
                    if login_keys:
                        for key in login_keys:
                            del data[key]
                            self.log(f"   已清除配置: {key}")
                        
                        with open(storage_json_file, 'w', encoding='utf-8') as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)
                        
                        cleaned_count += len(login_keys)
                        self.log(f"   已清除 {len(login_keys)} 个登录相关配置")
                    else:
                        self.log("   未找到登录相关配置")
                
                except Exception as e:
                    self.log(f"   清理用户配置失败: {e}")
            
            # 5. 清理设备指纹和认证数据
            self.log("5. 清理设备指纹和认证数据...")
            device_files = [
                "DeviceMetadata", "HardwareInfo", "SystemInfo",
                "origin_bound_certs", "AutofillStrikeDatabase",
                "AutofillStrikeDatabase-journal", "Feature Engagement Tracker"
            ]
            
            for device_file in device_files:
                file_path = qoder_support_dir / device_file
                if file_path.exists():
                    try:
                        if file_path.is_dir():
                            shutil.rmtree(file_path)
                        else:
                            file_path.unlink()
                        self.log(f"   已清除: {device_file}")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 {device_file}: {e}")
            
            self.log(f"   登录身份清理完成，处理了 {cleaned_count} 个项目")
            
        except Exception as e:
            self.log(f"   登录身份清理失败: {e}")

    def deep_identity_cleanup(self):
        """深度身份清理功能"""
        self.log("开始深度身份清理...")

        # 检查Qoder是否在运行
        is_running, pids = self.check_qoder_running()
        if is_running:
            reply = QMessageBox.question(self, "检测到 Qoder 正在运行",
                                       f"检测到 Qoder 正在运行 (PID: {', '.join(pids)})\n\n"
                                       "深度清理需要先关闭 Qoder。\n"
                                       "请手动关闭后点击'Yes'继续。",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply != QMessageBox.Yes:
                self.log("用户取消操作")
                return

            # 再次检查
            is_running, _ = self.check_qoder_running()
            if is_running:
                self.log("Qoder 仍在运行，操作取消")
                QMessageBox.critical(self, "错误", "请先完全关闭 Qoder 应用程序")
                return

        # 确认操作
        reply = QMessageBox.question(self, "确认深度清理",
                                   f"深度身份清理将：\n\n"
                                   f"• 清除所有网络状态和 Cookie\n"
                                   f"• 清除所有本地存储数据\n"
                                   f"• 清除 SharedClientCache 内部文件\n"
                                   f"• 清除系统级别身份文件\n"
                                   f"• 清除崩溃报告和缓存数据\n\n"
                                   f"这是最强力的身份重置，确定继续吗？",
                                   QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            self.log("用户取消深度清理")
            return

        try:
            home_dir = Path.home()
            qoder_support_dir = home_dir / "Library/Application Support/Qoder"
            
            if not qoder_support_dir.exists():
                raise Exception("未找到 Qoder 应用数据目录")
            
            self.log("=" * 40)
            self.log("开始深度身份清理")
            self.log("=" * 40)
            
            # 执行高级身份清理
            self.perform_advanced_identity_cleanup(qoder_support_dir, preserve_chat=False)
            
            self.log("=" * 40)
            self.log("深度身份清理完成！")
            self.log("=" * 40)
            
            QMessageBox.information(self, "完成", "深度身份清理完成！\n现在可以重新启动 Qoder。")
            
        except Exception as e:
            self.log(f"深度清理失败: {e}")
            QMessageBox.critical(self, "错误", f"深度清理失败: {e}")

    def reset_machine_id(self):
        """重置机器ID"""
        self.log("开始重置机器ID...")

        # 检查Qoder是否在运行
        is_running, _ = self.check_qoder_running()
        if is_running:
            self.log("错误: Qoder 正在运行，请先关闭")
            QMessageBox.critical(self, "错误", "请先关闭 Qoder 应用程序")
            return

        try:
            home_dir = Path.home()
            qoder_support_dir = home_dir / "Library/Application Support/Qoder"
            machine_id_file = qoder_support_dir / "machineid"

            if not qoder_support_dir.exists():
                raise Exception("未找到 Qoder 应用数据目录")

            if machine_id_file.exists():
                new_machine_id = str(uuid.uuid4())
                with open(machine_id_file, 'w') as f:
                    f.write(new_machine_id)
                self.log(f"机器ID已重置为: {new_machine_id}")
                QMessageBox.information(self, "成功", "机器ID重置完成")
            else:
                self.log("未找到机器ID文件")
                QMessageBox.warning(self, "警告", "未找到机器ID文件")

        except Exception as e:
            self.log(f"重置机器ID失败: {e}")
            QMessageBox.critical(self, "错误", f"重置机器ID失败: {e}")

    def reset_telemetry(self):
        """重置遥测数据"""
        self.log("开始重置遥测数据...")

        # 检查Qoder是否在运行
        is_running, _ = self.check_qoder_running()
        if is_running:
            self.log("错误: Qoder 正在运行，请先关闭")
            QMessageBox.critical(self, "错误", "请先关闭 Qoder 应用程序")
            return

        try:
            home_dir = Path.home()
            qoder_support_dir = home_dir / "Library/Application Support/Qoder"
            storage_json_file = qoder_support_dir / "User/globalStorage/storage.json"

            if not storage_json_file.exists():
                raise Exception("未找到遥测数据文件")

            with open(storage_json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 生成新的遥测ID
            new_uuid = str(uuid.uuid4())
            machine_id_hash = hashlib.sha256(new_uuid.encode()).hexdigest()
            device_id = str(uuid.uuid4())

            data['telemetry.machineId'] = machine_id_hash
            data['telemetry.devDeviceId'] = device_id

            with open(storage_json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            self.log("遥测数据已重置")
            self.log(f"新遥测机器ID: {machine_id_hash[:16]}...")
            self.log(f"新设备ID: {device_id}")
            QMessageBox.information(self, "成功", "遥测数据重置完成")

        except Exception as e:
            self.log(f"重置遥测数据失败: {e}")
            QMessageBox.critical(self, "错误", f"重置遥测数据失败: {e}")

    def one_click_reset(self):
        """一键修改所有配置"""
        self.log("开始一键修改所有配置...")

        # 检查Qoder是否在运行
        is_running, pids = self.check_qoder_running()
        if is_running:
            reply = QMessageBox.question(self, "检测到 Qoder 正在运行",
                                       f"检测到 Qoder 正在运行 (PID: {', '.join(pids)})\n\n"
                                       "一键修改需要先关闭 Qoder。\n"
                                       "请手动关闭后点击'Yes'继续。",
                                       QMessageBox.Yes | QMessageBox.No)
            if reply != QMessageBox.Yes:
                self.log("用户取消操作")
                return

            # 再次检查
            is_running, _ = self.check_qoder_running()
            if is_running:
                self.log("Qoder 仍在运行，操作取消")
                QMessageBox.critical(self, "错误", "请先完全关闭 Qoder 应用程序")
                return

        # 确认操作
        preserve_chat = self.preserve_chat_checkbox.isChecked()
        chat_action = "保留对话记录" if preserve_chat else "清除对话记录"

        reply = QMessageBox.question(self, "确认一键修改",
                                   f"一键修改所有配置将：\n\n"
                                   f"• 重置机器ID\n"
                                   f"• 重置遥测数据\n"
                                   f"• 清理缓存数据\n"
                                   f"• 清理身份识别文件 (Cookies, 网络状态等)\n"
                                   f"• 执行高级身份清理 (SharedClientCache 等)\n"
                                   f"• {chat_action}\n\n"
                                   f"这是最全面的重置方案，确定继续吗？",
                                   QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            self.log("用户取消一键修改")
            return

        try:
            self.log("=" * 40)
            self.log("开始一键修改所有配置")
            self.log("=" * 40)

            # 执行重置操作
            preserve_chat = self.preserve_chat_checkbox.isChecked()
            self.perform_full_reset(preserve_chat)

            self.log("=" * 40)
            self.log("一键修改完成！")
            self.log("=" * 40)

            QMessageBox.information(self, "完成", "一键修改所有配置完成！\n现在可以重新启动 Qoder。")

        except Exception as e:
            self.log(f"一键修改失败: {e}")
            QMessageBox.critical(self, "错误", f"一键修改失败: {e}")

    def perform_full_reset(self, preserve_chat=True):
        """执行完整重置"""
        home_dir = Path.home()
        qoder_support_dir = home_dir / "Library/Application Support/Qoder"

        if not qoder_support_dir.exists():
            raise Exception("未找到 Qoder 应用数据目录")

        # 1. 重置机器ID
        self.log("1. 重置机器ID...")
        machine_id_file = qoder_support_dir / "machineid"
        if machine_id_file.exists():
            new_machine_id = str(uuid.uuid4())
            with open(machine_id_file, 'w') as f:
                f.write(new_machine_id)
            self.log("   机器ID已重置")

        # 2. 重置遥测数据
        self.log("2. 重置遥测数据...")
        storage_json_file = qoder_support_dir / "User/globalStorage/storage.json"
        if storage_json_file.exists():
            with open(storage_json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            new_uuid = str(uuid.uuid4())
            machine_id_hash = hashlib.sha256(new_uuid.encode()).hexdigest()
            device_id = str(uuid.uuid4())
            sqm_id = str(uuid.uuid4())  # 新增：软件质量度量ID

            # 重置所有遥测相关的标识符
            data['telemetry.machineId'] = machine_id_hash
            data['telemetry.devDeviceId'] = device_id
            data['telemetry.sqmId'] = sqm_id
            
            # 清除其他可能的身份识别配置（保留对话时不清除）
            if not preserve_chat:
                # 完全重置模式：清除所有可能的身份相关配置
                identity_keys_to_remove = []
                for key in data.keys():
                    if any(keyword in key.lower() for keyword in [
                        'auth', 'login', 'session', 'token', 'credential',
                        'device', 'fingerprint', 'tracking', 'analytics'
                    ]):
                        identity_keys_to_remove.append(key)
                
                for key in identity_keys_to_remove:
                    del data[key]
                    self.log(f"   已清除配置: {key}")
            else:
                # 保留对话模式：只清除明确的身份识别配置
                self.log("   保留对话模式：保留非身份相关配置")

            with open(storage_json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            self.log(f"   新遥测机器ID: {machine_id_hash[:16]}...")
            self.log(f"   新设备ID: {device_id}")
            self.log(f"   新SQM ID: {sqm_id}")

        # 3. 清理缓存
        self.log("3. 清理缓存数据...")
        cache_dirs = [
            "Cache", "blob_storage", "Code Cache", "SharedClientCache",
            "GPUCache", "DawnGraphiteCache", "DawnWebGPUCache"
        ]

        cleaned = 0
        for cache_dir in cache_dirs:
            cache_path = qoder_support_dir / cache_dir
            if cache_path.exists():
                try:
                    shutil.rmtree(cache_path)
                    cleaned += 1
                except:
                    pass

        self.log(f"   已清理 {cleaned} 个缓存目录")
        
        # 4. 清理身份识别文件（新增）
        self.log("4. 清理身份识别文件...")
        identity_files = [
            "Network Persistent State",  # 网络服务器连接历史和指纹
            "TransportSecurity",  # HSTS等安全策略记录
            "Trust Tokens", "Trust Tokens-journal",  # 信任令牌数据库
            "SharedStorage", "SharedStorage-wal",  # 共享存储数据库
            "Preferences",  # 用户偏好设置（可能包含指纹）
            "Login Credentials",  # 登录凭据（如果存在）
            "Web Data", "Web Data-journal",  # Web数据数据库（如果存在）
            "cert_transparency_reporter_state.json",  # 证书透明度状态
            "Local State",  # Chromium本地状态（包含加密密钥）
            "NetworkDataMigrated"  # 网络数据迁移标记
        ]
        
        identity_cleaned = 0
        for identity_file in identity_files:
            file_path = qoder_support_dir / identity_file
            if file_path.exists():
                try:
                    file_path.unlink()
                    self.log(f"   已清除: {identity_file}")
                    identity_cleaned += 1
                except Exception as e:
                    self.log(f"   清除失败 {identity_file}: {e}")
        
        # 5. 清理存储目录
        storage_dirs = [
            "Service Worker",  # 服务工作者缓存
            "Certificate Revocation Lists",  # 证书撤销列表
            "SSLCertificates",  # SSL证书缓存
            "databases",  # 数据库目录
            "clp",  # 剪贴板数据，可能包含敏感信息
            "logs",  # 日志文件，可能记录用户活动
            "Backups",  # 备份文件，可能包含历史身份信息
            "CachedExtensionVSIXs"  # 扩展缓存，显示用户安装的扩展
        ]
        
        # 根据是否保留对话记录来决定清理哪些存储目录
        if not preserve_chat:
            # 如果不保留对话记录，清理所有存储目录
            storage_dirs.extend([
                "Local Storage",  # 本地存储数据库（可能包含对话索引）
                "Session Storage",  # 会话存储
                "WebStorage",  # Web存储
                "Shared Dictionary"  # 共享字典
            ])
            self.log("   不保留对话模式：清理所有存储目录")
        else:
            # 如果保留对话记录，保留可能包含对话索引的存储
            # 但仍需清理可能包含身份信息的存储
            storage_dirs.extend([
                "Session Storage",  # 会话存储（可能包含身份信息）
                "WebStorage",  # Web存储（可能包含身份信息）
                "Shared Dictionary"  # 共享字典
            ])
            self.log("   保留对话模式：保留 Local Storage（可能包含对话索引）")
        
        for storage_dir in storage_dirs:
            storage_path = qoder_support_dir / storage_dir
            if storage_path.exists():
                try:
                    shutil.rmtree(storage_path)
                    self.log(f"   已清除: {storage_dir}")
                    identity_cleaned += 1
                except Exception as e:
                    self.log(f"   清除失败 {storage_dir}: {e}")
        
        self.log(f"   已清理 {identity_cleaned} 个身份识别文件/目录")
        
        # 5. 执行高级身份清理（新增）
        self.log("5. 执行高级身份清理...")
        self.perform_advanced_identity_cleanup(qoder_support_dir, preserve_chat)

        # 6. 处理对话记录
        if preserve_chat:
            self.log("6. 保留对话记录...")
            self.log("   对话记录已保留")
        else:
            self.log("6. 清除对话记录...")
            self.clear_chat_history(qoder_support_dir)

    def perform_advanced_identity_cleanup(self, qoder_support_dir, preserve_chat=False):
        """执行高级身份清理，清除所有可能的身份识别信息"""
        try:
            self.log("开始高级身份清理...")
            cleaned_count = 0
            
            # 1. 清理 SharedClientCache 内部文件
            shared_cache = qoder_support_dir / "SharedClientCache"
            if shared_cache.exists():
                # 总是清理这些关键的身份文件（会重新生成）
                critical_files = [".info", ".lock", "mcp.json"]
                for file_name in critical_files:
                    file_path = shared_cache / file_name
                    if file_path.exists():
                        try:
                            file_path.unlink()
                            self.log(f"   已清除: SharedClientCache/{file_name}")
                            cleaned_count += 1
                        except Exception as e:
                            self.log(f"   清除失败 {file_name}: {e}")
                
                # 总是清理 cache 目录（缓存数据）
                cache_dir = shared_cache / "cache"
                if cache_dir.exists():
                    try:
                        shutil.rmtree(cache_dir)
                        self.log("   已清除: SharedClientCache/cache")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 cache: {e}")
                
                # 根据保留对话设置决定是否清理 index 目录
                index_dir = shared_cache / "index"
                if index_dir.exists():
                    if not preserve_chat:
                        # 不保留对话：清理所有索引
                        try:
                            shutil.rmtree(index_dir)
                            self.log("   已清除: SharedClientCache/index")
                            cleaned_count += 1
                        except Exception as e:
                            self.log(f"   清除失败 index: {e}")
                    else:
                        # 保留对话：只清理非对话相关的索引
                        # 保留可能包含对话搜索索引的文件
                        for index_item in index_dir.iterdir():
                            if index_item.is_dir() and 'chat' not in index_item.name.lower():
                                try:
                                    shutil.rmtree(index_item)
                                    self.log(f"   已清除: SharedClientCache/index/{index_item.name}")
                                    cleaned_count += 1
                                except Exception as e:
                                    self.log(f"   清除失败 index/{index_item.name}: {e}")
                        self.log("   保留对话模式：保留可能的对话索引")
            
            # 2. 清理系统级别的身份文件
            system_files = [
                "code.lock",
                "languagepacks.json"
            ]
            
            for sys_file in system_files:
                file_path = qoder_support_dir / sys_file
                if file_path.exists():
                    try:
                        file_path.unlink()
                        self.log(f"   已清除: {sys_file}")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 {sys_file}: {e}")
            
            # 3. 清理崩溃报告目录（可能包含设备信息）
            crashpad_dir = qoder_support_dir / "Crashpad"
            if crashpad_dir.exists():
                try:
                    shutil.rmtree(crashpad_dir)
                    self.log("   已清除: Crashpad")
                    cleaned_count += 1
                except Exception as e:
                    self.log(f"   清除失败 Crashpad: {e}")
            
            # 4. 清理缓存目录（CachedData和 CachedProfilesData）
            cached_dirs = ["CachedData", "CachedProfilesData"]
            for cached_dir in cached_dirs:
                dir_path = qoder_support_dir / cached_dir
                if dir_path.exists():
                    try:
                        shutil.rmtree(dir_path)
                        self.log(f"   已清除: {cached_dir}")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 {cached_dir}: {e}")
            
            # 5. 清理 socket 文件
            import glob
            socket_pattern = str(qoder_support_dir / "*.sock")
            socket_files = glob.glob(socket_pattern)
            for socket_file in socket_files:
                try:
                    Path(socket_file).unlink()
                    self.log(f"   已清除: {Path(socket_file).name}")
                    cleaned_count += 1
                except Exception as e:
                    self.log(f"   清除失败 {Path(socket_file).name}: {e}")
            
            # 6. 清理设备指纹和活动记录文件（新增）
            fingerprint_and_activity_files = [
                "DeviceMetadata", "HardwareInfo", "SystemInfo",
                "QuotaManager", "QuotaManager-journal",
                "ActivityLog", "EventLog", "UserActivityLog",
                "origin_bound_certs", "Network Action Predictor",
                "AutofillStrikeDatabase", "AutofillStrikeDatabase-journal",
                "Feature Engagement Tracker", "PasswordStoreDefault",
                "PreferredApps", "UserPrefs", "UserPrefs.backup"
            ]
            
            for file_name in fingerprint_and_activity_files:
                file_path = qoder_support_dir / file_name
                if file_path.exists():
                    try:
                        if file_path.is_dir():
                            shutil.rmtree(file_path)
                        else:
                            file_path.unlink()
                        self.log(f"   已清除: {file_name}")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 {file_name}: {e}")
            
            # 7. 清理数据库目录内的所有文件（新增）
            databases_dir = qoder_support_dir / "databases"
            if databases_dir.exists():
                try:
                    shutil.rmtree(databases_dir)
                    self.log("   已清除: databases 目录及其所有内容")
                    cleaned_count += 1
                except Exception as e:
                    self.log(f"   清除失败 databases: {e}")
            
            # 8. 清理 Electron 相关的持久化数据（新增）
            electron_files = [
                "Dictionaries", "Platform Notifications",
                "ShaderCache", "VideoDecodeStats",
                "OriginTrials", "BrowserMetrics",
                "AutofillRegexes", "SafeBrowsing"
            ]
            
            for electron_file in electron_files:
                file_path = qoder_support_dir / electron_file
                if file_path.exists():
                    try:
                        if file_path.is_dir():
                            shutil.rmtree(file_path)
                        else:
                            file_path.unlink()
                        self.log(f"   已清除: {electron_file}")
                        cleaned_count += 1
                    except Exception as e:
                        self.log(f"   清除失败 {electron_file}: {e}")
            
            self.log(f"   高级身份清理完成，处理了 {cleaned_count} 个项目")
            
        except Exception as e:
            self.log(f"   高级身份清理失败: {e}")

    def clear_chat_history(self, qoder_support_dir):
        """清除对话记录"""
        try:
            cleared = 0

            # 1. 清除工作区中的对话会话
            workspace_storage = qoder_support_dir / "User/workspaceStorage"
            if workspace_storage.exists():
                for workspace_dir in workspace_storage.iterdir():
                    if workspace_dir.is_dir():
                        # 清除chatSessions目录
                        chat_sessions = workspace_dir / "chatSessions"
                        if chat_sessions.exists():
                            try:
                                shutil.rmtree(chat_sessions)
                                self.log(f"   已清除: {chat_sessions.relative_to(qoder_support_dir)}")
                                cleared += 1
                            except Exception as e:
                                self.log(f"   清除失败 {chat_sessions.relative_to(qoder_support_dir)}: {e}")

                        # 清除chatEditingSessions目录
                        chat_editing = workspace_dir / "chatEditingSessions"
                        if chat_editing.exists():
                            try:
                                shutil.rmtree(chat_editing)
                                self.log(f"   已清除: {chat_editing.relative_to(qoder_support_dir)}")
                                cleared += 1
                            except Exception as e:
                                self.log(f"   清除失败 {chat_editing.relative_to(qoder_support_dir)}: {e}")

            # 2. 清除历史记录
            history_dir = qoder_support_dir / "User/History"
            if history_dir.exists():
                try:
                    shutil.rmtree(history_dir)
                    self.log(f"   已清除: User/History")
                    cleared += 1
                except Exception as e:
                    self.log(f"   清除失败 User/History: {e}")

            # 3. 清除会话存储中的对话相关数据
            session_storage = qoder_support_dir / "Session Storage"
            if session_storage.exists():
                try:
                    shutil.rmtree(session_storage)
                    self.log(f"   已清除: Session Storage")
                    cleared += 1
                except Exception as e:
                    self.log(f"   清除失败 Session Storage: {e}")

            # 4. 清除用户数据中的对话相关配置
            user_data_file = qoder_support_dir / "User/globalStorage/storage.json"
            if user_data_file.exists():
                try:
                    with open(user_data_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    # 清除对话相关的键
                    chat_keys = [key for key in data.keys() if
                               'chat' in key.lower() or
                               'conversation' in key.lower() or
                               'history' in key.lower() or
                               'session' in key.lower()]

                    if chat_keys:
                        for key in chat_keys:
                            del data[key]
                            self.log(f"   已清除配置: {key}")

                        with open(user_data_file, 'w', encoding='utf-8') as f:
                            json.dump(data, f, indent=4, ensure_ascii=False)

                        cleared += 1

                except Exception as e:
                    self.log(f"   清除用户配置失败: {e}")

            self.log(f"   对话记录清除完成 (处理了 {cleared} 个项目)")

        except Exception as e:
            self.log(f"   清除对话记录失败: {e}")

    def open_github(self):
        """打开GitHub链接"""
        self.log("打开GitHub链接...")
        webbrowser.open("https://github.com/itandelin/qoder-free")

def main():
    app = QApplication(sys.argv)

    # 设置应用程序样式
    app.setStyle('Fusion')

    # 设置全局样式表，确保对话框文字和按钮可见
    app.setStyleSheet("""
        QMessageBox {
            background-color: white;
            color: black;
        }
        QMessageBox QLabel {
            color: black;
        }
        QMessageBox QPushButton {
            background-color: white;
            color: black;
            border: 1px solid #ccc;
            padding: 5px 15px;
        }
    """)

    window = QoderResetGUI()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
