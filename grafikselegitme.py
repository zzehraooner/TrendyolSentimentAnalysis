    import pandas as pd
    import matplotlib.pyplot as plt

    # Veri setini yükle
    data = pd.read_csv("C:\\Users\\SERHAT\\Desktop\\AgProje\\sentiment_analysis_result.csv")

    # Duygu analizi sonuçlarını say
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
    plt.savefig("duygu_dagilimi.png")
    plt.show()
