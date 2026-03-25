"""
Type definitions for Qwen Image Generation
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any


# ============================================================================
# Constants
# ============================================================================

DEFAULT_MODEL = "qwen-image-2.0-pro"
DEFAULT_SIZE = "2048*2048"
DEFAULT_N = 1
DEFAULT_NEGATIVE_PROMPT = (
    "低分辨率，低画质，肢体畸形，手指畸形，画面过饱和，蜡像感，人脸无细节，"
    "过度光滑，画面具有 AI 感。构图混乱。文字模糊，扭曲。"
)
DEFAULT_PROMPT_EXTEND = True
DEFAULT_WATERMARK = False

MIN_SIZE = 512
MAX_SIZE = 2048
MAX_IMAGES = 6
MAX_SEED = 2147483647
MAX_PROMPT_LENGTH = 800
MAX_NEGATIVE_PROMPT_LENGTH = 500

API_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"

CONFIG_DIR_NAME = ".qwen-image-gen"
ENV_FILE_NAME = ".env"

# Retry configuration
MAX_ATTEMPTS = 3
RETRY_DELAY_MS = 1000

# Aspect ratio presets (2K resolution)
ASPECT_RATIO_PRESETS: Dict[str, Dict[str, Any]] = {
    "1:1": {"label": "1:1（正方形）", "size": "2048*2048", "width": 2048, "height": 2048},
    "16:9": {"label": "16:9（横图）", "size": "2048*1152", "width": 2048, "height": 1152},
    "9:16": {"label": "9:16（竖图）", "size": "1152*2048", "width": 1152, "height": 2048},
    "4:3": {"label": "4:3（横图）", "size": "2048*1536", "width": 2048, "height": 1536},
    "3:4": {"label": "3:4（竖图）", "size": "1536*2048", "width": 1536, "height": 2048},
}


# ============================================================================
# Data Classes
# ============================================================================

@dataclass
class CliArgs:
    """Command line arguments"""
    prompt: Optional[str] = None
    image_path: Optional[str] = None
    size: str = DEFAULT_SIZE
    ar: Optional[str] = None
    n: int = DEFAULT_N
    negative_prompt: str = DEFAULT_NEGATIVE_PROMPT
    prompt_extend: bool = DEFAULT_PROMPT_EXTEND
    watermark: bool = DEFAULT_WATERMARK
    seed: Optional[int] = None
    api_key: Optional[str] = None
    json_output: bool = False
    help: bool = False
    check_setup: bool = False
    setup: bool = False
    no_prompt_extend: bool = False


@dataclass
class Config:
    """Configuration loaded from .env file"""
    DASHSCOPE_API_KEY: str = ""


@dataclass
class UserPreferences:
    """User preferences stored in EXTEND.md"""
    default_aspect_ratio: str = "1:1"
    default_quality: str = "2k"
    prompt_extend: bool = True
    watermark: bool = False
    negative_prompt: str = DEFAULT_NEGATIVE_PROMPT
    n: int = 1


@dataclass
class SetupStatus:
    """Setup check result"""
    configured: bool
    has_preferences: bool
    config_path: str


@dataclass
class GeneratedImage:
    """Generated image information"""
    url: str
    output_path: str


@dataclass
class ImageResult:
    """Image download result"""
    path: str
    success: bool
    error: Optional[str] = None


# ============================================================================
# API Request/Response Types
# ============================================================================

class ApiRequest:
    """API request structure"""
    
    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        prompt: str = "",
        size: str = DEFAULT_SIZE,
        n: int = DEFAULT_N,
        negative_prompt: str = DEFAULT_NEGATIVE_PROMPT,
        prompt_extend: bool = DEFAULT_PROMPT_EXTEND,
        watermark: bool = DEFAULT_WATERMARK,
        seed: Optional[int] = None,
    ):
        self.model = model
        self.prompt = prompt
        self.size = size
        self.n = n
        self.negative_prompt = negative_prompt
        self.prompt_extend = prompt_extend
        self.watermark = watermark
        self.seed = seed
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to API request dictionary"""
        params: Dict[str, Any] = {
            "size": self.size,
            "n": self.n,
            "prompt_extend": self.prompt_extend,
            "watermark": self.watermark,
        }
        
        if self.negative_prompt:
            params["negative_prompt"] = self.negative_prompt
        
        if self.seed is not None:
            params["seed"] = self.seed
        
        return {
            "model": self.model,
            "input": {
                "messages": [
                    {
                        "role": "user",
                        "content": [{"text": self.prompt}],
                    }
                ],
            },
            "parameters": params,
        }


class ApiResponse:
    """API response structure"""
    
    def __init__(self, data: Dict[str, Any]):
        self.raw = data
        self.output = data.get("output", {})
        self.usage = data.get("usage", {})
        self.request_id = data.get("request_id", "")
        self.code = data.get("code")
        self.message = data.get("message")
    
    @property
    def image_urls(self) -> List[str]:
        """Extract image URLs from response"""
        urls = []
        choices = self.output.get("choices", [])
        for choice in choices:
            message = choice.get("message", {})
            content = message.get("content", [])
            for item in content:
                if "image" in item:
                    urls.append(item["image"])
        return urls
    
    @property
    def success(self) -> bool:
        """Check if response is successful"""
        return self.code is None and len(self.image_urls) > 0
