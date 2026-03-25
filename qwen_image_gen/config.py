"""
Configuration management for Qwen Image Generation

Handles:
- API key loading from multiple sources
- User preferences (EXTEND.md)
- Setup wizard
"""

import os
import json
from pathlib import Path
from typing import Optional, Dict, Any, List

from .types import Config, UserPreferences, SetupStatus, CONFIG_DIR_NAME, ENV_FILE_NAME


def get_config_paths() -> List[Path]:
    """
    Get config file paths in priority order:
    1. Project directory (.qwen-image-gen/.env)
    2. XDG config (~/.config/.qwen-image-gen/.env)
    3. Home directory (~/.qwen-image-gen/.env)
    """
    paths = []
    
    # Project directory
    paths.append(Path.cwd() / CONFIG_DIR_NAME / ENV_FILE_NAME)
    
    # XDG config
    xdg_config = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    paths.append(xdg_config / CONFIG_DIR_NAME / ENV_FILE_NAME)
    
    # Home directory
    paths.append(Path.home() / CONFIG_DIR_NAME / ENV_FILE_NAME)
    
    return paths


def get_preferences_path() -> Path:
    """Get preferences file path (~/.qwen-image-gen/EXTEND.md)"""
    return Path.home() / CONFIG_DIR_NAME / "EXTEND.md"


def load_config() -> Optional[Config]:
    """
    Load config from file (API key).
    Returns config from first file that contains a valid API key.
    """
    for config_path in get_config_paths():
        try:
            if config_path.exists():
                content = config_path.read_text(encoding="utf-8")
                for line in content.split("\n"):
                    line = line.strip()
                    if line and not line.startswith("#"):
                        if "=" in line:
                            key, value = line.split("=", 1)
                            if key.strip() == "DASHSCOPE_API_KEY":
                                api_key = value.strip()
                                if api_key:
                                    return Config(DASHSCOPE_API_KEY=api_key)
        except Exception:
            continue
    
    return None


def load_preferences() -> UserPreferences:
    """Load user preferences from EXTEND.md"""
    preferences_path = get_preferences_path()
    default_prefs = UserPreferences()
    
    try:
        if preferences_path.exists():
            content = preferences_path.read_text(encoding="utf-8")
            
            # Parse YAML-like front matter
            if content.startswith("---"):
                end_idx = content.find("---", 3)
                if end_idx > 0:
                    yaml_content = content[3:end_idx]
                    for line in yaml_content.split("\n"):
                        if ":" in line:
                            key, value = line.split(":", 1)
                            key = key.strip()
                            value = value.strip()
                            
                            if key == "default_aspect_ratio":
                                default_prefs.default_aspect_ratio = value
                            elif key == "default_quality":
                                default_prefs.default_quality = value
                            elif key == "prompt_extend":
                                default_prefs.prompt_extend = value.lower() == "true"
                            elif key == "watermark":
                                default_prefs.watermark = value.lower() == "true"
                            elif key == "negative_prompt":
                                default_prefs.negative_prompt = value.strip('"')
                            elif key == "n":
                                default_prefs.n = int(value)
    except Exception:
        pass
    
    return default_prefs


def save_config(api_key: str) -> Path:
    """Save API key to config file"""
    config_dir = Path.home() / CONFIG_DIR_NAME
    config_dir.mkdir(parents=True, exist_ok=True)
    
    config_path = config_dir / ENV_FILE_NAME
    config_path.write_text(f"DASHSCOPE_API_KEY={api_key}\n", encoding="utf-8")
    
    return config_path


def save_preferences(prefs: UserPreferences) -> Path:
    """Save user preferences to EXTEND.md"""
    config_dir = Path.home() / CONFIG_DIR_NAME
    config_dir.mkdir(parents=True, exist_ok=True)
    
    preferences_path = config_dir / "EXTEND.md"
    
    content = f"""---
default_aspect_ratio: {prefs.default_aspect_ratio}
default_quality: {prefs.default_quality}
prompt_extend: {str(prefs.prompt_extend).lower()}
watermark: {str(prefs.watermark).lower()}
negative_prompt: "{prefs.negative_prompt}"
n: {prefs.n}
---
"""
    preferences_path.write_text(content, encoding="utf-8")
    
    return preferences_path


async def get_api_key(cli_api_key: Optional[str] = None) -> Optional[str]:
    """
    Get API key from all sources (priority order):
    1. CLI argument
    2. Config file
    3. Environment variable
    """
    if cli_api_key:
        return cli_api_key
    
    config = load_config()
    if config and config.DASHSCOPE_API_KEY:
        return config.DASHSCOPE_API_KEY
    
    return os.environ.get("DASHSCOPE_API_KEY")


async def check_setup() -> SetupStatus:
    """Check if setup is complete (API key configured)"""
    api_key = await get_api_key()
    config_dir = Path.home() / CONFIG_DIR_NAME
    preferences_path = config_dir / "EXTEND.md"
    
    has_preferences = preferences_path.exists()
    
    return SetupStatus(
        configured=bool(api_key),
        has_preferences=has_preferences,
        config_path=str(config_dir),
    )


def validate_size(size: str) -> tuple[bool, Optional[str]]:
    """
    Validate size string.
    Returns (valid, error_message)
    """
    parts = size.split("*")
    if len(parts) != 2:
        return False, f"Invalid size format: {size}. Use format like 1024*1024"
    
    try:
        width = int(parts[0])
        height = int(parts[1])
    except ValueError:
        return False, f"Invalid size values: {size}"
    
    from .types import MIN_SIZE, MAX_SIZE
    
    if width < MIN_SIZE or height < MIN_SIZE:
        return False, f"Size must be at least {MIN_SIZE}×{MIN_SIZE}"
    
    if width > MAX_SIZE or height > MAX_SIZE:
        return False, f"Size must be at most {MAX_SIZE}×{MAX_SIZE}"
    
    total_pixels = width * height
    min_pixels = MIN_SIZE * MIN_SIZE
    max_pixels = MAX_SIZE * MAX_SIZE
    
    if total_pixels < min_pixels or total_pixels > max_pixels:
        return False, f"Total pixels must be between {min_pixels} and {max_pixels}"
    
    return True, None


def run_setup_wizard() -> None:
    """Interactive setup wizard for first-time users"""
    print("""
🎨 欢迎使用 Qwen Image Generation 设置向导！

本向导将帮助您配置 API Key，以便生成图片。

📌 如何获取 API Key：
   1. 访问：https://bailian.console.aliyun.com/
   2. 登录/注册阿里云账号
   3. 在控制台创建 API Key（格式：sk-xxx）

⚠️  由于脚本运行环境限制，无法在此直接输入 API Key。
   请选择以下任一方式配置：

   【推荐】方式 1：在 AI 编程工具中直接使用
   输入"帮我生成一张图片"，系统会自动引导您配置。

   方式 2：手动创建配置文件
   运行以下命令（将 sk-xxx 替换为您的真实 API Key）：
   mkdir -p ~/.qwen-image-gen
   echo "DASHSCOPE_API_KEY=sk-xxx" > ~/.qwen-image-gen/.env

   方式 3：设置环境变量
   在终端运行：
   export DASHSCOPE_API_KEY=sk-xxx

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 验证配置是否成功：
   python -m qwen_image_gen --check-setup

   期望输出：{"configured": true, "hasPreferences": false}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
