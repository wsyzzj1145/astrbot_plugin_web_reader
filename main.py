import httpx
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

from astrbot.api.star import Context, Star
from astrbot.api import llm_tool, logger
from astrbot.api.event import AstrMessageEvent

class WebReaderPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @llm_tool(name="web_search")
    async def web_search(self, event: AstrMessageEvent, query: str) -> str:
        '''使用搜索引擎在互联网上搜索信息。当你需要最新信息、实时新闻或不知道答案时，请调用此工具。
        
        Args:
            query(string): 搜索关键词
        '''
        logger.info(f"[WebReader] 正在搜索关键词: {query}")
        try:
            results =[]
            # 使用 duckduckgo 搜索，免 API Key
            with DDGS() as ddgs:
                # 限制结果数量为 5 个，避免 token 爆炸
                for r in ddgs.text(query, max_results=5):
                    results.append(f"标题: {r.get('title')}\n链接: {r.get('href')}\n摘要: {r.get('body')}\n")
            
            if not results:
                return "未找到相关搜索结果。"
            
            # 在返回结果末尾暗示大模型可以进一步读取
            instruction = "搜索结果如上。如果你需要了解某个链接的具体内容，请使用 web_fetch 工具读取该链接。"
            return "搜索结果如下：\n\n" + "\n".join(results) + "\n" + instruction
            
        except Exception as e:
            logger.error(f"[WebReader] 搜索失败: {e}")
            return f"搜索发生错误: {e}"

    @llm_tool(name="web_fetch")
    async def web_fetch(self, event: AstrMessageEvent, url: str) -> str:
        '''获取指定网页的详细纯文本内容。结合 web_search 提供的链接使用，当你需要深入阅读某篇文章或网页详情时调用。
        
        Args:
            url(string): 网页的完整 URL 链接
        '''
        logger.info(f"[WebReader] 正在读取网页: {url}")
        try:
            # 使用异步 httpx 发起请求
            async with httpx.AsyncClient(verify=False, timeout=15.0, follow_redirects=True) as client:
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                
                # 解析 HTML
                soup = BeautifulSoup(response.text, "html.parser")
                
                # 移除无用的标签（脚本、样式、导航栏、页脚等），提高大模型阅读质量
                for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
                    tag.extract()
                    
                # 提取纯文本
                text = soup.get_text(separator='\n')
                
                # 清理多余的空白符和空行
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                clean_text = '\n'.join(chunk for chunk in chunks if chunk)
                
                # 限制返回的最大字符数（大约 6000 字），防止超出大模型的上下文窗口限制
                max_length = 6000
                if len(clean_text) > max_length:
                    clean_text = clean_text[:max_length] + "\n\n...（文章过长，已截断后面内容）"
                    
                return f"【网页抓取成功】URL: {url}\n\n内容如下：\n{clean_text}"
                
        except Exception as e:
            logger.error(f"[WebReader] 抓取网页失败: {e}")
            return f"无法读取该网页内容，可能该网站禁止抓取或需要验证。错误信息: {e}"