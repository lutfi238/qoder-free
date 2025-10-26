# Qoder-Free

A modern graphical interface tool for resetting user identity information in the Qoder application.

![Qoder-Free Interface](https://img.shields.io/badge/Platform-macOS-blue)
![Windows Support](https://img.shields.io/badge/Platform-Windows-blue)
![Python](https://img.shields.io/badge/Python-3.6+-green)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-orange)

**✨Important Note: After resetting Qoder, please use a fingerprint browser to re-register. This will prevent duplicate registration detection caused by browser cache or fingerprints.**

**Additionally, like with Cursor and Augment, future detection will become increasingly strict. There's no guarantee how long this will work, so use it while it lasts.**

## 📋 Table of Contents

- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Usage Guide](#usage-guide)
- [Feature Details](#feature-details)
- [Interface Description](#interface-description)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [Development Guide](#development-guide)
- [Update Log](#update-log)

## ✨ Features

- 💻 **Reset Machine ID** - Generate a brand new machine identifier
- 📊 **Reset Telemetry Data** - Reset the application's telemetry and device ID
- 🧹 **Smart Cache Cleaning** - Clean application cache while protecting important data
- 🔥 **Deep Identity Cleanup** - Clear all network states, trust tokens, and local storage
- 🔐 **Login Identity Cleanup** - Specifically cleans authentication tokens, login status, and session data
- 🛡️ **Hardware Fingerprint Reset** - The strongest anti-detection feature, generating fake hardware information to interfere with detection
- 🚀 **Super Deep Cleanup** - Secure system-level cache cleaning, network trace reset, browser fingerprint obfuscation
- 💬 **Smart Conversation Management** - Option to keep or clear chat history
- ⚡ **One-Click Complete Reset** - A complete solution including all 9 reset functions
- 🖥️ **Modern Interface** - A beautiful graphical interface based on PyQt5
- 📝 **Real-time Logs** - Detailed operation logs and status monitoring
- 🔍 **Status Detection** - Automatically detects Qoder's running status and data integrity
- 🛡️ **Safety Protection** - Confirmation before operations to prevent mistakes
- 🌍 **Cross-Platform Support** - Supports macOS, Windows, and Linux operating systems
- 🌐 **Multi-language Interface** - Supports switching between Chinese/English/Russian/Portuguese

### 🔍 Deep Identity Recognition Cleanup

**Why is deep cleaning necessary?**
Basic reset tools only handle basic identity files, but miss the following key identity information:

#### 1. Core Identity Identifiers
- **machineid** - Unique machine identifier
- **telemetry.machineId** - Telemetry machine ID (SHA256 hash)
- **telemetry.devDeviceId** - Device identifier
- **telemetry.sqmId** - Software Quality Metrics ID

#### 2. Network Layer Identity Information (Most Critical)
- **Network Persistent State** - Network server connection history and network fingerprint
- **TransportSecurity** - HSTS and other transport security status records
- **Trust Tokens & Trust Tokens-journal** - Trust token database
- **SharedStorage & SharedStorage-wal** - Shared storage database

#### 3. Local Storage Identity Information
- **Local Storage/leveldb/** - Local Storage LevelDB database
- **Session Storage** - Session storage data
- **WebStorage** - Web storage data
- **Shared Dictionary** - Shared dictionary data

#### 4. System-level Identity Information
- **SharedClientCache/.info** - Language server connection information (port/PID)
- **SharedClientCache/.lock** - Process lock file
- **SharedClientCache/mcp.json** - MCP configuration file
- **SharedClientCache/index/** - Index data directory
- **SharedClientCache/cache/** - Shared cache data

#### 5. Device Fingerprint and Configuration
- **Preferences** - User preferences (may contain device fingerprint)
- **Local State** - Chromium local state (contains encryption keys)
- **code.lock** - Code lock file
- **languagepacks.json** - Language pack configuration

#### 6. Hardware Fingerprint Reset
- **Hardware Identifier Reset** - cpu_id, gpu_id, memory_id, board_serial, bios_uuid
- **Fake Hardware Information Generation** - Generates realistic hardware configurations based on the system type
  - **macOS**: Apple M2-M5 Pro chips, LPDDR5 memory, macOS 12.x-15.x versions
  - **Windows**: Intel/AMD processors, NVIDIA/AMD graphics cards, Windows 10/11 versions
  - **Linux**: Generic hardware configuration, Linux 5.x/6.x kernel versions
- **Obfuscate Detection Files** - Create multiple fake hardware information files to interfere with detection
- **System Information Reset** - Reset system version, architecture information, timezone, and other system fingerprints

#### 7. Login Identity Cleanup
- **Authentication Token Cleanup** - Clear all login states and session data
- **Nonce and Challenge Data** - Clear authentication challenge-related data
- **Device Authentication Data** - DeviceMetadata, HardwareInfo, AutofillStrikeDatabase
- **User Configuration Cleanup** - Clear login-related user preferences
- **SharedClientCache Login Status** - Clean language server connection information and authentication cache

## ️ System Requirements

- **Operating System**: macOS 10.14+ or Windows 10+
- **Python**: 3.6 or higher
- **Dependencies**: PyQt5
- **Disk Space**: At least 50MB of free space
- **Permissions**:
  - macOS: Read/write permissions for `~/Library/Application Support/Qoder`
  - Windows: Read/write permissions for `%APPDATA%\Qoder`

## 📦 Installation Guide

### Method 1: Direct Execution (Recommended)

1.  **Clone or Download Project**
    ```bash
    git clone <repository-url>
    cd qoder-free
    ```

2.  **Install Dependencies**
    ```bash
    pip3 install PyQt5
    ```

3.  **Run the Program**
    ```bash
    python3 qoder_reset_gui.py
    ```

### Method 2: Using Launch Scripts

**macOS/Linux:**
```bash
chmod +x start_gui.sh
./start_gui.sh
```

**Windows:**
```cmd
start_gui.bat
```

## 🚀 Usage Guide

### Basic Usage Flow

1.  **Start the Application**
    - Double-click to run `qoder_reset_gui.py`
    - Or start it via a terminal command

2.  **Check Status**
    - The program will automatically detect the current status upon startup
    - Check the log area to understand the system status

3.  **Select an Operation**
    - Check "Keep Conversation History" (checked by default)
    - Select a specific reset operation

4.  **Execute Reset**
    - Click the corresponding button to perform the action
    - Check the logs to confirm the operation result

### Quick Start

```bash
# 1. Install Dependencies
pip3 install PyQt5

# 2. Run the Program
python3 qoder_reset_gui.py

# 3. Click "One-Click Reset All Settings" in the interface
```

## 🔧 Feature Details

### Main Function Buttons

#### 🔴 **Close Qoder**
   - Checks the running status of the Qoder process
   - Prompts the user to manually close the application
   - Ensures the safety of the reset operation

#### 💻 **Reset Machine ID**
   - Generates a new UUID as the machine identifier
   - Creates multiple backup ID files (deviceid, hardware_uuid, system_uuid, etc.)
   - Modifies the `~/Library/Application Support/Qoder/machineid` file
   - Synchronously updates related identifiers in storage.json
   - Makes Qoder recognize the device as brand new

#### 📊 **Reset Telemetry Data**
   - Resets `telemetry.machineId` and `telemetry.devDeviceId`
   - Adds new identifiers like sessionId, installationId, clientId, userId, anonymousId
   - Randomly generates system version, architecture info, timezone, and other system fingerprints
   - Modifies the telemetry configuration in the `storage.json` file
   - Clears device tracking information

#### 🔥 **Deep Identity Cleanup**
   - Clears all network states and cookies
   - Clears all local storage data
   - Clears internal files in SharedClientCache
   - Clears system-level identity files
   - Clears crash reports and cached data
   - **Forcibly does not keep conversations**, for the most thorough identity reset

#### 🔐 **Login Identity Cleanup**
   - Specifically cleans login-related identity information
   - Cleans login status files in SharedClientCache
   - Cleans authentication tokens and session data
   - Cleans nonce and challenge related data
   - Cleans device fingerprint and authentication data
   - Resets login-related user preferences

#### 🛡️ **Hardware Fingerprint Reset** (Strongest anti-detection)
   - Resets all possible hardware identifiers (cpu_id, gpu_id, memory_id, etc.)
   - **Generates fake hardware information based on system type**:
     - macOS: Apple M2-M5 Pro chip configurations
     - Windows: Intel/AMD processor + NVIDIA/AMD graphics card
     - Linux: Generic hardware configuration
   - Cleans hardware fingerprint-related files and cache
   - Creates multiple fake hardware information files to interfere with detection
   - Resets system version, architecture, timezone, and other system fingerprints
   - **It is recommended to restart the system before using Qoder again**

#### ⚡ **One-Click Reset All Settings** (Recommended)
   - **A complete reset solution including all 8 features**:
     1. Reset Machine ID
     2. Reset Telemetry Data
     3. Clean Cache Data
     4. Clean Identity Files
     5. Advanced Identity Cleanup
     6. Login Identity Cleanup
     7. Hardware Fingerprint Reset
     8. Smart Conversation Management
   - Processes chat data according to the "Keep Conversation History" option
   - **The most comprehensive anti-detection reset solution**

### Conversation History Management

- **Keep Conversation History** (checked by default)
  - Fully retained:
    - `User/workspaceStorage/.../chatSessions/*.json` - Conversation content files
    - `User/workspaceStorage/.../chatEditingSessions/` - Editing session status
    - `User/settings.json` - User settings
  - Smart retention:
    - `Local Storage/leveldb/` - Local storage database (may contain conversation index)
    - `SharedClientCache/index/` - Selectively retains conversation-related indexes
  - Conditional cleaning:
    - `Session Storage` - Cleaned (may contain identity information)
    - `WebStorage` - Cleaned (may contain identity information)
    - `Shared Dictionary` - Cleaned

- **Clear Conversation History** (unchecked)
  - Deletes all conversation session data
  - Clears chat editing sessions
  - Cleans all storage directories (including Local Storage)
  - Cleans all index data
  - Removes history
  - Cleans session storage

## 🖼️ Interface Description

### Interface Screenshot

![Qoder-Free GUI Screenshot](screenshot.webp)

## 🔧 Technical Details

### File Structure

```
qoder-free/
├── qoder_reset_gui.py          # Main program file (PyQt5 interface, cross-platform support)
├── start_gui.sh               # macOS/Linux launch script
├── start_gui.bat              # Windows launch script
└── README.md                  # Complete documentation
```

### Core Technology

- **GUI Framework**: PyQt5 - Modern cross-platform GUI framework
- **Process Detection**: Uses `pgrep` command to detect Qoder's running state
- **File Operations**: Python's `pathlib` for safe file path operations
- **JSON Handling**: Standard library `json` module for handling configuration files
- **UUID Generation**: Uses `uuid4()` to generate random identifiers
- **Hash Calculation**: SHA256 algorithm to generate telemetry machine ID

### Files and Directories Manipulated

```
~/Library/Application Support/Qoder/  (or Windows: %APPDATA%\Qoder\)
├── machineid                               # Machine ID file
├── deviceid                                # Device ID file (new)
├── hardware_uuid                           # Hardware UUID file (new)
├── system_uuid                             # System UUID file (new)
├── platform_id                             # Platform ID file (new)
├── installation_id                         # Installation ID file (new)
├── cpu_id                                  # CPU ID file (hardware fingerprint)
├── gpu_id                                  # GPU ID file (hardware fingerprint)
├── memory_id                               # Memory ID file (hardware fingerprint)
├── board_serial                            # Motherboard serial number (hardware fingerprint)
├── bios_uuid                               # BIOS UUID (hardware fingerprint)
├── Network Persistent State                # Network connection history and fingerprint (critical)
├── TransportSecurity                       # HSTS and other security policy records
├── Trust Tokens                           # Trust token database
├── Trust Tokens-journal                   # Trust token log
├── SharedStorage                           # Shared storage database
├── SharedStorage-wal                       # Shared storage WAL file
├── Preferences                             # User preferences
├── Secure Preferences                      # Secure preferences (new)
├── Local State                             # Chromium local state
├── code.lock                               # Code lock file
├── languagepacks.json                      # Language pack configuration
├── *.sock                                  # Socket files
├── DeviceMetadata                          # Device metadata (login identity cleanup)
├── HardwareInfo                            # Hardware information (login identity cleanup)
├── SystemInfo                              # System information (login identity cleanup)
├── AutofillStrikeDatabase                  # Autofill database (login identity cleanup)
├── AutofillStrikeDatabase-journal          # Autofill database log
├── Feature Engagement Tracker             # Feature engagement tracker (login identity cleanup)
├── Platform Notifications                  # Platform notifications (new)
├── VideoDecodeStats                        # Video decode stats (new)
├── OriginTrials                            # Origin trials (new)
├── BrowserMetrics                          # Browser metrics (new)
├── SafeBrowsing                            # Safe browsing (new)
├── QuotaManager                            # Quota manager (new)
├── QuotaManager-journal                    # Quota manager log
├── Network Action Predictor                # Network action predictor (new)
├── hardware_detection.json                # Fake hardware detection file (hardware fingerprint reset)
├── device_capabilities.json               # Fake device capabilities file (hardware fingerprint reset)
├── system_features.json                   # Fake system features file (hardware fingerprint reset)
├── User/
│   ├── globalStorage/storage.json         # Telemetry data configuration (enhanced)
│   │                                      # Contains sessionId, clientId, hardwareId, etc.
│   ├── settings.json                      # User settings (retained)
│   └── workspaceStorage/                  # Workspace storage (contains chat history)
│       ├── */chatSessions/            # Conversation session files (retained)
│       └── */chatEditingSessions/     # Editing session status (retained)
├── SharedClientCache/                      # Shared client cache
│   ├── .info                              # Language server information (port/PID)
│   ├── .lock                              # Process lock file
│   ├── mcp.json                           # MCP configuration file
│   ├── index/                             # Index data directory (selectively retained)
│   └── cache/                             # Shared cache data
├── Local Storage/leveldb/                  # Local Storage LevelDB (retained when keeping chat)
├── Session Storage/                        # Session storage (may contain identity info)
├── WebStorage/                             # Web storage (may contain identity info)
├── Shared Dictionary/                      # Shared dictionary
├── Cache/                                  # Application cache
├── Code Cache/                             # Code cache
├── GPUCache/                               # GPU cache
├── DawnGraphiteCache/                      # Dawn graphite cache
├── DawnWebGPUCache/                        # Dawn WebGPU cache
├── ShaderCache/                            # Shader cache (new)
├── DawnCache/                              # Dawn cache (new)
├── MediaCache/                             # Media cache (hardware fingerprint)
├── Dictionaries/                           # Dictionary cache (new)
├── CachedData/                             # Cached data
├── CachedProfilesData/                     # Cached profile data
├── CachedExtensions/                       # Cached extensions (new)
├── IndexedDB/                              # IndexedDB database (new)
├── CacheStorage/                           # Cache storage (new)
├── WebSQL/                                 # WebSQL database (new)
├── Crashpad/                               # Crash report directory
├── Service Worker/                         # Service worker data
├── Certificate Revocation Lists/           # Certificate revocation lists (new)
├── SSLCertificates/                        # SSL certificate cache (new)
├── databases/                              # Database directory
├── logs/                                   # Log files
├── Backups/                                # Backup files
└── clp/                                    # Clipboard data
```

### 📊 Reset Operation Description

#### ✅ **New Files (v2.3.0)**:
- **Hardware Identifiers**: cpu_id, gpu_id, memory_id, board_serial, bios_uuid
- **Fake Hardware Information**: hardware_detection.json, device_capabilities.json, system_features.json
- **Identity Files**: Secure Preferences, DeviceMetadata, HardwareInfo, SystemInfo
- **Cache Extensions**: ShaderCache, DawnCache, MediaCache, CachedExtensions
- **Network Files**: Certificate Revocation Lists, SSLCertificates

#### 🔄 **storage.json Enhanced Configuration**:
```json
{
  "telemetry.machineId": "SHA256 hash value",
  "telemetry.devDeviceId": "UUID",
  "telemetry.sqmId": "UUID",
  "telemetry.sessionId": "UUID",
  "telemetry.installationId": "UUID",
  "telemetry.clientId": "UUID",
  "telemetry.userId": "UUID",
  "telemetry.anonymousId": "UUID",
  "hardwareId": "UUID",
  "platformId": "UUID",
  "cpuId": "UUID",
  "gpuId": "UUID",
  "memoryId": "UUID",
  "system.platform": "System type",
  "system.arch": "System architecture",
  "system.version": "System version",
  "system.build": "System build number",
  "system.locale": "en-US",
  "system.timezone": "Random timezone"
}
```

## 🚨 Troubleshooting

### Common Problems

#### 1. PyQt5 Installation Fails
```bash
# If pip installation fails, try using conda
conda install pyqt

# Or use homebrew to install Python and PyQt5
brew install python-tk
pip3 install PyQt5
```

#### 2. Insufficient Permissions Error
```bash
# Ensure you have read/write permissions for the Qoder directory
ls -la ~/Library/Application\ Support/Qoder/

# If permissions are insufficient, you can try to fix them
chmod -R u+rw ~/Library/Application\ Support/Qoder/
```

#### 3. Qoder Directory Not Found
- Ensure the Qoder application is installed
- Run Qoder at least once to create the configuration directory
- Check if Qoder is installed in the correct location

#### 4. Interface Text is Invisible
- The program has automatically handled macOS dark mode compatibility
- If problems persist, try switching the system theme
- Restart the application

#### 5. Dialog Box Buttons are Invisible
- The program has set a global style to ensure buttons are visible
- If the problem persists, check your system's PyQt5 version

### Log Analysis

The program displays detailed status check information on startup:

```
[Time] Qoder-Free Reset Tool Started
[Time] ================================================
[Time] 1. Checking Qoder process status...
[Time]    ✅ Qoder is not running
[Time] 2. Checking Qoder directory...
[Time]    ✅ Qoder directory exists
[Time] 3. Checking machine ID file...
[Time]    ✅ Machine ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
[Time] 4. Checking telemetry data file...
[Time]    ✅ Telemetry Machine ID: xxxxxxxxxxxxxxxx...
[Time]    ✅ Device ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
[Time] 5. Checking cache directories...
[Time]    ✅ Found 7/7 cache directories
[Time] 6. Checking conversation history...
[Time]    ✅ Found 4/4 conversation-related directories
[Time] ================================================
[Time] Status check complete, you can now begin operations
```

## 👨‍💻 Development Guide

### Code Structure

```python
class QoderResetGUI(QMainWindow):
    def __init__(self):
        # Initialize interface and multi-language support
        # Set current language to Chinese
        # Initialize multi-language translation dictionary and user interface

    def init_translations(self):
        # Initialize multi-language dictionary (supports Chinese/English/Russian/Portuguese)
        # Contains translations for all UI text, log messages, and dialog texts
        
    def init_ui(self):
        # Create modern PyQt5 interface elements
        # Set window size, style, and layout
        # Create all 8 function buttons and their corresponding event handlers

    def change_language(self, language_text):
        # Dynamic language switching function
        # Supports Chinese, English, Russian, Portuguese
        # Updates all UI text in real-time

    def initialize_status_check(self):
        # Enhanced startup status check (11 new checks)
        # Checks Qoder process, directory, machine ID, telemetry, cache, chat history, etc.

    def check_qoder_running(self):
        # Cross-platform process detection (macOS/Windows/Linux)
        # Uses pgrep command to detect Qoder process status

    def generate_system_version(self, system_type):
        # Generates an appropriate system version number based on the system type (new)
        # macOS: 12.x.x-15.x.x, Windows: 10.0.x, Linux: 5.x.x/6.x.x

    # ========== Basic Function Buttons ==========
    def close_qoder(self):
        # Close Qoder function
        # Checks process status and prompts the user to close it manually

    def reset_machine_id(self):
        # Reset Machine ID (enhanced)
        # Generates new UUID and creates multiple backup ID files
        # Synchronously updates related identifiers in storage.json

    def reset_telemetry(self):
        # Enhanced telemetry data reset (adds sqmId and multiple new identifiers)
        # Resets all telemetry-related identifiers, including sessionId, clientId, etc.

    # ========== Advanced Function Buttons ==========
    def deep_identity_cleanup(self):
        # Deep identity cleanup function (new)
        # Forcibly does not keep conversations, for the most thorough identity reset
        
    def login_identity_cleanup(self):
        # Login identity cleanup function (new)
        # Specifically cleans login-related identity information and authentication data

    def hardware_fingerprint_reset(self):
        # Hardware fingerprint reset function (new - strongest anti-detection)
        # Resets all hardware identifiers and generates fake hardware info to interfere with detection

    def one_click_reset(self):
        # One-click reset function (enhanced)
        # Integrates all 8 functions into a complete reset solution

    # ========== Core Implementation Functions ==========
    def perform_full_reset(self, preserve_chat=True):
        # Execute full reset (enhanced)
        # 1. Reset Machine ID (enhanced)
        # 2. Reset Telemetry Data (enhanced)
        # 3. Clean Cache Data (enhanced)
        # 4. Clean Identity Files (enhanced)
        # 5. Advanced Identity Cleanup
        # 6. Login Identity Cleanup (new)
        # 7. Hardware Fingerprint Reset (new)
        # 8. Smart Conversation Management

    def perform_advanced_identity_cleanup(self, qoder_support_dir, preserve_chat=False):
        # Advanced identity cleanup (new)
        # Cleans SharedClientCache internal files, system-level identity files
        # Cleans crash reports, socket files, device fingerprint files, etc.
        
    def perform_login_identity_cleanup(self, qoder_support_dir):
        # Login-related identity cleanup (new)
        # Cleans login status files in SharedClientCache
        # Cleans authentication tokens, nonce, challenge data
        # Cleans device fingerprint and authentication data

    def perform_hardware_fingerprint_reset(self, qoder_support_dir):
        # Specific implementation of hardware fingerprint reset (new)
        # 1. Reset all hardware identifiers (cpu_id, gpu_id, memory_id, etc.)
        # 2. Reset hardware identifiers in storage.json
        # 3. Clean hardware fingerprint-related files
        # 4. Clean hardware-related cache
        # 5. Create fake hardware information files (adapted to system type)

    def clear_chat_history(self, qoder_support_dir):
        # Clear conversation history (enhanced)
        # Clears conversation sessions and editing sessions in the workspace
        # Clears conversation-related configurations in user settings
        
    # ========== Utility Functions ==========
    def get_qoder_data_dir(self):
        # Cross-platform data directory retrieval (new)
        # Supports macOS, Windows, and Linux
    
    def log(self, message):
        # Logging function (enhanced)
        # Includes timestamps, auto-scrolling, and multi-language support
        
    def tr(self, key):
        # Translation function, returns text for the current language
        
    def update_ui_text(self):
        # Updates UI text for real-time interface updates during language switching

# ========== Global Utility Function ==========
def main():
    # Main function, creates QApplication and starts the GUI application
    # Includes error handling and program exit logic
```

### Testing

Suggested testing steps:

1.  **Startup Test**: Run the program to ensure the interface displays correctly.
2.  **Functionality Test**: Test each button's function individually.
3.  **Status Check**: Verify that the initial status check is correct.
4.  **Reset Test**: Verify the reset functionality in a test environment.
5.  **Log Validation**: Confirm that the operation logs are displayed correctly.

## 📝 Update Log

### v2.3.0 - Complete Anti-Detection Version (Latest)
- ⚡ **One-Click Complete Reset** - The ultimate solution integrating all 8 functions.
- 🛡️ **Hardware Fingerprint Reset** - The strongest anti-detection feature, generating fake hardware information to interfere with detection.
- 🔐 **Login Identity Cleanup** - Specifically cleans authentication tokens, login status, and session data.
- 🌍 **Smart System Adaptation** - Generates corresponding hardware configurations based on the operating system type.
- 🔍 **Enhanced Log Output** - Displays the detected system type for easier debugging and verification.
- 📊 **Telemetry Data Enhancement** - Adds multiple new identifiers like sessionId, installationId, clientId.
- 🛡️ **Identity File Expansion** - Added cleaning for 15+ more identity files, including those related to hardware fingerprints.
- 🧹 **Cache Cleaning Enhancement** - Added new cache directories like ShaderCache, DawnCache, CachedExtensions.

### v2.2.0 - Smart Cross-Platform Version
- 🌍 **Cross-Platform Support** - Added support for Windows and Linux.
- 🔄 **Smart Conversation Retention** - Redesigned the conversation history retention mechanism.
- ✨ **Multi-language Interface** - Supports switching between Chinese/English/Russian/Portuguese.
- 🔧 **Windows Launch Script** - Added `start_gui.bat` for automatic environment checks.
- 📊 **Enhanced Telemetry Reset** - Added reset for `telemetry.sqmId`.
- 🔍 **Precise Identity Cleanup** - Cleanup strategy based on actual directory analysis.
- 🧠 **Smart Index Retention** - Selectively retains index data when keeping conversations.
- 🛡️ **Security Enhancement** - Finer identification and cleaning of identity information.

### v2.1.0 - Identity Recognition Fix Version
- ✨ Added deep identity cleanup feature.
- 🔧 Fixed missing key identity files.
- 📈 Enhanced status check functionality.
- 🎨 Improved interface layout (2x2 button layout).
- 📋 Improved log output and user feedback.
- 🔍 Cleared Network Persistent State, Cookies, SharedStorage, etc.
- 🛠️ Cleaned critical files within SharedClientCache (.info, mcp.json, etc.).
- 🧹 Cleared crash reports, socket files, and other identity information.

### v2.0.0
- ✨ Brand new PyQt5 interface, replacing tkinter.
- 🔧 Fixed issue with invisible dialog text.
- 📝 Added auto-scrolling log display.
- 💬 Precise conversation history protection mechanism.
- 🔍 Automatic status check on startup.
- 🎨 Modern interface design, matching the prototype.

### v1.x.x (Historical Versions)
- GUI based on tkinter.
- Basic reset functionality.
- Simple log display.

## ⚠️ Important Notes

1.  **Backup Before Use**: It is recommended to back up important Qoder configurations and data before use.
2.  **Close Application**: The Qoder application must be completely closed before performing a reset.
3.  **Re-login**: You will need to log back into your Qoder account after a reset.
4.  **Data Loss**: Unchecking "Keep Conversation History" will permanently delete all chat history.
- ✅ **System Compatibility**: Currently supports macOS and Windows systems.

## 📄 License

This project is for learning and research purposes only. Please comply with relevant laws, regulations, and software usage agreements.

## 🤝 Contributing

Contributions are welcome! Please submit Issues and Pull Requests to improve this project.

## 📞 Support

If you encounter problems, please:
1.  Check the troubleshooting section.
2.  Check the log output.
3.  Submit an Issue describing the problem.

## 📱 Modern Interface Features

### 🎨 Design Highlights
- **Purple Banner Title** - Modern top design.
- **Rounded Buttons** - Aesthetically pleasing modern buttons.
- **Gradient Colors** - Professional color scheme.
- **Responsive Layout** - Adapts to different window sizes.

### 🔧 Main Functions
- 🔴 **Check Qoder Status** - One-click check of the application's running status.
- 🔍 **Preview Reset Operation** - Safe dry-run mode.
- ⚡ **Execute Reset Operation** - One-click completion of all reset steps.

### ⚙️ Smart Options
- 💾 **Automatic Backup** - Creates a full backup before reset.
- 💬 **Session Retention** - Option to keep conversation history.
- 📝 **Detailed Logs** - Real-time display of operation progress and results.

## 📋 What Gets Reset

### Content That Will Be Reset
- ✅ **Core Identity Identifiers**
  - Machine ID (`machineid`)
  - Telemetry Machine ID (`telemetry.machineId`)
  - Device ID (`telemetry.devDeviceId`)
  - Software Quality Metrics ID (`telemetry.sqmId`)
- ✅ **Network Identity Fingerprints**
  - Network Persistent State (`Network Persistent State`)
  - Transport Security Records (`TransportSecurity`)
  - Trust Tokens (`Trust Tokens`)
  - Shared Storage (`SharedStorage`)
- ✅ **System-level Files**
  - Language Server Info (`SharedClientCache/.info`, `mcp.json`)
  - User Preferences (`Preferences`)
  - Chromium Local State (`Local State`)
- ✅ **Cache Directories**
  - Cache, GPUCache, DawnGraphiteCache, DawnWebGPUCache
  - Code Cache, SharedClientCache/cache
  - CachedData, CachedProfilesData

### Smartly Retained Content (depends on "Keep Conversation History" setting)
- 🔄 **Conversation Data** - Conversation content and editing sessions (retained by default).
- 🔄 **Local Storage** - Local Storage/leveldb (may contain conversation index).
- 🔄 **Index Data** - SharedClientCache/index (selectively retained).

### Content Always Retained
- ✅ User Settings (`User/settings.json`)
- ✅ Workspace Configuration (`User/workspaceStorage/*/workspace.json`)
- ✅ Code snippets and extension data.

## 🔍 Troubleshooting

### Common Problems

1.  **GUI Window Does Not Appear**
    - Ensure PyQt5 is installed: `pip3 install PyQt5`
    - Try using the launch script: `./start_gui.sh`
    - Check the terminal for any error messages.

2.  **"Qoder is running"**
    - Completely close the Qoder application.
    - Use Cmd+Q or select Quit from the menu.

3.  **"python3 not found"**
    - Install Python 3: https://www.python.org
    - Or use Homebrew: `brew install python3`

4.  **"tkinter not available"**
    - Install python-tk: `brew install python-tk`

5.  **Still Detected as an Old User After Reset**
    - **Recommended Solution**: Use "One-Click Reset All Settings" (now includes all 9 functions).
    - **Step-by-step Troubleshooting**:
      - First, use "Hardware Fingerprint Reset" for the strongest anti-detection effect.
      - Then, use "Deep Identity Cleanup" to clear any remaining identity information.
      - Finally, use "Login Identity Cleanup" to clear authentication status.
      - New: Use the "Super Deep Cleanup" function for system-level cleaning.
    - **Verify Cleanup Effect**: Check the logs to confirm all identity files have been cleaned:
      - `Network Persistent State` - Network connection history
      - `SharedStorage` - Shared storage database
      - `Trust Tokens` - Trust tokens
      - `telemetry.*` - All telemetry identifiers
      - `hardwareId, cpu_id, gpu_id` - Hardware fingerprints
      - New: System-level cache and network traces.
    - **Uncheck** "Keep Conversation History" for the most thorough cleaning.
    - **Environment Change**: Consider changing your network environment or using a VPN.
    - **System Restart**: Restart your system and test again (especially after using hardware fingerprint reset).
    - **New Suggestion**: Use a fingerprint browser or a virtual machine to re-register.

6.  **Secure System-Level Cleaning Issues**
    - **Fully Resolved**: All system-level cleaning functions now use a safe mode.
    - **Whitelist Protection**: Only cleans files related to Qoder/VSCode/Electron.
    - **Path Validation**: Strictly limits the cleaning scope to avoid accidental deletion of other application files.
    - **Protection Mechanism**: Automatically skips important system files and caches of other applications.
    - **User-level Operations**: All cleaning is done at the user permission level, no administrator rights required.
    - **System Stability**: Skips operations like DNS cache flushing that might affect network functionality.
    - **System Mismatch**: Check the "Detected system type" message in the logs.
    - **Fake Information Anomaly**: Confirm that the generated hardware information matches the system type.
    - **Cleaning System-level Cache**:
      ```bash
      # Clear system-level DNS cache
      sudo dscacheutil -flushcache
      
      # Resetting network settings may help clear network fingerprints
      ```

7.  **Log Debug Information**
    - The program now displays the detected system type.
    - Confirm if the fake hardware information generation matches the actual system.
    - Check the log output for all reset operations to ensure they are normal.

7.  **macOS GUI Display Issues**
    - Check the Python icon in the Dock and click to activate it.
    - Ensure the terminal has sufficient permissions to run GUI applications.
    - Try running it in a different terminal application.

## ⚠️ Important Reminders

- **Backup Before Use**: It is recommended to use the backup function to protect important data.
- **Close Application**: Ensure Qoder is completely closed before running the reset.
- **Legal Use**: Use for lawful purposes only and comply with the software's terms of use.
- **Session Retention**: Conversation history is kept by default; uncheck if you wish to clear it.

## 🎉 Get Started

### Recommended Launch Method:

**macOS/Linux:**
```bash
# Use the launch script (recommended)
./start_gui.sh

# Or run directly
python3 qoder_reset_gui.py
```

**Windows:**
```cmd
# Use the launch script (recommended)
start_gui.bat

# Or run directly
python qoder_reset_gui.py
```

Enjoy a brand new Qoder experience!

---

**Version**: 2.2.0
**Development**: Mac: [Mr.T](https://www.74110.net/recommendation/qoder-free/) | Windows: [MRLTR-CMD](https://github.com/MRLTR-CMD)
**Support**: macOS, Windows
