"""
Qwen API client for image generation
"""

import asyncio
import aiohttp
from pathlib import Path
from typing import Optional, List, Tuple

from .types import ApiRequest, ApiResponse, ImageResult, MAX_ATTEMPTS, RETRY_DELAY_MS


async def generate_image(
    prompt: str,
    api_key: str,
    size: str = "2048*2048",
    n: int = 1,
    negative_prompt: str = "",
    prompt_extend: bool = True,
    watermark: bool = False,
    seed: Optional[int] = None,
) -> ApiResponse:
    """
    Generate image using Qwen API
    
    Args:
        prompt: Image description
        api_key: API key for authentication
        size: Image size (e.g., "2048*2048")
        n: Number of images to generate
        negative_prompt: Negative prompt
        prompt_extend: Enable prompt extension
        watermark: Add watermark
        seed: Random seed
    
    Returns:
        ApiResponse object
    """
    request = ApiRequest(
        prompt=prompt,
        size=size,
        n=n,
        negative_prompt=negative_prompt,
        prompt_extend=prompt_extend,
        watermark=watermark,
        seed=seed,
    )
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation",
            headers=headers,
            json=request.to_dict(),
        ) as response:
            data = await response.json()
            return ApiResponse(data)


async def download_image(
    url: str,
    output_path: Path,
    max_retries: int = 3,
) -> ImageResult:
    """
    Download image from URL with retry logic
    
    Args:
        url: Image URL
        output_path: Output file path
        max_retries: Maximum retry attempts
    
    Returns:
        ImageResult with success/failure status
    """
    last_error: Optional[Exception] = None
    
    for attempt in range(1, max_retries + 1):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                    if not response.ok:
                        raise Exception(f"HTTP {response.status}")
                    
                    # Ensure directory exists
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Download and save
                    content = await response.read()
                    output_path.write_bytes(content)
                    
                    return ImageResult(path=str(output_path), success=True)
                    
        except Exception as e:
            last_error = e
            if attempt < max_retries:
                await asyncio.sleep(RETRY_DELAY_MS * attempt / 1000)
    
    return ImageResult(
        path=str(output_path),
        success=False,
        error=str(last_error) if last_error else "Unknown error",
    )


async def generate_and_download(
    prompt: str,
    api_key: str,
    output_path: Path,
    size: str = "2048*2048",
    n: int = 1,
    negative_prompt: str = "",
    prompt_extend: bool = True,
    watermark: bool = False,
    seed: Optional[int] = None,
    json_output: bool = False,
) -> Tuple[List[ImageResult], Optional[ApiResponse]]:
    """
    Generate images and download them
    
    Args:
        prompt: Image description
        api_key: API key
        output_path: Base output path
        size: Image size
        n: Number of images
        negative_prompt: Negative prompt
        prompt_extend: Enable prompt extension
        watermark: Add watermark
        seed: Random seed
        json_output: Output in JSON format
    
    Returns:
        Tuple of (list of ImageResult, ApiResponse)
    """
    from .types import MAX_ATTEMPTS, RETRY_DELAY_MS
    
    # Generate with retry
    response: Optional[ApiResponse] = None
    last_error: Optional[Exception] = None
    
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            response = await generate_image(
                prompt=prompt,
                api_key=api_key,
                size=size,
                n=n,
                negative_prompt=negative_prompt,
                prompt_extend=prompt_extend,
                watermark=watermark,
                seed=seed,
            )
            
            if response.success:
                break
                
        except Exception as e:
            last_error = e
            if not json_output:
                print(f"Attempt {attempt}/{MAX_ATTEMPTS} failed: {e}")
            
            if attempt < MAX_ATTEMPTS:
                if not json_output:
                    print(f"Retrying in {RETRY_DELAY_MS}ms...")
                await asyncio.sleep(RETRY_DELAY_MS / 1000)
    
    if not response or not response.success:
        raise Exception(
            f"Failed to generate image after {MAX_ATTEMPTS} attempts. "
            f"Last error: {last_error}"
        )
    
    # Download images
    image_urls = response.image_urls
    results: List[ImageResult] = []
    
    for i, url in enumerate(image_urls):
        # Handle multiple images
        if len(image_urls) > 1:
            stem = output_path.stem
            suffix = output_path.suffix
            parent = output_path.parent
            img_path = parent / f"{stem}_{i + 1}{suffix}"
        else:
            img_path = output_path
        
        if not json_output:
            print(f"📥 Downloading image {i + 1}/{len(image_urls)}...")
        
        result = await download_image(url, img_path)
        results.append(result)
        
        if result.success:
            if not json_output:
                print(f"✓ Saved: {result.path}")
        else:
            if not json_output:
                print(f"✗ Failed to save {result.path}: {result.error}")
                print(f"🔗 Image URL: {url}")
    
    return results, response
