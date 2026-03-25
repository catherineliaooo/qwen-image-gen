# Qwen Image 2.0 使用手册（持续更新中）
> https://qwen.ai/blog?id=qwen-image-2.0

## 💡 模型亮点速览

Qwen-Image-2.0 是千问专业级图像生成模型，发布于 2026 年 2 月。专注于**专业信息图生成**与**精美照片级真实感图像**生成。

**本次更新核心特性如下：**

*   📝 **文字渲染：** 1k token 指令支持，直出专业信息图，包括 PPT/海报/漫画等
    
*   🖼️ **真实质感：** 2k 分辨率支持，细腻刻画写实场景，包括人物/自然/建筑等
    
*   ✂️ **生图编辑二合一：** 理解生成一体化，一个模型同时支持图像生成与编辑功能
    
*   ⚡ **轻量架构：** 更小模型，更快生成速度，实现效果与性能的最佳平衡
   

| ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/04da72a0-5878-41d5-b625-60165e5ebd92.png) | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/c0c86397-315b-45ac-b83e-44b2b6326ec4.png) | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/a0f3cec9-50f2-44bd-9601-cd20209408b3.png) | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/272cecaa-43ac-462c-b941-effd4056ee71.png) | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/43f5fd3f-c84b-4446-8ca6-3d2c8099cc7d.png) | <img width="1536" height="2048" alt="image" src="https://github.com/user-attachments/assets/24a3f25c-3525-46f4-ba29-d55293a18233" />|
| --- | --- | --- | --- | --- | --- |

| ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/6fed4ba0-28a9-4dda-bf71-ff9ab9556d90.png) | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/955b47d4-6aa1-4bb7-9b52-c14171cb6ad3.png) | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/71c7a5f3-5e95-4c52-9175-426d279f1304.png) | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/3d5b1d66-7f43-476a-a08a-6f4d7590e791.png) | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/05eb02e8-4372-4bbc-85c9-ba8919050e98.png) |
| --- | --- | --- | --- | --- |



---
## 🖼️ 场景 Prompt 示例

> 💡 **使用说明**：以下表格按场景分类展示 Prompt 示例，点击或复制 Prompt 内容进入 [百炼模型体验](https://bailian.console.aliyun.com/cn-beijing?source_channel=K7mP9wR2vA&tab=model#/efm/model_experience_center/vision/imageGenerate) 即可快捷体验。

<img width="2880" height="1626" alt="image" src="https://github.com/user-attachments/assets/deae04ca-5166-421c-b5c9-7d35ea9715f3" />


---

### 高级复杂信息图 ⭐

> **场景描述**：生成专业 PPT 页面、复杂文字海报、多格漫画、教育科普插图等高级信息图。
>
> **适用场景**：
>
> 专业 PPT 设计、信息图表、多格漫画、复杂排版海报
> 
> 教学课件、科普插图、知识卡片、学习图表
>
> **Prompt 要素**：
>
> 内容结构：明确的数据/知识内容
> 
> 布局要求：清晰的排版布局（如横向、纵向、卡片式）
> 
> 风格指定：扁平化、现代、简洁等

| **场景** | **效果** | **Prompt** |
| --- | --- | --- |
| **科普插图（狗狗睡姿）** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/123bf3fd-e80a-4633-9b0f-f07f40932509.png) | `手绘风格宠物科普信息图，背景为米色卷边纸张（带自然卷边效果和柔和投影），标题为"《狗狗睡姿大揭秘》"（手写书法字体，下方配波浪形下划线装饰）。画面包含六种典型狗狗睡姿插图及对应科普内容，所有文字元素均以中文双引号""严格包裹：1. "侧卧"：插图呈现短腿长身、臀部圆润的柯基，四肢自然舒展侧躺，肚皮外露，耳朵放松贴伏，尾巴呈柔和弧线垂落；文字内容"行为描述：放松信任，深度睡眠中，完全不设防""安全感指数：非常有安全感"（绿色五角星形标签），搭配骨头图标与"观察笔记"文字标签；2. "超人趴"：插图呈现毛发蓬松、体型匀称的金毛，前肢向前大幅伸展趴伏，后腿向后蹬直，头部轻抬，耳朵微竖显警觉，整体呈流线型；文字内容"行为描述：随时准备行动，警惕性高，或只是想凉快一下""安全感指数：警惕中"（黄色眼睛图标标签），搭配风扇图标与"太可爱了！"文字标签；3. "卷成圈"：插图呈现毛发卷曲、体型小巧的贵宾，身体紧密蜷缩成圆形，鼻子轻触尾巴尖，四肢收拢护住腹部，耳朵自然覆盖眼部；文字内容"行为描述：保护脆弱部位，保存体温，可能感到不安或寒冷""安全感指数：需要安全感"（蓝色波浪形标签），搭配围巾图标与"记得保暖哦"文字标签；4. "仰面朝天"：插图呈现面部褶皱明显、体型敦实的斗牛犬，四脚朝天完全舒展，肚皮外露，舌头微吐，四肢放松呈"投降"状，表情安详；文字内容"行为描述：极度放松，对环境和主人完全信任，散热好姿势""安全感指数：非常有安全感，信任爆棚！"（绿色心形标签），搭配爱心装饰与"睡得真香哦"文字标签；5. "狮身人面像式"：插图呈现体型纤细、毛发柔顺的约克夏，前肢并拢前伸支撑上身，头部抬起目视前方，后腿蜷于身下，尾巴轻卷贴地，姿态警觉；文字内容"行为描述：半梦半醒，准备随时应对突发情况，浅睡眠""安全感指数：警惕中"（黄色问号标签），搭配时钟图标与"？"文字标签；6. "依靠式"：插图呈现混种特征明显的混种犬，身体紧贴墙壁或家具侧卧，头部自然倚靠支撑物，四肢放松但保持接触姿态，表情依恋；文字内容"行为描述：寻求身体接触和舒适感，需要陪伴和依靠""安全感指数：需要陪伴"（紫色爱心标签），搭配狗碗图标与"Buddy"文字标签；整体设计要求：柔和暖色调（低饱和度米色/浅黄/淡蓝），中文手写字体圆润可爱，画面点缀动态线条元素（箭头指引、星星、爪印装饰），留白充足保证呼吸感，垂直构图，适配小红书平台分享。` |
| **科普插图（大模型）**<br>![capybara.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/74d36883-88ea-4093-b84f-44d3b6f4d9b9.jpeg) | <img width="1536" height="2688" alt="image" src="https://github.com/user-attachments/assets/6ed852bd-73ef-4c19-ae2c-37ce7d33f7d4" />| `讲解 Transformer 的历史与故事，为这个知识点做有趣的九宫格科普漫画（自由分布），二次元漫画风格，由图片一中的卡通人物进行讲解。`<br>> ❗️需要开启 prompt_extend |
| **药物机制科学插图** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/c83290d3-6498-46b9-8125-ec181509ee2b.png)| `请创建一张幻灯片，阐释 GLP-1 药物的作用机制。要求：使用科学插图直观展示其作用原理（如 GLP-1 受体激活、胰岛素/胰高血糖素分泌调控、胃排空延缓、下丘脑饱腹中枢作用等关键环节）；配以专业的中文解说，突出药物如何通过葡萄糖依赖性方式调节血糖并产生减重效果。` |
| **PPT（LLM 发展）** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/6fed4ba0-28a9-4dda-bf71-ff9ab9556d90.png) | `图像标题为"LLM 发展关键突破与经济影响"，位于顶部中央，采用深灰色无衬线粗体字，简洁专业。整体为麦肯锡风格商务信息图，纯白背景，布局清晰、留白充足，配色以深蓝、科技蓝与浅灰为主，图标为扁平化矢量风格。上半部分为时间轴结构，横向贯穿画面中上区域，标注四个关键节点：左起"2013 — Word2Vec：分布式词向量表示"；"2017 — Transformer 架构：自注意力机制奠基"；"2018 — BERT & GPT-1：双向/单向预训练范式确立"；"2022 — ChatGPT：规模化对话能力引爆应用落地"。每个节点配简约蓝色圆点图标与垂直连接线，文字使用深灰常规字体，关键年份加粗。下半部分分为左右两个对比区块：左侧标题为"技术跃迁驱动因素"，含三个并列图标卡片——上方为"算力增长"，配芯片图标与文字"GPU 算力提升 300 倍（2012–2022）"；中部为"数据规模"，配数据库图标与文字"互联网文本超 10TB，清洗语料达万亿 token"；下方为"算法优化"，配齿轮图标与文字"稀疏激活、混合专家（MoE）、RLHF 对齐"。右侧标题为"宏观经济影响（2023–2030 预测）"，含三组数据条：顶部为"全球 AI 相关 GDP 贡献"，数值"$4.4 万亿"，配上升箭头图标；中部为"知识工作自动化率"，数值"27% 岗位任务可被 LLM 增强"；底部为"企业生产率提升中位数"，数值"+12%（高采纳行业）"。所有文字均使用中文双引号明确标出，图像中未出现任何其他文字或人像元素。` |
| **PPT（古文教学）** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/81d0b08a-684a-4a6b-9ddb-f48bba1fb4fa.png) | `一幅宋代宫廷风格工笔重彩画：画面中央为一位身着淡青色齐胸襦裙、披浅绯色薄纱披帛的偏瘦年轻宫女，立于雕花汉白玉栏杆旁的杏花树下翩然起舞，衣袖舒展如云，裙裾微扬，足尖轻点青砖地面，姿态柔婉而端庄；背景为春日皇家苑囿，枝头盛放粉白相间的重瓣杏花，花瓣随风轻落，树影婆娑；远处可见一角飞檐翘角的宫殿轮廓与半掩的朱红宫墙；左上角一泓清池初解冻，浮着细碎冰晶，画面右上方悬垂一道素雅湘竹帘，帘旌正被微风悄然吹动。整幅画采用绢本设色，色调清丽雅致。画面自上而下、自右向左以瘦金体工整题写全文："帘旌微动，峭寒天气，\n龙池冰泮。\n杏花笑吐香犹浅，\n又还是、春将半。\n清歌妙舞从头按。\n等芳时开宴。\n记去年、对著东风，\n曾许不负莺花愿。" 字体纤劲挺拔，笔锋锐利如削，墨色乌亮。` |
| **PPT（古文教学）** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/844db0fb-c818-4a2a-a993-1d48fe21f6c7.png) | `一幅水墨设色长卷风格中国画。 画面中央偏右绘一位魏晋风度的文人雅士，身着宽袖素色交领袍服，头戴小冠，跽坐于兰亭水畔青石之上，左手轻抚膝前古琴，右侧远景为会稽山阴连绵青黛山峦，山间隐现曲径与飞檐亭角；近景溪水蜿蜒，留白处氤氲水气。画面自上而下、自右向左用王羲之小楷写着"永和九年，岁在癸丑，暮春之初，\n会于会稽山阴之兰亭，修禊事也。\n群贤毕至，少长咸集。\n此地有崇山峻岭，茂林修竹，\n又有清流激湍，映带左右，\n引以为流觞曲水，列坐其次。\n虽无丝竹管弦之盛，一觞一咏，\n亦足以畅叙幽情。是日也，\n天朗气清，惠风和畅。\n仰观宇宙之大，俯察品类之盛，\n所以游目骋怀，足以极视听之娱，\n信可乐也。夫人之相与，俯仰一世。\n或取诸怀抱，悟言一室之内；\n或因寄所托，放浪形骸之外。\n虽趣舍万殊，静躁不同，\n当其欣于所遇，暂得于己，\n快然自足，不知老之将至。\n及其所之既倦，情随事迁，感慨系之矣。\n向之所欣，俯仰之间，已为陈迹，\n犹不能不以之兴怀，况修短随化，\n终期于尽！古人云，死生亦大矣。\n岂不痛哉！每览昔人兴感之由，若合一契，\n未尝不临文嗟悼，不能喻之于怀。\n固知一死生为虚诞，齐彭殇为妄作。\n后之视今，亦犹今之视昔，悲夫！\n故列叙时人，录其所述，虽世殊事异，\n所以兴怀，其致一也。\n后之览者，亦将有感于斯文。"` |
| **PPT（除法教学）** | <img width="2688" height="1536" alt="image" src="https://github.com/user-attachments/assets/47073059-bee5-43c0-bfbe-176f2ba68629" />| `Create a slide to help first graders learn the basic concepts behind division and go through the example of 75 divided by 5. Use a fun cartoon Egyptian theme to engage the students.` |
| **多格漫画** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/955b47d4-6aa1-4bb7-9b52-c14171cb6ad3.png) | `一套四格漫画风格的可爱马年主题插画，采用明亮活泼的暖色调（米黄、浅橙、嫩绿、明黄），搭配纯黑粗线条勾勒，营造出轻松治愈的萌系氛围。背景为浅米色，带有"BUNNY HORSE"的淡灰色底纹。主角设定：一只名为"马哈哈"的卡通马，主体为暖橙黄色，带有浅棕色斑点，表情丰富（翻白眼、无奈、嫌弃等）。四格内容：左上格马哈哈坐在马桶上用力拉屎；右上格马哈哈瞪眼看着章鱼小丸子；左下格马哈哈戴着黑色假发双马尾；右下格马哈哈戴着绿色发箍表情嫌弃。每格都有圆角矩形边框，配文幽默风趣。` |
| **手帐风旅行插画** | <img width="1536" height="2688" alt="image" src="https://github.com/user-attachments/assets/93cfce6c-7408-45ce-bd8d-1917c9e89cfd" />| `手帐风上海旅行插画，分四天场景呈现：第一天外滩和南京路步行街（画外滩建筑群剪影、南京路百年商铺、街头小笼包摊位）；第二天豫园和城隍庙（画豫园九曲桥、湖心亭、城隍庙老街小吃）；第三天浦东陆家嘴和滨江（画东方明珠、上海中心、黄浦江游船）；第四天武康路和田子坊（画武康大楼、文艺咖啡馆、石库门小店）。每个场景角落有手写日期标注（如"Day1 外滩寻味"）。搭配云朵、太阳、行李箱、小飞机、梧桐叶等装饰元素，风格可爱温馨，线条柔和，色彩明快。` |

### AI 短剧/漫剧

> **场景描述**：生成短剧剧照、海报、漫剧分镜等图片，支持分镜生成和角色连贯形象。
>
> **适用场景**：短剧宣传海报、剧照生成、漫剧分镜设计、角色定妆照、剧情场景概念图、多角度角色生成
>
> **Prompt 要素**：
>
> 剧情设定：剧情背景与设定、角色特征与关系
> 
> 场景氛围：场景氛围、构图与视角
> 
> 风格参考：风格参考（古装、现代、奇幻等）

| **场景** | **效果** | **Prompt** |
| --- | --- | --- |
| **短剧宣传海报 1** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/04da72a0-5878-41d5-b625-60165e5ebd92.png) | `电影海报风格，浪漫氛围，暖色调夕阳光线（橙金色光晕），年轻女性与男性亲密对视特写：女性长发微卷，佩戴精致耳环，眼神温柔；男性短发，侧脸靠近女性，表情深情。文字内容严格按位置布局：左上角：红色书法字体"小 A" 和 小号英文"XIAO A"（字体清晰无模糊）；右上角：红色书法字体"小 B" 和 小号英文"XIAO B"（字体清晰无模糊）；中央偏下：手写毛笔字"S 城待星归"（白色流畅行书手写体笔触，带书法飞白效果）；标题右侧：英文"SCheng Star."（浅金色衬线字体，句点保留）；右下角：半透明金鱼元素（橙红色金鱼游动，带光斑特效）。整体构图：人物占据 70% 画面，背景为模糊的暖色光晕（模拟夕阳余晖），朦胧感，浅景深虚化，电影级光影质感。cinematic lighting，film grain texture` |
| **短剧宣传海报 2** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/62e01cde-dd37-4853-8722-ea33d4d60f72.png) | `古装剧电影海报，暖红底色（#C3272B）带金色光晕，谢予望饰陆怀川（深色刺绣古装，玉佩）与黄云云饰宋槿乔（浅色金线古装，珍珠项链）亲密特写：鼻尖相触，女子手搭男子胸前。文字严格按位置布局：左侧竖排："小 A 饰 陆公子" 和 拼音"XIAO A" "LU GONGZI"（红色书法体，贴合男子肩部）；右侧竖排："小 B 饰 宋小姐" + 拼音"XIAO B" "SONG XIAOJIE"（红色书法体，贴合女子发髻）；中央：大字"王妃"（金色闪光书法字体，居中偏下）；底部："【改编自《王妃》原著：千问】"（白色小字，瘦金体，底部居中）。电影级光影，柔光无阴影，35mm 胶片颗粒感，绢布纹理背景。` |
| **漫剧宣传海报** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/c0c86397-315b-45ac-b83e-44b2b6326ec4.png) | `一张高质量的国漫风格封面图，动态漫海报风格。画面构图分为前后两层。后景：一对年轻男女。男子黑发冷酷，身穿黑色夹克内搭白色 T 恤，戴着银色项链，右手持一把黑色手枪指向前方，眼神犀利。女子拥有银白色长发，身穿红色外套和白色连衣裙，温柔地挽着男子的手臂，表情依赖。前景：一个非常可爱的小女孩特写，占据画面下方很大比例。她留着深棕色齐刘海短发，有着巨大的闪亮金色眼睛，表情兴奋开心，双手握拳放在胸前，头上有两个白色的毛球发饰。背景：深蓝色的背景，带有模糊的圆形光斑（Bokeh 效果），营造出都市夜晚或梦幻的氛围。文字元素：画面底部中央位置有醒目的红色粗体汉字标题"特工奶爸"，字体设计带有力量感和金属质感，艺术化，带有战斗气息的笔触效果。画质：8k 分辨率，色彩鲜艳，线条清晰，赛璐璐上色。` |
| **漫画分镜生成** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/cee1459d-2b7e-4bd4-8e00-b65ba3407a91.png) | `一幅高质量的二次元厚涂风格插画，游戏概念艺术。黄昏时分，巨大的红日悬挂在地平线，光芒万丈。前景是随风飘动的金色芦苇。画面主体是一位长发侠客，头戴斗笠，身形呈现剪影效果，身穿黑色长袍。他手持长剑直指镜头，剑身反射着刺眼的金光。艺术风格：类似《对马岛之魂》或《原神》的 CG 过场动画风格，半写实动漫风 (Semi-realistic anime)，数字绘画，笔触明显，色彩高饱和度，红橙色调主导。强烈的逆光，轮廓光 (Rim light)，丁达尔效应，史诗感，杰作，8k 分辨率，Unreal Engine 5 渲染质感。` |

---

### 广告/创意/营销

> **场景描述**：生成中英混合排版的专业海报，包括活动宣传、产品推广、品牌宣传、电商营销、IP 设计等。
>
> **适用场景**：
>
> 活动宣传海报、产品推广图、品牌宣传物料、促销广告图
> 
> 商品主图、详情页插图、促销活动图、场景化展示
> 
> IP 形象设计、周边产品开发、品牌 IP 孵化
>
> **Prompt 要素**：
>
> 主题文案：海报主题与文案、商品特征
> 
> 视觉风格：视觉风格、色彩偏好
> 
> 排版要求：排版布局、营销氛围

| **场景** | **效果** | **Prompt** |
| --- | --- | --- |
| **宠物用品促销海报** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/9e71f69b-7998-44c0-b2e9-40e8ce651fbf.png) | `以蓝色为主色调的促销海报，宣传的是"春日爱宠季"活动，品牌为"Qwen"。画面中央，特写一只非常可爱的大眼睛橘猫从克莱因蓝色的撕开的纸中探出，大猫头萌萌的眼神特写，前爪伸向下方装满各类宠物用品（如带有"Qwen"标识的猫粮、猫条、猫罐头等）的蓝色盒子。左侧有白色的猫碗，旁边还有一个毛茸茸的宠物玩具。右侧堆叠着带有丝带的蓝色礼盒。上方有白色的"春日爱宠季"艺术大字，左侧有"Spring of Joyfulness"文字。左下角标注活动时间"2 月 1 日 -3 月 15 日"，右下角有"全场每 200 减 30"的白色文字，背景是纯净的克莱因蓝色，整体构图围绕宠物和促销活动展开，充满温馨欢快的氛围。` |
| **女神节可爱风促销海报** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/a0f3cec9-50f2-44bd-9601-cd20209408b3.png) | `一张可爱风促销海报，整体以粉色和蓝色等柔和色彩为主，充满毛绒质感的设计风格。画面上方有粉色毛绒字体的"3.8 提前购 放肆嗨购 满额惠享"文字，其中"放肆嗨购"字体较大且醒目，旁边还有黄色笑脸标识和"福利大放送"文字。中间偏上位置有橙色背景区域，上面写着"WOMEN'S DAY"，巨大购物袋有可爱眼睛和笑脸，还有粉色和蓝色的毛绒购物袋，上面分别标有"%"符号。画面右侧有一个蓝色和粉色毛绒组成的巨大喇叭，左侧有带蝴蝶结的礼盒。下方粉色背景区域有白色的"限时秒杀 女神嗨购"文字，下方展示了三个优惠活动："消费满 200 元减 50""充 200 得 240""消费满 100 元减 20"。整体构图活泼可爱，充满促销的热闹感。` |
| **波普风趣味海报** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/272cecaa-43ac-462c-b941-effd4056ee71.png) | `波普风的趣味海报，以浅灰色为底，用点阵纹理和高饱和度色块营造出轻松诙谐的潮流感。核心图形：视觉主体是一颗红色点阵纹理的草莓，搭配几何造型的绿色叶片；旁边是一颗红色圆点（似浆果）和一个粉色杯子，杯子上有蓝色星状装饰，细节充满童趣。文字玩梗：顶部是巨大的白色艺术字"Fruit"，周围环绕着"QWEN QWEN QWEN"；右上角黑色块里写着"我 没事"，粉色杯子旁标注"别榨我"；底部是黑色粗体谐音梗文字"莓有烦恼"（呼应草莓图案，谐音没有烦恼），并配有英文"I'M NOT JUST A FRUIT"。最底部加入很小的版权信息"POWERED BY QWEN IMAGE"、"2026 AIGC"。整体风格：通过波普点阵、几何色块和谐音梗文案，把水果主题玩出潮流感，既可爱又解压。` |
| **超现实产品摄影** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/423747ee-de7b-4177-8199-abf62111c39d.png) | `超现实高端产品摄影：一罐红色铝制"Qwen Soda"苏打水直立居中，沿中线剧烈纵向劈裂，撕裂金属边缘锋利参差，鲜艳粉色番石榴汁以动态冻结姿态向外迸射。整颗新鲜番石榴与绿色果皮粉色果肉的厚切片从罐内向上向外爆散，间以光亮绿叶，全部悬空凝固。罐身覆满细密冷凝水珠，高细节金属质地与真实反光。亮红番石榴液体飞溅成戏剧性弧线，水滴清晰定格。无缝暖红背景与台面，单色配色以红绿粉主导；戏剧性影棚布光，强烈正面主光加柔和补光，形成锐利高光、明确阴影与高对比。相机平直眼位、微距裁切，浅景深但聚焦罐身与水果，电影级真实感、商业广告品质、超细节、照片级真实、超锐利、高端饮品广告美学。` |
| **打工人情绪海报** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/0843a1cc-bdf1-4b39-9487-7eb66eeed6df.png) | `主打打工人自嘲情绪的趣味海报，风格诙谐且视觉冲击力强。背景与主色调：以高饱和度的亮绿色为底色，搭配做旧纹理，视觉醒目又带点复古质感。核心元素：主体是"马头 + 西装"的反差形象——棕褐色马头搭配黑色西装、白衬衫与领带，既保留"牛马（打工人）"的自嘲设定，又用正装强化职场身份的反差感；旁边还配有一罐黄包装的啤酒，呼应"发酒疯"的主题。文字设计：主文案"牛马也要放放风 偶尔发个酒疯，再上工"用夸张的黑白块状字体呈现，搭配英文标注（牛马=WORKER、放风=REST、酒疯=DRINK），强化梗的指向性。字体带有漫画式的线条装饰，进一步烘托搞怪氛围。左上方加入很小的版权信息"POWERED BY QWEN IMAGE"、"2026 AIGC"。` |
| **极简艺术海报** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/a5af66fd-a186-46a4-9071-4cfe3b1e6267.png) | `极简朦胧意识流美学，高级排版海报，雅致淡兰紫色艺术，模糊梦幻的抽象纹理，拉丝渐变效果，艺术概念风格，视觉柔和且充满缥缈大气感。画面右下角放主题字：主题字进行字体设计，极细宋体风格"兰影云梦"，文字进行错位穿插摆放，字体优雅细长，笔画尾部添加花体曲线，在文字间穿插，整体呈现东方诗意，探索非凡自然与微观世界的艺术化表达。画面上方小文案从左到右依次放"2026""Visual Concept by Qwen""February"，对称；下方左边文案突出时间数字"TIME——02.20/02.23"；画面中隐秘穿插极小字号英文文案："Visual Dream""Oriental Visual Concept""New Expression of Culture"，文字低饱和灰紫墨色。` |
| **山野露营海报** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/59c59301-9497-4756-8503-eb9f515fc28b.png) | `竖版海报设计，自然山野实景摄影背景：晨光微熹的夏日森林，前景为青翠柔软的开阔草地，中景是层叠葱郁的阔叶林与松林，远景为柔和轮廓的苍翠远山，天空呈浅青灰蓝渐变，几缕薄云透出暖光；整体光影通透，空气感强，使用等效全画幅 35mm 镜头（f/5.6，1/250s，ISO 200）拍摄，呈现真实细腻的自然肌理与丰富绿色层次。画面中央醒目排布巨型白色粗体文字"山野露营派对"，字体为定制手绘风无衬线体，笔画边缘带有有机颗粒质感——模拟苔藓附着、树皮皲裂与风化岩石纹理，字形厚重有力，与森林粗粝感和山势轮廓形成视觉共鸣。文字间隙自然穿插一条暖黄色（Pantone 124 C）蜿蜒线条，粗细微变，起于左上角、绕过文字右侧、延展至右下角，形态如林间土径、篝火余烬轨迹或悬垂串灯，具流动韵律与引导视线功能。文字正下方，该暖黄路径延伸为一条具透视感的林间小径，路径上分布 6 组高辨识度简笔插画人物（每组 2–3 人），均采用扁平化矢量风格但带微妙阴影与环境反光：①左起第一组：两人协作撑开墨绿色三角帐篷，帐篷顶飘动细绳；②第二组：一人蹲姿用打火石引燃堆叠松枝的篝火，火星微溅；③第三组：三人围坐原木矮凳，举陶杯相碰，杯口蒸腾热气；④第四组：一人盘坐弹奏原木色民谣吉他，音符符号轻盈浮升；⑤第五组：一人展开野餐垫，另一人正摆放西瓜切片与柠檬水壶；⑥第六组（靠右）：两人并肩仰望天空，指尖指向一颗初现的亮星。所有人物色彩鲜明饱和（主色：明黄、珊瑚橙、钴蓝、草绿），服饰细节清晰（帆布背包、登山靴、草编帽、格子衬衫），比例约 1:15 于路径宽度，与实景背景形成"摄影 + 插画"双重视觉维度。色彩系统以大地色系（橄榄褐、沙岩米、松针深绿）为基底，叠加夜空深靛蓝（#1a237e）作顶部留白区衬托，暖黄路径与帐篷灯、篝火光晕、杯中液体反光共同构成温暖焦点；所有光源方向统一为左上方 45°柔光，强化体积感与沉浸氛围。左上角以橙色（Pantone 158 C）无衬线字体垂直排列活动时间信息："07.15 START"（字号稍大，加粗）与"CLOSE 09.20"（字号稍大，加粗），字距紧凑，背景微透明浅灰圆角矩形衬底提升可读性。底部居中排布两行文案：上方中文"星空为幕，山林为家"，下方英文"UNDER THE STARS, HOME IN THE WILD"，均采用细衬线字体（如 Playfair Display），字号适中，字间距宽松，色调为深炭灰（#2e2e2e）；文案右侧配一枚精致线性图标：简约单线勾勒的圆顶帐篷（线条粗细 1.2pt），顶部悬浮三颗不规则五角星（大小错落，最小星直径≈帐篷高度 1/3），星与帐篷呈 45°倾斜构图，整体以暖金（#d4af37）单色呈现。海报底部边缘添加一行极细小字（字号 6pt，浅灰#7a7a7a）："©2026 山野共生计划｜官网：qwenshanyewild.com｜#山野派对"，左下角椭圆形品牌标识：横向椭圆（长轴宽 8% 画幅，高轴高 4% 画幅），纯白底，内嵌衬线字体"qwenimage"，字母间距微调，字体颜色为深森林绿（#1b5e20），无描边无阴影。整体风格统一融合——摄影背景提供真实空间锚点，插画人物注入叙事活力，动态线条构建节奏呼吸，文字即图形、图形即信息，达成自然感、年轻感与传播力的三重平衡。` |
| **产品宣传图** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/c6b3fa65-f50a-4afe-b761-a6df950d511a.png) | `这是一张融合东方美学与未来感的香氛宣传图，主体是"QWEN"品牌香氛：透明圆柱形玻璃瓶身（内装深暖棕液体），印黑色"50ml"标识，搭配亮面正红球形瓶盖；香氛被放置在悬浮的弯曲花叶带有红 / 黄绒球、深棕浆果，花叶等艺术红色元素上。场景设定为轻奢艺术展示空间，背景是暖棕红渐变圆形色块（从深棕过渡到浅棕），外围是浅米白墙面，无多余装饰，营造出兼具东方雅致与未来科技感的氛围。风格参考"复古 AIGC 视觉风"，以精致的材质质感结合东方符号元素，呈现高级且先锋的新年限定宣传调性。色调以暖棕系为核心：瓶身液体是柔和暖棕，瓶盖是高饱和亮面正红（光泽饱满浓郁，表面有清晰圆润的高光）；整体色调温暖浓郁，红棕碰撞既显新年氛围，又通过暖调基底平衡了科技感的冷硬。光影采用侧方定向暖柔光：采用平视略仰视视角，强化香氛的精致感与装置的艺术感。` |
| **产品概念图** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/0d172a98-a421-4a41-ba97-ee0b979634e3.png) | `以茂密森林的外轮廓形成伏特加酒瓶轮廓的负空间，内部展现森林景观（溪流、岩石、湖泊、远处山林）；画面风格是超现实合成的写实摄影风，风格参考自然酒类广告设计；场景设定为繁茂的绿色森林，光线从酒瓶轮廓顶部洒入，营造通透感；构图视角为平视角度，采用中心对称构图；画面排版是品牌信息（"Qwen"字样、驼鹿标志）置于酒瓶轮廓中心，底部有 宣传 标语；细节补充包括森林植被的丰富层次（不同种类的树木、灌木、蕨类）、溪流的动态质感、光线的明暗对比（轮廓外的深绿与轮廓内的明亮绿意），整体呈现自然与产品融合的超现实广告风格。` |
| **名画构图** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/132b3539-3d7e-4619-a1f6-3b2058abb29d.png) | `米开朗基罗名画"创造亚当"构图，左侧哈士奇向左横躺屈曲左腿并伸出左臂躺在地上，食指伸出，右侧狸花猫趴在云上伸出食指与亚当相触，大师构图，杰作，丰富颜色及细节，米开朗基罗风格，它们手指接触的中间有发散性强烈光芒。` |
| **文创宣传海报** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/32898835-4131-4351-a5f5-9328685bd3b4.png) | `生成一张新中式国潮风城市文创宣传海报，画面主体为河北地标古建筑（钟楼 / 鼓楼），建筑以深棕、灰紫为主色调，墙面带有细腻的颗粒磨砂质感，屋檐与门窗点缀青绿色、橙黄色线条，建筑底部环绕着青绿色、鹅黄色的抽象祥云纹样，位于画面中下部。背景是层叠的渐变蓝紫色抽象山水云海，带有均匀的网点颗粒肌理，呈现出从浅蓝到藏蓝的色彩层次；画面左侧中上部是一轮巨大的暖黄色圆形落日，散发柔和光晕；画面右上方，一只白色仙鹤展翅飞翔，翅膀点缀黑色羽毛，仙鹤旁有青绿色飘带与浅蓝色气球状元素。 画面风格为国潮插画与新中式平面设计融合，整体调性大气、典雅且富有地域文化底蕴；视角为平视偏仰视的装饰性视角，采用非写实的平面化构图，建筑作为视觉核心，落日与仙鹤形成对角平衡；整体配色以高饱和的藏蓝、紫蓝为主色调，搭配暖黄落日、青绿祥云、白黑仙鹤，冷暖对比强烈且色彩浓郁；材质质感方面，背景为网点颗粒肌理的渐变质感，建筑为磨砂颗粒的厚重质感，祥云与飘带为平滑的平涂质感；专业渲染参数：8K 超高清分辨率，矢量插画结合数字肌理技法，网点纹理叠加，全局色彩统一协调，画面线条流畅、肌理细腻，传递出河北地域文化与文创美学结合的核心意境。 超清晰左上角有极细无衬线字体"HUBEI"，右上角有极细无衬线字体"Powered by Qwen"。` |

---

### 人像肖像摄影

> **场景描述**：生成真实质感的人像图片，包括时尚写真、职业照、艺术照等。
>
> **适用场景**：时尚写真、职业形象照、艺术创作、角色设计参考
>
> **Prompt 要素**：
>
> 人物特征：年龄、性别、发型、服装等
> 
> 拍摄风格：肖像、全身、特写等
> 
> 光线背景：光线与背景、情绪与姿态

| **场景** | **效果** | **Prompt** |
| --- | --- | --- |
| **王家卫风格人像** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/4555c18c-2f2a-4a23-a5b3-3e6a73469460.png) | `人像摄影，王家卫电影风格，地铁站，运动模糊，模糊曝光，动态模糊，情绪氛围感，胶片柔光，复古颗粒感，慢快门，简约高级感大片，荒木经纬风格人像摄影，kodak Ektachrome64 胶卷，颓废治愈氛围，自然静谧气息，斑驳梦幻光影，呼吸感，梦核，流光溢彩，极致光影美学，中西艺术融合，独特胶片颗粒感，非常规构图，诗意，白橙点缀，暗黑系，夜色，动态模糊，虚焦，高对比高饱和色彩叙事，褪色记忆，遥远的她，放浪形骸，情绪拉扯。` |
| **90 年代胶片感人像** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/12ae6900-b02c-4c05-bfb4-8c198af9ae59.png) | `Create a portrait of a beautiful young woman with porcelain-white skin, captured with a 1990s-style camera using a direct front flash. Her messy dark brown hair is tied up, posing with a calm yet playful smile. She wears a modern oversized cream sweater. The background is a dark white wall covered with aesthetic magazine posters and stickers, evoking a cozy bedroom or personal room atmosphere under dim lighting. The 35mm lens flash creates a nostalgic glow.` |
| **写实人像** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/1d726af0-78a2-4ba5-800b-188e70de4cb2.png) | `Generate a hyperrealistic realistic-anime portrait of a female character standing in a completely black background. Lighting: use a narrow beam spotlight focused only on the center of the face. The edges of the light must be sharp and dramatic. All areas outside the spotlight should fall quickly into deep darkness (high falloff shadow), almost blending into the black background. Not soft lighting.Hair: long dark hair with some strands falling over the face. The lower parts of the hair should fade into the shadows.Pose: one hand raised gently to the lips in a shy, hesitant gesture. Eyes looking directly at the camera with a mysterious mood.Clothing: black long-sleeve knit sweater; the sweater and body should mostly disappear into the darkness with minimal detail.Overall tone: dark, moody, dramatic, mysterious. High-contrast only in the lit portion of the face. Everything outside the spotlight should be nearly invisible.` |

### 自然风景与动物

> **场景描述**：生成细腻的自然景观和动物图片，包括山水、天空、植物、野生动物、宠物等。
>
> **适用场景**：旅游宣传素材、背景壁纸、自然主题设计、环境概念图、野生动物摄影、宠物肖像
>
> **Prompt 要素**：
>
> 场景类型：山川、海洋、森林、草原等
> 
> 时间天气：时间与天气、季节特征
> 
> 色彩氛围：色彩氛围
> 
> 动物特征：动物种类、毛发纹理、姿态表情、栖息环境

| **场景** | **效果** | **Prompt** |
| --- | --- | --- |
| **挪威冬日雪景** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/71c7a5f3-5e95-4c52-9175-426d279f1304.png) | `远景，鸟瞰，挪威罗弗敦的冬日景象，画面中，一座红色的小木屋矗立在雪地中，木屋的红色在白雪的映衬下格外醒目，木屋表面有些许磨损的痕迹，更显岁月感。周围是一片洁白的雪地，雪地上还能看到一些干枯的植物。远处是广阔的海面，海面平静，呈现出淡淡的蓝色。再远处，是被白雪覆盖的连绵山脉，山脉巍峨壮观，与天空的淡紫色、蓝色等色调相融合，营造出一种静谧、纯净且壮阔的冬日氛围，仿佛整个世界都被冰雪所包裹，充满了自然的美感与宁静的气息。` |
| **狮子** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/05eb02e8-4372-4bbc-85c9-ba8919050e98.png) | `3d photorealistic photo, side profile of a lion on the Serengeti, extreme close-up, in the style of Frans Lanting, shot on a Canon EOS R3 with a 70-200mm lens, filling the entire screen, high-resolution` |
| **海边日落** | ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jod02rzlpz/img/4bf888a8-85d0-4fa5-a222-2ceffceb75ef.png) | `Generate a serene beach sunset scene. The sun is setting on the horizon, casting warm orange and pink colors across the sky. Gentle waves lap at the sandy shore. A few seagulls fly in the distance. Palm trees frame the left side of the image. Style: travel photography, warm color palette, peaceful atmosphere, high resolution.` |

---

## 💻 API 接入指南

> Qwen-Image-2.0 系列支持 HTTP 同步调用，一次请求即可获得结果，调用流程简单，推荐用于多数场景。
>
> 北京地域：`POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`
>
> 新加坡地域：`POST https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation`
>
> ⚠️ 本次 Qwen-Image-2.0 系列支持了 2K 分辨率高清生成，以下是一些常用比例的 2K 分辨率取值：
>
> 16:9：`2048*1152`
>
> 9:16：`1152*2048`
>
> 4:3：`2048*1536`
>
> 3:4：`1536*2048`
>
> 1:1：`2048*2048`
>
> ⚠️⚠️ 本次 Qwen-Image-2.0 系列将 [文生图](https://help.aliyun.com/zh/model-studio/qwen-image-api?scm=20140722.H_2975126._.OR_help-T_cn~zh-V_1&userCode=okjhlpr5) 和 [图像编辑](https://help.aliyun.com/zh/model-studio/qwen-image-edit-api#05ad58a0dd5kd) 两种模式合二为一，调用一个模型即可适配不同的使用场景

```powershell
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $DASHSCOPE_API_KEY" \
--data '{
    "model": "qwen-image-2.0-pro",
    "input": {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": "手帐风上海旅行插画，分四天场景呈现：第一天外滩和南京路步行街（画外滩建筑群剪影、南京路百年商铺、街头小笼包摊位）；第二天豫园和城隍庙（画豫园九曲桥、湖心亭、城隍庙老街小吃）；第三天浦东陆家嘴和滨江（画东方明珠、上海中心、黄浦江游船）；第四天武康路和田子坊（画武康大楼、文艺咖啡馆、石库门小店）。每个场景角落有手写日期标注（如"Day1 外滩寻味"）。搭配云朵、太阳、行李箱、小飞机、梧桐叶等装饰元素，风格可爱温馨，线条柔和，色彩明快。"
                    }
                ]
            }
        ]
    },
    "parameters": {
        "negative_prompt": "构图混乱。文字模糊，扭曲。",
        "prompt_extend": true,
        "watermark": false,
        "size": "1152*2048"
    }
}'
```

```powershell
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $DASHSCOPE_API_KEY" \
--data '{
    "model": "qwen-image-2.0-pro",
    "input": {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "image": "image 链接"
                    },
                    {
                        "text": "讲解 Transformer 的历史与故事，为这个知识点做有趣的九宫格科普漫画（自由分布），二次元漫画风格，由图片一中的卡通人物进行讲解。"
                    }
                ]
            }
        ]
    },
    "parameters": {
        "n": 1,
        "negative_prompt": " ",
        "prompt_extend": true,
        "watermark": false,
        "size": "1152*2048"
    }
}'
```

---

## 💰 模型规格与定价

| **模型版本** | **定位** | **核心能力** | **价格** | **免费额度** |
| --- | --- | --- | --- | --- |
| [**Qwen-Image-2.0**](https://bailian.console.aliyun.com/cn-beijing?source_channel=K7mP9wR2vA&tab=model#/model-market/detail/qwen-image-2.0) | 加速版 | 图片生成 + 编辑融合、专业文字渲染（1k token 指令支持）、真实质感、强语义遵循，实现效果与性能的最佳平衡 | 0.2 元/张 | 100 张 |
| [**Qwen-Image-2.0-Pro**](https://bailian.console.aliyun.com/cn-beijing?source_channel=K7mP9wR2vA&tab=model#/model-market/detail/qwen-image-2.0-pro) | 满血版 | 图片生成 + 编辑融合、专业文字渲染（1k token 指令支持）、真实质感、强语义遵循，具备 2.0 系列最强的文字渲染能力和真实质感 | 0.5 元/张 | 100 张 |
