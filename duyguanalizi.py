#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:25:11 2024

@author: zehraoner
"""

import pandas as pd
import matplotlib.pyplot as plt

# Veri setini yükle
data = pd.read_csv("C:\\Users\\SERHAT\\Desktop\\AgProje\\input.csv")

# Duygu analizi için anahtar kelimeler
positive_keywords = ["iyi","harika","ederim","güzel","sağlam","hızlı","teşekkürler","ilgili","şık","rahat","kullanışlı","memnun","inanılmaz","süper","şahane","rahat","kalıcı","sevdim","beğendim","başarılı","hoş","kaliteli","performans"]
negative_keywords = ["kötü","başarısız","kalitesiz","iade","hatalı","beğenmedim","sorunlu","problemli","kırık","arızalı","eksik","kusurlu","değilim","arıza","arızalı","ilgilenmiyor","ilgisiz","bozuk","bozuldu","almayın","aldırmayın","dandik","düşük"] 

# Duygu analizi fonksiyonu
def analyze_sentiment(comment):
    positive_count = sum(comment.lower().count(keyword) for keyword in positive_keywords if isinstance(comment, str))
    negative_count = sum(comment.lower().count(keyword) for keyword in negative_keywords if isinstance(comment, str))
    
    if positive_count > negative_count:
        return 'Positive'
    elif positive_count < negative_count:
        return 'Negative'
    else:
        return 'Neutral'

# Yorumları işle
comments = data['comments']
sentiments = []

for comment in comments:
    sentiment = analyze_sentiment(comment)
    sentiments.append(sentiment)

# Sonuçları DataFrame'e ekle ve CSV dosyasına kaydet
data['sentiment'] = sentiments
data.to_csv('static/sentiment_analysis_result.csv', index=False)

sentiment_counts = data['sentiment'].value_counts()

# Grafik için verileri hazırla
labels = sentiment_counts.index
sizes = sentiment_counts.values
colors = ['lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0)  # Sadece pozitif duyguları vurgulamak için

# Pasta grafiği oluştur
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Daireyi daire olarak görüntülemek için
plt.title('Yorumların Duygu Dağılımı')

# Grafiği dosyaya kaydet
plt.savefig("static/duygu_dagilimi.png")


