import requests
from collections import Counter
from konlpy.tag import Okt
import pandas as pd
from datetime import datetime, timedelta

class KeywordAnalyzer:
    def __init__(self):
        self.okt = Okt()
        self.naver_trending = []
        self.google_trends = []
        
    def get_naver_trending(self):
        """네이버 실시간 검색어 수집"""
        # 네이버 API 사용 (실제 구현시 네이버 검색 API 키 필요)
        pass
        
    def get_google_trends(self):
        """구글 트렌드 데이터 수집"""
        # pytrends 라이브러리 사용 (실제 구현시 Google Trends API 필요)
        pass
        
    def analyze_title_engagement(self, title):
        """제목 매력도 분석"""
        score = 0
        
        # 1. 길이 체크 (15-25자 사이가 최적)
        if 15 <= len(title) <= 25:
            score += 10
            
        # 2. 감정적 키워드 포함 여부
        emotional_keywords = ['놀라운', '충격', '최고의', '필수', '꿀팁']
        for keyword in emotional_keywords:
            if keyword in title:
                score += 5
                
        # 3. 숫자 포함 여부 (예: "5가지", "10개")
        if any(char.isdigit() for char in title):
            score += 5
            
        # 4. 시의성 체크
        current_trends = self.naver_trending + self.google_trends
        if any(trend in title for trend in current_trends):
            score += 15
            
        return score
    
    def suggest_keywords(self, topic):
        """주제에 맞는 키워드 제안"""
        base_keywords = self.okt.nouns(topic)
        suggested_titles = []
        
        templates = [
            "{}에 대한 모든 것",
            "{} 완벽 가이드",
            "당신이 몰랐던 {} 꿀팁",
            "전문가가 알려주는 {} 비법",
            "{} 실패하지 않는 방법"
        ]
        
        for keyword in base_keywords:
            for template in templates:
                title = template.format(keyword)
                score = self.analyze_title_engagement(title)
                suggested_titles.append({
                    'title': title,
                    'score': score
                })
                
        return sorted(suggested_titles, key=lambda x: x['score'], reverse=True)

# 사용 예시
analyzer = KeywordAnalyzer()
results = analyzer.suggest_keywords("다이어트 운동 방법")
for result in results[:5]:
    print(f"제목: {result['title']} (점수: {result['score']})")
