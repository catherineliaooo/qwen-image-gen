---
name: qwen-image-gen-python
description: AI image generation using Alibaba Qwen Image 2.0 Pro (Python version). Supports text-to-image with excellent Chinese and English text rendering. Use when user asks to generate, create, or draw images.
version: 1.0.0
metadata:
  openclaw:
    homepage: https://help.aliyun.com/zh/model-studio/qwen-image-api
    requires:
      anyBins:
        - python3
        - pip
---

# Qwen Image Generation (Python)

AI image generation using Alibaba's Qwen Image 2.0 Pro model. Excellent at rendering complex Chinese and English text in images.

---

## 🚀 Quick Start

### 3 Steps to Generate Images

**1️⃣ Get API Key** (First time only)
- Visit: https://bailian.console.aliyun.com/
- Login/Register Alibaba Cloud account
- Create API Key (format: `sk-xxx`)

**2️⃣ In AI Coding Tool, input:**
```
帮我生成一张图片
```

**3️⃣ Follow prompts:**
- Describe the image
- Select aspect ratio
- Confirm generation

### Verify Installation

```bash
python -m qwen_image_gen --check-setup
# or
qwen-image-gen --check-setup
```

Expected output:
```json
{"configured": true, "hasPreferences": false}
```

---

## ⚠️ IMPORTANT: Interactive Workflow ⛔ REQUIRED

**DO NOT execute the script directly without parameters.** The script is a CLI tool, not interactive.

When user wants to generate an image, follow this workflow:

### Step-by-Step Workflow

```
User: "生成图片" / "generate image" / "帮我画一张图"
         │
         ▼
┌─────────────────────────────────────┐
│ Step 0: Check Setup                 │
│ Run: --check-setup                  │
│ If not configured → First-Time Setup│
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Step 1a: ask_followup_question      │
│ Collect prompt (text input)         │
│ "请描述您想要生成的图片内容"          │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Step 1b: AskUserQuestion            │
│ Collect options (multiple choice)   │
│ - aspect_ratio                      │
│ - prompt_extend                     │
│ - watermark                         │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Step 2: Execute Script              │
│ With collected parameters           │
└─────────────────────────────────────┘
```

**CRITICAL**: Use `ask_followup_question` for text input, then `AskUserQuestion` for options.

---

## Script Directory

**Agent Execution**:
1. `{baseDir}` = this SKILL.md file's directory
2. Script: `python -m qwen_image_gen` or `qwen-image-gen`
3. **Use `python` or `qwen-image-gen`** to run the script

---

## Step 0: Check Setup ⛔ BLOCKING

**CRITICAL**: This step MUST complete BEFORE any image generation. Do NOT skip or defer.

Run this command to check if setup is complete:

```bash
python -m qwen_image_gen --check-setup
```

**Response**:
```json
{
  "configured": true|false,
  "hasPreferences": true|false,
  "configPath": "~/.qwen-image-gen"
}
```

| configured | Action |
|-----------|--------|
| `true` | Continue to Step 1 |
| `false` | ⛔ Run First-Time Setup below |

---

## First-Time Setup ⛔ BLOCKING

> ⛔ **CRITICAL: DO NOT use AskUserQuestion for API Key input!**
>
> `AskUserQuestion` requires `options` array (2-4 items) for EVERY question.
> **Use `ask_followup_question` tool instead for API Key text input.**

When `configured: false`, use **ask_followup_question** to collect API Key (text input):

```
欢迎使用 Qwen Image Generation！🎨

请从阿里云百炼获取 API Key:
👉 https://bailian.console.aliyun.com/

请输入您的 API Key (sk-xxx):
```

Save the API key:
```bash
mkdir -p ~/.qwen-image-gen
echo "DASHSCOPE_API_KEY=sk-xxx" > ~/.qwen-image-gen/.env
```

After saving, show confirmation:
```
✅ API Key 已保存！
现在您可以开始生成图片了。
```

---

## Step 1: Collect Generation Parameters ⛔ BLOCKING

Due to tool limitations, collect parameters in **two steps**:

### ⚠️ Tool Limitations

**AskUserQuestion** requires `options` array (2-4 items) for EVERY question - no text input support.

**Solution**: Use two different tools:
1. `ask_followup_question` for free text input (图片内容)
2. `AskUserQuestion` for multiple choice options (比例、智能改写、水印)

---

### Step 1a: Collect Prompt (TEXT INPUT)

> ⛔ **CRITICAL: DO NOT use AskUserQuestion for text input!**
>
> `AskUserQuestion` requires `options` array (2-4 items) for EVERY question.
> It does NOT support free text input - using it will cause this error:
> ```
> Question 1: "options" must contain between 2 and 4 options.
> ```
>
> **Use `ask_followup_question` tool instead for any text input.**

**Use `ask_followup_question` to get image description:**

```
🎨 请描述您想要生成的图片内容

描述越详细，生成效果越好。例如：
• 米开朗基罗名画"创造亚当"构图，左侧哈士奇向左横躺屈曲左腿并伸出左臂躺在地上，食指伸出，右侧狸花猫趴在云上伸出食指与亚当相触，大师构图，杰作，丰富颜色及细节，米开朗基罗风格，它们手指接触的中间有发散性强烈光芒。
• 以蓝色为主色调的促销海报，宣传的是 "春日爱宠季" 活动，品牌为 "Qwen"。画面中央，特写一只非常可爱的大眼睛橘猫从克莱因蓝色的撕开的纸中探出，大猫头萌萌的眼神特写，前爪伸向下方装满各类宠物用品（如带有 "Qwen" 标识的猫粮、猫条、猫罐头等）的蓝色盒子。左侧有白色的猫碗，旁边还有一个毛茸茸的宠物玩具。右侧堆叠着带有丝带的蓝色礼盒。上方有白色的 "春日爱宠季" 艺术大字，左侧有 "Spring of Joyfulness" 文字。左下角标注活动时间"2 月 1 日 -3 月 15 日"，右下角有 "全场每 200 减 30" 的白色文字，背景是纯净的克莱因蓝色，整体构图围绕宠物和促销活动展开，充满温馨欢快的氛围。
• 电影海报风格，浪漫氛围，暖色调夕阳光线（橙金色光晕），年轻女性与男性亲密对视特写：女性长发微卷，佩戴精致耳环，眼神温柔；男性短发，侧脸靠近女性，表情深情。文字内容严格按位置布局：左上角：红色书法字体"小 A" 和 小号英文"XIAO A"（字体清晰无模糊）；右上角：红色书法字体"小 B" 和 小号英文"XIAO B"（字体清晰无模糊）；中央偏下：手写毛笔字"S 城待星归"（白色流畅行书手写体笔触，带书法飞白效果）；标题右侧：英文"SCheng Star."（浅金色衬线字体，句点保留）；右下角：半透明金鱼元素（橙红色金鱼游动，带光斑特效）。整体构图：人物占据 70% 画面，背景为模糊的暖色光晕（模拟夕阳余晖），朦胧感，浅景深虚化，电影级光影质感。cinematic lighting，film grain texture
• 一幅宋代宫廷风格工笔重彩画：画面中央为一位身着淡青色齐胸襦裙、披浅绯色薄纱披帛的偏瘦年轻宫女，立于雕花汉白玉栏杆旁的杏花树下翩然起舞，衣袖舒展如云，裙裾微扬，足尖轻点青砖地面，姿态柔婉而端庄；背景为春日皇家苑囿，枝头盛放粉白相间的重瓣杏花，花瓣随风轻落，树影婆娑；远处可见一角飞檐翘角的宫殿轮廓与半掩的朱红宫墙；左上角一泓清池初解冻，浮着细碎冰晶，画面右上方悬垂一道素雅湘竹帘，帘旌正被微风悄然吹动。整幅画采用绢本设色，色调清丽雅致。画面自上而下、自右向左以瘦金体工整题写全文："帘旌微动，峭寒天气，\n龙池冰泮。\n杏花笑吐香犹浅，\n又还是、春将半。\n清歌妙舞从头按。\n等芳时开宴。\n记去年、对著东风，\n曾许不负莺花愿。" 字体纤劲挺拔，笔锋锐利如削，墨色乌亮。

请描述您想生成的图片：
```

Store user response as `prompt`.

---

### Step 1b: Collect Options (MULTIPLE CHOICE)

**Use `AskUserQuestion` with 3 option questions:**

```json
{
  "questions": [
    {
      "question": "📐 选择图片比例",
      "header": "图片比例",
      "options": [
        {"label": "1:1 正方形", "description": "2048×2048"},
        {"label": "16:9 横图", "description": "2048×1152"},
        {"label": "9:16 竖图", "description": "1152×2048"},
        {"label": "3:4 竖图", "description": "1536×2048"}
      ],
      "multiSelect": false
    },
    {
      "question": "✨ 智能改写（优化提示词）",
      "header": "智能改写",
      "options": [
        {"label": "开启", "description": "AI 优化提示词（推荐）"},
        {"label": "关闭", "description": "使用原始提示词"}
      ],
      "multiSelect": false
    },
    {
      "question": "💧 水印设置",
      "header": "水印",
      "options": [
        {"label": "不添加", "description": "纯净图片"},
        {"label": "添加水印", "description": "包含 Qwen 标识"}
      ],
      "multiSelect": false
    }
  ]
}
```

**Wait for user response.** Parse and store all parameters.

---

### Default Values

Use these defaults to avoid asking too many questions:

| Parameter | Default | Notes |
|-----------|---------|-------|
| 数量 (`n`) | `1` | Don't ask, use default |
| 反向提示词 | Built-in | Don't ask, use default below |

### Parameter Mapping After Collection

| User Response | Store As |
|---------------|----------|
| 图片内容 | `prompt` (string) |
| 图片比例 | "1:1 正方形"→`1:1`, "16:9 横图"→`16:9`, "9:16 竖图"→`9:16`, "3:4 竖图"→`3:4` |
| 智能改写 | `prompt_extend` (true if "开启", false if "关闭") |
| 水印 | `watermark` (true if "添加水印", false if "不添加") |
| 数量 | `n` = `1` (default) |
| 反向提示词 | `negative_prompt` = default (below) |

---

### Default Negative Prompt

```
低分辨率，低画质，肢体畸形，手指畸形，画面过饱和，蜡像感，人脸无细节，过度光滑，画面具有 AI 感。构图混乱。文字模糊，扭曲。
```

### Note: Other Aspect Ratios

Due to the 4-option limit, some ratios like `4:3` are not listed. If user wants `4:3`:
- Ask follow-up: "您需要 4:3（横图，2048×1536）比例吗？"
- Or user can specify directly: "生成一张 4:3 的图片"

---

## Step 2: Confirm and Generate

Display settings summary:

```
📋 生成设置确认

📝 Prompt: {prompt}
📐 比例：{aspect_ratio}
🔢 数量：{n} 张
✨ 智能改写：{prompt_extend ? "开启" : "关闭"}
💧 水印：{watermark ? "添加" : "不添加"}
🚫 反向提示词：默认

确认生成？(y/n)
```

**If user wants to modify 数量 or 反向提示词:**

Use `ask_followup_question` to collect:

- **数量**: "请输入生成数量（1-6 张）"
- **反向提示词**: "请输入反向提示词（不想出现的内容）"

After modification, display updated summary and execute:

```bash
python -m qwen_image_gen \
  --prompt "{PROMPT}" \
  --ar "{ASPECT_RATIO}" \
  --n {N} \
  {"" if PROMPT_EXTEND else "--no-prompt-extend"} \
  {"--watermark" if WATERMARK else ""} \
  {f'--negative-prompt "{NEGATIVE_PROMPT}"' if NEGATIVE_PROMPT else ""} \
  --image "qwen-image-$(date +%Y%m%d-%H%M%S).png"
```

---

## Quick Generation (Skip Interactive Flow)

If user provides ALL parameters in one message, generate directly without AskUserQuestion:

```
用户：帮我生成一张 16:9 的猫咪图片，不要水印
Agent：正在生成图片...
```

```bash
python -m qwen_image_gen --prompt "一只可爱的猫咪" --ar 16:9 --image cat.png
```

---

## CLI Options

| Option | Description |
|--------|-------------|
| `--prompt <text>`, `-p` | Prompt text (required) |
| `--image <path>` | Output image path (required) |
| `--size <WxH>` | Image size, e.g., `2048*2048` |
| `--ar <ratio>` | Aspect ratio: `1:1`, `16:9`, `9:16`, `4:3`, `3:4` |
| `--n <count>` | Number of images, 1-6 (default: 1) |
| `--negative-prompt <text>` | Negative prompt |
| `--no-prompt-extend` | Disable prompt extension |
| `--watermark` | Add Qwen-Image watermark |
| `--seed <number>` | Random seed (0-2147483647) |
| `--api-key <key>` | API key (overrides config) |
| `--json` | Output in JSON format |
| `--check-setup` | Check if API key is configured |
| `--setup` | Interactive setup wizard |
| `--help`, `-h` | Show help |

---

## Aspect Ratios (2K Resolution)

| Ratio | Size | Pixels | Use Case |
|-------|------|--------|----------|
| `1:1` | 2048×2048 | 4.2MP | 正方形、头像、图标 |
| `16:9` | 2048×1152 | 2.4MP | 横图、封面、海报 |
| `9:16` | 1152×2048 | 2.4MP | 竖图、手机壁纸、海报 |
| `4:3` | 2048×1536 | 3.1MP | 横图、演示文稿 |
| `3:4` | 1536×2048 | 3.1MP | 竖图、海报 |

---

## Size Constraints

**qwen-image-2.0-pro**:
- Min: 512×512
- Max: 2048×2048
- Total pixels must be between 262,144 and 4,194,304

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DASHSCOPE_API_KEY` | Alibaba DashScope API Key |

**Load Priority**: CLI args > project `.qwen-image-gen/.env` > user `~/.qwen-image-gen/.env` > environment variable

---

## Config Files

| File | Location | Purpose |
|------|----------|---------|
| `.env` | `~/.qwen-image-gen/.env` | API Key storage |
| `EXTEND.md` | `~/.qwen-image-gen/EXTEND.md` | User preferences (optional) |

---

## Model Information

| Model | Description |
|-------|-------------|
| `qwen-image-2.0-pro` | Best for complex text rendering, realistic textures, and semantic understanding |

---

## Response

The API returns a URL to the generated image. Images are available for 24 hours and should be downloaded immediately.

---

## Examples

### Interactive mode (recommended)
```
用户：帮我生成一张图片
Agent：[AskUserQuestion 收集参数]
Agent：正在生成图片...
Agent：[显示生成的图片]
```

### Direct generation with all parameters
```bash
python -m qwen_image_gen --prompt "以蓝色为主色调的促销海报，宣传的是 "春日爱宠季" 活动，品牌为 "Qwen"。画面中央，特写一只非常可爱的大眼睛橘猫从克莱因蓝色的撕开的纸中探出，大猫头萌萌的眼神特写，前爪伸向下方装满各类宠物用品（如带有 "Qwen" 标识的猫粮、猫条、猫罐头等）的蓝色盒子。左侧有白色的猫碗，旁边还有一个毛茸茸的宠物玩具。右侧堆叠着带有丝带的蓝色礼盒。上方有白色的 "春日爱宠季" 艺术大字，左侧有 "Spring of Joyfulness" 文字。左下角标注活动时间"2 月 1 日 -3 月 15 日"，右下角有 "全场每 200 减 30" 的白色文字，背景是纯净的克莱因蓝色，整体构图围绕宠物和促销活动展开，充满温馨欢快的氛围。" --image commerceposter.png --ar 9:16
```

### Generate poster with text
```bash
python -m qwen_image_gen --prompt "电影海报风格，浪漫氛围，暖色调夕阳光线（橙金色光晕），年轻女性与男性亲密对视特写：女性长发微卷，佩戴精致耳环，眼神温柔；男性短发，侧脸靠近女性，表情深情。文字内容严格按位置布局：左上角：红色书法字体“小A” 和 小号英文“XIAO A”（字体清晰无模糊）；右上角：红色书法字体“小B” 和 小号英文“XIAO B”（字体清晰无模糊）；中央偏下：手写毛笔字“S城待星归”（白色流畅行书手写体笔触，带书法飞白效果）；标题右侧：英文“SCheng Star.”（浅金色衬线字体，句点保留）；右下角：半透明金鱼元素（橙红色金鱼游动，带光斑特效）。整体构图：人物占据70%画面，背景为模糊的暖色光晕（模拟夕阳余晖），朦胧感，浅景深虚化，电影级光影质感。cinematic lighting，film grain texture'" --image dramaposter.png --ar 9:16
```

### Generate multiple variations
```bash
python -m qwen_image_gen --prompt "一幅宋代宫廷风格工笔重彩画：画面中央为一位身着淡青色齐胸襦裙、披浅绯色薄纱披帛的偏瘦年轻宫女，立于雕花汉白玉栏杆旁的杏花树下翩然起舞，衣袖舒展如云，裙裾微扬，足尖轻点青砖地面，姿态柔婉而端庄；背景为春日皇家苑囿，枝头盛放粉白相间的重瓣杏花，花瓣随风轻落，树影婆娑；远处可见一角飞檐翘角的宫殿轮廓与半掩的朱红宫墙；左上角一泓清池初解冻，浮着细碎冰晶，画面右上方悬垂一道素雅湘竹帘，帘旌正被微风悄然吹动。整幅画采用绢本设色，色调清丽雅致。画面自上而下、自右向左以瘦金体工整题写全文："帘旌微动，峭寒天气，\n龙池冰泮。\n杏花笑吐香犹浅，\n又还是、春将半。\n清歌妙舞从头按。\n等芳时开宴。\n记去年、对著东风，\n曾许不负莺花愿。" 字体纤劲挺拔，笔锋锐利如削，墨色乌亮。" --image textshowcase.png --ar 9:16 --n 2
```

---

## Error Handling

| Error | Solution |
|-------|----------|
| **Missing API key** | Run setup wizard, get key from https://bailian.console.aliyun.com/ |
| **Generation failure** | Auto-retry up to 3 attempts |
| **Invalid size** | Error with valid range hint (512-2048) |
| **API rate limit** | Wait and retry |
| **Download failure** | Shows image URL for manual download, auto-retry up to 3 times with exponential backoff |
