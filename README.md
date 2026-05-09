<div align="center">

# 🌐 astrbot_plugin_web_reader

_✨ 一个赋予 AstrBot 大模型智能搜索与深度阅读网页能力的插件 ✨_

[![AstrBot](https://img.shields.io/badge/AstrBot-v4.0.0+-blue.svg)](https://github.com/AstrBotDevs/AstrBot)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

</div>

## 💡 简介

`astrbot_plugin_web_reader` 是为 AstrBot 开发的网页检索与阅读插件。
它通过注册 LLM 函数工具（Tools），让大语言模型（LLM）不仅能在网上搜索实时信息，还能**像人类一样点击进入特定网页，提取并阅读详细的纯文本内容**。

### ✨ 特性
- 🔍 **开箱即用，免 API Key**：内置 `duckduckgo-search`，直接白嫖高质量的搜索引擎，无需配置复杂的 API 密钥。
- 📄 **深度网页清理与阅读**：自动抓取指定 URL，并使用 `BeautifulSoup` 剔除无关的脚本、样式、导航栏及广告，提取纯净的正文文本供大模型阅读。
- 🤖 **全自动智能规划**：大模型会根据你的问题，**自主决定**先调用搜索工具查阅概览，再调用阅读工具进入具体链接深入了解，最后为你输出精准总结。

## 🛠️ 工具列表 (Tools)

大模型在需要时会自动调用以下工具：
1. `web_search(query: str)`: 向 DuckDuckGo 提交搜索词，返回最新的 5 条带有链接和摘要的搜索结果。
2. `web_fetch(url: str)`: 访问特定的 URL 链接，抓取网页内容并转换为大模型易于理解的纯文本。

## 📦 安装指南

1. **进入 AstrBot 的插件目录**：
   ```bash
   cd AstrBot/data/plugins/
   ```

2. **创建插件目录并放入文件**：
   你可以通过 Git Clone 或者手动新建 `astrbot_plugin_web_reader` 文件夹，并将 `main.py`、`metadata.yaml` 和 `requirements.txt` 放入其中。

3. **安装依赖库**：
   在插件目录下（或在你的 AstrBot 虚拟环境中）执行以下命令：
   ```bash
   pip install -r requirements.txt
   ```

4. **重启 AstrBot**：
   重启你的 AstrBot 以加载新插件。在管理面板或控制台日志中看到插件成功加载即可。

## 🚀 使用示例

在任意受支持的聊天平台中，您可以直接像平常一样和机器人对话。

**示例 1：热点新闻总结**
> **用户**：帮我搜索一下今天关于“人工智能”的最新新闻，选一篇最详细的文章点进去，把核心内容总结给我。
> 
> **机器人的自动处理流程**：
> 1. 调用 `web_search("人工智能 最新新闻")`
> 2. 拿到搜索列表，挑选出一个合适的新闻 URL
> 3. 调用 `web_fetch("https://xxx.com/news/123")`
> 4. 阅读长文本并返回精华总结

**示例 2：查阅文档或百科**
> **用户**：什么是“黑神话悟空”？去查一下它的维基百科或者官网，告诉我它的发售日期和主要玩法。

## ⚙️ 依赖清单

本插件依赖以下第三方库（见 `requirements.txt`）：
- `duckduckgo-search>=6.0.0`
- `httpx>=0.27.0`
- `beautifulsoup4>=4.12.0`

## 📝 许可证

本项目基于[MIT License](LICENSE) 开源，欢迎提交 Issue 或 Pull Request！
