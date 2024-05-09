# Olumlu anahtar kelimeler listesi
olumlu_kelimeler = ["iyi","harika","ederim","güzel","sağlam","hızlı","teşekkürler","ilgili","şık","rahat","kullanışlı","memnun","inanılmaz","süper","şahane","rahat","kalıcı","sevdim","beğendim","başarılı","hoş","kaliteli","performans"]

# Olumsuz anahtar kelimeler listesi
olumsuz_kelimeler = ["kötü","başarısız","kalitesiz","iade","hatalı","beğenmedim","sorunlu","problemli","kırık","arızalı","eksik","kusurlu","değilim","arıza","arızalı","ilgilenmiyor","ilgisiz","bozuk","bozuldu","almayın","aldırmayın","dandik","düşük","ölü"]

# Boş bir sözlük oluştur
kelime_sayilari_olumlu = {kelime: 0 for kelime in olumlu_kelimeler}
kelime_sayilari_olumsuz = {kelime: 0 for kelime in olumsuz_kelimeler}

# CSV dosyasını oku ve her satırdaki kelimelerin frekansını say
with open("C:\\Users\\SERHAT\\Desktop\\AgProje\\comments.csv", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        for kelime in satir.lower().split():
            if kelime in olumlu_kelimeler:
                kelime_sayilari_olumlu[kelime] += 1
            elif kelime in olumsuz_kelimeler:
                kelime_sayilari_olumsuz[kelime] += 1

# Anahtar kelimelerin frekanslarını görüntüle
print("Olumlu kelimeler:")
print(kelime_sayilari_olumlu)
print("\nOlumsuz kelimeler:")
print(kelime_sayilari_olumsuz)
