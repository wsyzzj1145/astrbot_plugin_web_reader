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
