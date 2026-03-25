# Qwen Image Generation 🎨

AI image generation using Alibaba's **Qwen Image 2.0 Pro** model. Excellent at rendering complex Chinese and English text in images.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Quick Start

### 1. Get API Key

Visit [Alibaba Bailian Console](https://bailian.console.aliyun.com/) to create your API key (format: `sk-xxx`).

### 2. Install

```bash
pip install qwen-image-gen
```

Or for development:

```bash
pip install -e .
```

### 3. Configure API Key

```bash
# Option 1: Setup wizard
qwen-image-gen --setup

# Option 2: Manual config
mkdir -p ~/.qwen-image-gen
echo "DASHSCOPE_API_KEY=sk-xxx" > ~/.qwen-image-gen/.env

# Option 3: Environment variable
export DASHSCOPE_API_KEY=sk-xxx
```

### 4. Generate Images

```bash
# Simple generation
qwen-image-gen --prompt "A cute cat sitting on a sofa" --image cat.png

# With options
qwen-image-gen -p "A sunset landscape" --ar 16:9 --watermark --image sunset.png

# Check setup
qwen-image-gen --check-setup
```

---

##  AI Coding Tools Integration

This skill supports multiple AI coding assistants. Add the following configuration to your project:

### OpenClaw

Create `.openclaw/config.json`:

```json
{
  "skills": [
    {
      "name": "qwen-image-gen",
      "type": "python",
      "entry": "qwen_image_gen.cli:main",
      "trigger": ["generate image", "create image", "draw", "生成图片", "画图"]
    }
  ]
}
```

### Cursor (CC)

Add to `.cursor/rules/qwen-image-gen.mdc`:

```markdown
---
name: qwen-image-gen
description: AI image generation using Qwen Image 2.0 Pro
trigger: generate image, create image, draw, 生成图片
---

When user wants to generate an image:

1. Check setup: `qwen-image-gen --check-setup`
2. If not configured, guide user to get API key from https://bailian.console.aliyun.com/
3. Collect parameters:
   - Prompt (required): Image description
   - Aspect ratio: 1:1, 16:9, 9:16, 4:3, 3:4
   - Watermark: yes/no
   - Prompt extend: on/off (default: on)
4. Run: `qwen-image-gen --prompt "{PROMPT}" --ar {RATIO} --image {OUTPUT}.png`
```

### OpenCode

Add to `.opencode/skills/qwen-image-gen.json`:

```json
{
  "name": "qwen-image-gen",
  "description": "AI image generation using Qwen Image 2.0 Pro",
  "language": "python",
  "module": "qwen_image_gen.cli",
  "function": "main",
  "triggers": ["generate image", "create image", "draw", "生成图片"],
  "workflow": {
    "step1": "Check setup with --check-setup",
    "step2": "Collect prompt and options from user",
    "step3": "Execute with collected parameters"
  }
}
```

### Codex (GitHub Copilot)

Add comment in your code:

```python
# QWEN-IMAGE-GEN-SKILL
# When user asks to generate images:
# 1. Check: qwen-image-gen --check-setup
# 2. Collect: prompt, aspect_ratio, watermark, prompt_extend
# 3. Run: qwen-image-gen --prompt "..." --ar 16:9 --image output.png
```

### Qwen Code (Native)

Create `~/.qwen/skills/qwen-image-gen-python/SKILL.md`:

```markdown
---
name: qwen-image-gen-python
description: AI image generation using Qwen Image 2.0 Pro (Python version)
version: 1.0.0
---

See README.md for full documentation.
```

---

## 📋 CLI Options

| Option | Description | Default |
|--------|-------------|---------|
| `-p, --prompt <text>` | Prompt text (required) | - |
| `--image <path>` | Output image path (required) | - |
| `--size <WxH>` | Image size (e.g., `2048*2048`) | `2048*2048` |
| `--ar <ratio>` | Aspect ratio: `1:1`, `16:9`, `9:16`, `4:3`, `3:4` | - |
| `--n <count>` | Number of images (1-6) | `1` |
| `--negative-prompt <text>` | Negative prompt | Built-in |
| `--no-prompt-extend` | Disable prompt extension | Off |
| `--watermark` | Add Qwen watermark | Off |
| `--seed <number>` | Random seed (0-2147483647) | Random |
| `--api-key <key>` | API key (overrides config) | Config file |
| `--json` | Output in JSON format | Off |
| `--check-setup` | Check API key configuration | - |
| `--setup` | Interactive setup wizard | - |
| `-h, --help` | Show help | - |

---

## 📐 Aspect Ratios

| Ratio | Size | Use Case |
|-------|------|----------|
| `1:1` | 2048×2048 | Square, avatars, icons |
| `16:9` | 2048×1152 | Landscape, covers, banners |
| `9:16` | 1152×2048 | Portrait, phone wallpapers |
| `4:3` | 2048×1536 | Landscape, presentations |
| `3:4` | 1536×2048 | Portrait, posters |

---

## 🔧 Configuration

### API Key Priority

1. CLI argument (`--api-key`)
2. Project config (`.qwen-image-gen/.env`)
3. User config (`~/.qwen-image-gen/.env`)
4. Environment variable (`DASHSCOPE_API_KEY`)

### User Preferences (`~/.qwen-image-gen/EXTEND.md`)

```markdown
---
default_aspect_ratio: 16:9
default_quality: 2k
prompt_extend: true
watermark: false
negative_prompt: "低分辨率，低画质，肢体畸形..."
n: 1
---
```

---

## 📚 Examples

### Basic Generation

```bash
qwen-image-gen --prompt "A cute cat" --image cat.png
```

### Poster with Text

```bash
qwen-image-gen \
  --prompt "E-commerce sale poster with 'Big Sale' text" \
  --ar 9:16 \
  --image poster.png
```

### Multiple Variations

```bash
qwen-image-gen \
  --prompt "Minimalist logo design" \
  --n 4 \
  --image logo.png
```

### With Custom Seed

```bash
qwen-image-gen \
  --prompt "A sunset landscape" \
  --seed 42 \
  --image sunset.png
```

---

## ⚠️ Troubleshooting

### API Key Not Found

```
Error: API_KEY_NOT_FOUND
```

**Solution**: Run `qwen-image-gen --setup` or manually create `~/.qwen-image-gen/.env`.

### Prompt Too Long

```
Error: Prompt exceeds maximum length of 800 characters
```

**Solution**: Shorten your prompt to under 800 characters.

### Download Failed

```
✗ Failed to save image.png: Connection timeout
```

**Solution**: The image URL is provided. Download manually:

```bash
curl -L "IMAGE_URL" -o "image.png"
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

---

## 🙏 Acknowledgments

- Powered by [Alibaba Qwen Image 2.0 Pro](https://help.aliyun.com/zh/model-studio/qwen-image-api)
- Built with Python and aiohttp
