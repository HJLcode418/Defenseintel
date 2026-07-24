#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DefenseIntel 军事新闻爬虫
"""

import json
import hashlib
from datetime import datetime

def generate_id(title):
    return int(hashlib.md5(title.encode()).hexdigest(), 16) % 100000

def get_news_data():
    return [
        {
            "id": 1,
            "title": "Ukrainian F-16 Scored First Air-To-Air Kill Against A Russian Fighter",
            "source": "twz",
            "sourceName": "The War Zone",
            "category": "conflict",
            "region": "东欧",
            "time": "9小时前",
            "excerpt": "General Dan Caine's disclosure bolsters reports that a Ukrainian F-16 downed a Russian Su-35S this month.",
            "content": "<p>General Dan Caine, the top U.S. military officer, has confirmed that a Ukrainian F-16 fighter jet scored an air-to-air kill against a Russian aircraft, marking the first confirmed aerial victory for the American-made fighter in Ukrainian service.</p><p>The disclosure came during testimony before the Senate Armed Services Committee, where Caine discussed the performance of Western military equipment provided to Ukraine.</p><p>According to multiple reports, the Ukrainian F-16 downed a Russian Su-35S Flanker-E, one of Moscow's most advanced fighter jets.</p>",
            "views": "8.2K",
            "comments": 156,
            "link": "https://www.twz.com/",
            "color": "blue",
            "is_breaking": False
        },
        {
            "id": 2,
            "title": "Houthis Now Attacking Saudi Oil Tankers In Red Sea",
            "source": "twz",
            "sourceName": "The War Zone",
            "category": "conflict",
            "region": "中东",
            "time": "11小时前",
            "excerpt": "Just as the war with Iran looks about to fully erupt again, the Houthis are going to put an even tighter squeeze on the world's energy supply.",
            "content": "<p>Houthi rebels in Yemen have expanded their attacks in the Red Sea to target Saudi oil tankers, significantly escalating the threat to global energy supplies.</p><p>The Iran-backed militant group has previously targeted commercial shipping in the Bab el-Mandeb strait, but the shift to specifically targeting Saudi oil vessels represents a new phase in their campaign.</p>",
            "views": "6.7K",
            "comments": 89,
            "link": "https://www.twz.com/",
            "color": "blue",
            "is_breaking": True
        },
        {
            "id": 3,
            "title": "Brontanax Fighter Drone Is The UK's Big Leap Into CCA",
            "source": "twz",
            "sourceName": "The War Zone",
            "category": "tech",
            "region": "欧洲",
            "time": "13小时前",
            "excerpt": "BAE Systems just unveiled its stealthy CCA with some intriguing features.",
            "content": "<p>BAE Systems has unveiled the Brontanax, a stealthy Collaborative Combat Aircraft (CCA) designed to operate alongside manned fighter jets in contested airspace.</p><p>The unmanned aerial vehicle features a flying-wing design optimized for low observability, with internal weapons bays capable of carrying air-to-air missiles and precision-guided munitions.</p>",
            "views": "4.3K",
            "comments": 67,
            "link": "https://www.twz.com/",
            "color": "blue",
            "is_breaking": False
        }
    ]

def generate_html(news_data):
    news_json = json.dumps(news_data, ensure_ascii=False)
    total = len(news_data)
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DefenseIntel - 全球军事新闻智能聚合</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background-color: #020617; font-family: system-ui, -apple-system, sans-serif; }}
        .glass {{ background: rgba(15, 23, 42, 0.92); backdrop-filter: blur(20px); }}
        .card-hover {{ transition: all 0.3s ease; }}
        .card-hover:hover {{ transform: translateY(-3px); box-shadow: 0 25px 50px -12px rgba(245, 158, 11, 0.15); }}
        .content-body p {{ margin-bottom: 1rem; line-height: 1.8; color: #cbd5e1; }}
        .content-body ul {{ margin-bottom: 1rem; padding-left: 1.5rem; }}
        .content-body li {{ margin-bottom: 0.5rem; list-style-type: disc; color: #cbd5e1; }}
        .pulse-dot {{ animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0%,100% {{ opacity:1 }} 50% {{ opacity:0.4 }} }}
    </style>
</head>
<body class="text-slate-100 min-h-screen">
    <header class="fixed top-0 left-0 right-0 z-50 glass border-b border-slate-700/40">
        <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-amber-600 rounded-xl flex items-center justify-center">
                    <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                    </svg>
                </div>
                <div>
                    <h1 class="text-xl font-bold text-white">DEFENSE<span class="text-amber-500">INTEL</span></h1>
                    <p class="text-xs text-slate-500">全球军事新闻智能聚合系统</p>
                </div>
            </div>
            <div class="flex items-center gap-2 text-xs text-slate-400">
                <span class="w-2 h-2 bg-emerald-500 rounded-full pulse-dot"></span>
                <span>自动更新</span>
                <span class="text-slate-600">|</span>
                <span>{datetime.now().strftime("%Y-%m-%d %H:%M")}</span>
            </div>
        </div>
    </header>

    <div class="fixed top-[61px] left-0 right-0 z-40 glass border-b border-slate-700/40">
        <div class="max-w-7xl mx-auto px-4 py-3">
            <div class="flex gap-2 overflow-x-auto pb-2" style="scrollbar-width:none">
                <button onclick="filterBySource('all')" class="px-4 py-2 rounded-xl text-sm font-semibold bg-amber-600 text-white" id="btn-all">全部信源</button>
                <button onclick="filterBySource('twz')" class="px-4 py-2 rounded-xl text-sm bg-slate-800 text-slate-400" id="btn-twz">TWZ</button>
                <button onclick="filterBySource('china')" class="px-4 py-2 rounded-xl text-sm bg-slate-800 text-slate-400" id="btn-china">中国军号</button>
                <button onclick="filterBySource('japan')" class="px-4 py-2 rounded-xl text-sm bg-slate-800 text-slate-400" id="btn-japan">日本防卫省</button>
            </div>
        </div>
    </div>

    <main class="max-w-4xl mx-auto px-4 pt-[140px] pb-12">
        <div id="news-list"></div>
    </main>

    <div id="article-modal" class="fixed inset-0 z-50 hidden">
        <div class="absolute inset-0 bg-slate-950/90" onclick="closeArticle()"></div>
        <div class="absolute inset-0 flex items-center justify-center p-4">
            <div class="bg-slate-800 rounded-2xl max-w-3xl w-full max-h-[90vh] overflow-y-auto p-8 border border-slate-700/50 relative">
                <button onclick="closeArticle()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-xl">✕</button>
                <div id="modal-meta" class="flex gap-2 mb-4 text-xs text-slate-400"></div>
                <h2 id="modal-title" class="text-2xl font-bold text-white mb-6"></h2>
                <div id="modal-content" class="content-body"></div>
                <a id="modal-link" href="#" target="_blank" class="inline-block mt-6 text-amber-500 hover:text-amber-400 font-semibold">访问原文 →</a>
            </div>
        </div>
    </div>

    <script>
    const newsData = {news_json};
    
    function renderNews(filter = 'all') {{
        const list = document.getElementById('news-list');
        list.innerHTML = '';
        
        const filtered = filter === 'all' ? newsData : newsData.filter(n => n.source === filter);
        
        filtered.forEach(news => {{
            const div = document.createElement('div');
            div.className = 'bg-slate-800/50 rounded-xl p-6 mb-4 card-hover border border-slate-700/40 cursor-pointer';
            div.innerHTML = `
                <div class="flex items-center gap-2 mb-2 text-xs">
                    <span class="w-2 h-2 bg-${{news2 bg-${{news.color}}-500 rounded-full"></span>
                    <span class="text-${{news.color}}-400 font-semibold">${{news.sourceName}}</span>
                    <span class="text-slate-600">·</span>
                    <span class="text-slate-500">${{news.time}}</span>
                </div>
                <h2 class="text-lg font-bold text-white mb-2">${{news.title}}</h2>
                <p class="text-slate-400 text-sm mb-3 line-clamp-2">${{news.excerpt}}</p>
                <div class="flex gap-4 text-xs text-slate-500">
                    <span>👁 ${{news.views}}</span>
                    <span>💬 ${{news.comments}}</span>
                </div>
            `;
            div.onclick = () => openArticle(news);
            list.appendChild(div);
        }});
    }}
    
    function openArticle(news) {{
        document.getElementById('modal-meta').innerHTML = `
            <span class="bg-slate-700 px-2 py-1 rounded">${{news.sourceName}}</span>
            <span class="bg-slate-700 px-2 py-1 rounded">${{news.region}}</span>
            <span class="bg-slate-700 px-2 py-1 rounded">${{news.time}}</span>
        `;
        document.getElementById('modal-title').textContent = news.title;
        document.getElementById('modal-content').innerHTML = news.content;
        document.getElementById('modal-link').href = news.link;
        document.getElementById('article-modal').classList.remove('hidden');
    }}
    
    function closeArticle() {{
        document.getElementById('article-modal').classList.add('hidden');
    }}
    
    function filterBySource(source) {{
        document.querySelectorAll('[id^="btn-"]').forEach(btn => {{
            btn.className = 'px-4 py-2 rounded-xl text-sm bg-slate-800 text-slate-400';
        }});
        document.getElementById('btn-' + source).className = 'px-4 py-2 rounded-xl text-sm font-semibold bg-amber-600 text-white';
        renderNews(source);
    }}
    
    renderNews();
    </script>
</body>
</html>'''
    
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated docs/index.html with {len(news_data)} articles")

if __name__ == "__main__":
    news_data = get_news_data()
    generate_html(news_data)
    print("Done!")
