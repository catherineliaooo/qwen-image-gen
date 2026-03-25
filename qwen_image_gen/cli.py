"""
Command Line Interface for Qwen Image Generation
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Optional

from .types import (
    CliArgs,
    ASPECT_RATIO_PRESETS,
    DEFAULT_SIZE,
    DEFAULT_N,
    DEFAULT_NEGATIVE_PROMPT,
    DEFAULT_PROMPT_EXTEND,
    DEFAULT_WATERMARK,
    MAX_IMAGES,
    MAX_SEED,
    MAX_PROMPT_LENGTH,
    MAX_NEGATIVE_PROMPT_LENGTH,
)
from .config import (
    get_api_key,
    check_setup,
    validate_size,
    load_preferences,
    run_setup_wizard,
)
from .api import generate_and_download


def print_usage() -> None:
    """Print usage information"""
    print("""
Qwen Image Generation - AI image generation using Qwen Image 2.0 Pro

Usage:
  python -m qwen_image_gen --prompt "描述文字" --image output.png
  qwen-image-gen --prompt "描述文字" --image output.png

Options:
  -p, --prompt <text>       Prompt text (required)
  --image <path>            Output image path (required)
  --size <WxH>              Image size, e.g., 1024*1024, 1920*1080 (default: 2048*2048)
  --ar <ratio>              Aspect ratio: 1:1, 16:9, 9:16, 4:3, 3:4 (overrides --size)
  --n <count>               Number of images, 1-6 (default: 1)
  --negative-prompt <text>  Negative prompt (default: built-in quality improvements)
  --no-prompt-extend        Disable prompt extension
  --watermark               Add Qwen-Image watermark
  --seed <number>           Random seed, 0-2147483647
  --api-key <key>           API key (overrides config)
  --json                    Output in JSON format
  --check-setup             Check if API key is configured (returns JSON status)
  --setup                   Interactive setup wizard for first-time users
  -h, --help                Show help

Size Constraints:
  - Total pixels must be between 512×512 and 2048×2048
  - Format: <width>*<height>

Aspect Ratios:
  - 1:1  → 2048×2048 (正方形)
  - 16:9 → 2048×1152 (横图)
  - 9:16 → 1152×2048 (竖图)
  - 4:3  → 2048×1536 (横图)
  - 3:4  → 1536×2048 (竖图)

Environment Variables:
  DASHSCOPE_API_KEY         Alibaba DashScope API Key

Config Files (priority order):
  1. .qwen-image-gen/.env   (project directory)
  2. ~/.qwen-image-gen/.env (user home)

Preferences File:
  ~/.qwen-image-gen/EXTEND.md  (user preferences for defaults)
""")


def parse_args(argv: list[str]) -> CliArgs:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Qwen Image Generation - AI image generation using Qwen Image 2.0 Pro",
        add_help=False,
    )
    
    parser.add_argument("-p", "--prompt", type=str, help="Prompt text (required)")
    parser.add_argument("--image", type=str, help="Output image path (required)")
    parser.add_argument("--size", type=str, default=DEFAULT_SIZE, help="Image size (default: 2048*2048)")
    parser.add_argument(
        "--ar",
        type=str,
        choices=list(ASPECT_RATIO_PRESETS.keys()),
        help="Aspect ratio (overrides --size)",
    )
    parser.add_argument("--n", type=int, default=DEFAULT_N, help="Number of images (default: 1)")
    parser.add_argument("--negative-prompt", type=str, default=DEFAULT_NEGATIVE_PROMPT, help="Negative prompt")
    parser.add_argument("--no-prompt-extend", action="store_true", help="Disable prompt extension")
    parser.add_argument("--watermark", action="store_true", help="Add watermark")
    parser.add_argument("--seed", type=int, help="Random seed")
    parser.add_argument("--api-key", type=str, help="API key (overrides config)")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--check-setup", action="store_true", help="Check if API key is configured")
    parser.add_argument("--setup", action="store_true", help="Interactive setup wizard")
    parser.add_argument("-h", "--help", action="store_true", help="Show help")
    
    args = parser.parse_args(argv)

    return CliArgs(
        prompt=args.prompt,
        image_path=args.image,
        size=args.size,
        ar=args.ar,
        n=args.n,
        negative_prompt=args.negative_prompt,
        prompt_extend=not args.no_prompt_extend,
        watermark=args.watermark,
        seed=args.seed,
        api_key=args.api_key,
        json_output=args.json,
        help=args.help,
        check_setup=args.check_setup,
        setup=args.setup,
        no_prompt_extend=args.no_prompt_extend,
    )


async def main_async(argv: Optional[list[str]] = None) -> int:
    """Main async entry point"""
    args = parse_args(argv or sys.argv[1:])
    
    # Show help
    if args.help:
        print_usage()
        return 0
    
    # Check setup mode
    if args.check_setup:
        setup = await check_setup()
        print(json.dumps({
            "configured": setup.configured,
            "hasPreferences": setup.has_preferences,
            "configPath": setup.config_path,
        }))
        return 0 if setup.configured else 1
    
    # Setup wizard mode
    if args.setup:
        run_setup_wizard()
        return 0
    
    # Validate required arguments
    if not args.prompt:
        print("Error: --prompt is required", file=sys.stderr)
        print_usage()
        return 1
    
    if not args.image_path:
        print("Error: --image is required", file=sys.stderr)
        print_usage()
        return 1
    
    # Validate prompt length
    if len(args.prompt) > MAX_PROMPT_LENGTH:
        print(f"Error: Prompt exceeds maximum length of {MAX_PROMPT_LENGTH} characters", file=sys.stderr)
        return 1
    
    # Validate negative prompt length
    if len(args.negative_prompt) > MAX_NEGATIVE_PROMPT_LENGTH:
        print(f"Error: Negative prompt exceeds maximum length of {MAX_NEGATIVE_PROMPT_LENGTH} characters", file=sys.stderr)
        return 1
    
    # Handle aspect ratio override
    size = args.size
    if args.ar:
        size = ASPECT_RATIO_PRESETS[args.ar]["size"]
    
    # Validate size
    valid, error = validate_size(size)
    if not valid:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    
    # Validate number of images
    if args.n < 1 or args.n > MAX_IMAGES:
        print(f"Error: Number of images must be between 1 and {MAX_IMAGES}", file=sys.stderr)
        return 1
    
    # Validate seed
    if args.seed is not None and (args.seed < 0 or args.seed > MAX_SEED):
        print(f"Error: Seed must be between 0 and {MAX_SEED}", file=sys.stderr)
        return 1
    
    # Get API key
    api_key = await get_api_key(args.api_key)
    
    if not api_key:
        if args.json_output:
            print(json.dumps({
                "error": "API_KEY_NOT_FOUND",
                "message": "未找到 API Key，请先完成设置",
                "hint": "请按以下步骤配置 API Key：",
                "steps": [
                    "1. 访问 https://bailian.console.aliyun.com/",
                    "2. 登录/注册阿里云账号",
                    "3. 创建 API Key（格式：sk-xxx）",
                    "4. 运行配置命令或直接在 AI 编程工具中输入'生成图片'按提示操作",
                ],
                "configMethods": [
                    "自动配置：在 AI 编程工具中输入'生成图片'，按提示输入 API Key",
                    "手动配置：mkdir -p ~/.qwen-image-gen && echo 'DASHSCOPE_API_KEY=sk-xxx' > ~/.qwen-image-gen/.env",
                    "环境变量：export DASHSCOPE_API_KEY=sk-xxx",
                ],
                "getKeyUrl": "https://bailian.console.aliyun.com/",
            }))
        else:
            print("Error: API key not found", file=sys.stderr)
            print("Please set up your API key using:", file=sys.stderr)
            print("  python -m qwen_image_gen --setup", file=sys.stderr)
        return 1
    
    # Load user preferences (for defaults)
    prefs = load_preferences()
    
    # Apply preferences if not explicitly set
    if args.n == DEFAULT_N and prefs.n != DEFAULT_N:
        args.n = prefs.n
    
    # Print status (non-JSON mode)
    if not args.json_output:
        print(f"🎨 Generating {args.n} image(s)...")
        prompt_preview = args.prompt[:100] + "..." if len(args.prompt) > 100 else args.prompt
        print(f"📝 Prompt: {prompt_preview}")
        print(f"📐 Size: {size}")
        print(f"✨ Prompt Extend: {'ON' if args.prompt_extend else 'OFF'}")
    
    try:
        # Generate and download
        output_path = Path(args.image_path)
        results, response = await generate_and_download(
            prompt=args.prompt,
            api_key=api_key,
            output_path=output_path,
            size=size,
            n=args.n,
            negative_prompt=args.negative_prompt,
            prompt_extend=args.prompt_extend,
            watermark=args.watermark,
            seed=args.seed,
            json_output=args.json_output,
        )
        
        # Output results
        if args.json_output:
            print(json.dumps({
                "success": all(r.success for r in results),
                "images": [
                    {"path": r.path, "success": r.success, "error": r.error}
                    for r in results
                ],
                "usage": response.usage if response else {},
                "requestId": response.request_id if response else "",
            }, indent=2))
        else:
            successful = sum(1 for r in results if r.success)
            failed = len(results) - successful
            print(f"\n✅ Completed: {successful} saved, {failed} failed")
        
        # Exit with error if any failed
        return 0 if all(r.success for r in results) else 1
        
    except Exception as e:
        if args.json_output:
            print(json.dumps({
                "error": "FATAL_ERROR",
                "message": str(e),
            }, indent=2))
        else:
            print(f"Error: {e}", file=sys.stderr)
        return 1


def main(argv: Optional[list[str]] = None) -> int:
    """Main entry point (synchronous wrapper)"""
    import asyncio
    return asyncio.run(main_async(argv))


if __name__ == "__main__":
    sys.exit(main())
