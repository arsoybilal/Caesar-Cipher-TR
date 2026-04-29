# Türkçe Sezar Şifreleme Algoritması (Python)

Bu proje, kriptografinin temel taşlarından biri olan **Sezar Şifreleme (Caesar Cipher)** algoritmasının Python ile gerçekleştirilmiş, Türkçe karakter desteğiyle yerelleştirilmiş bir versiyonudur. Siber güvenliğe giriş seviyesinde veri gizliliği ve algoritma mantığını anlamak amacıyla geliştirilmiştir.

## 🚀 Özellikler

- **Türkçe Karakter Desteği:** Standart İngiliz alfabesi yerine 29 harfli Türk alfabesi (ç, ğ, ı, ö, ş, ü dahil) kullanılmıştır.
- **Dinamik Modülo Aritmetiği:** Kaydırma miktarı ne kadar büyük olursa olsun, alfabe uzunluğuna göre (mod 29) otomatik hesaplanır.
- **Çift Yönlü İşlem:** Hem şifreleme hem de şifre çözme (decryption) işlemlerini destekler.
- **Kullanıcı Dostu Arayüz:** Sürekli döngü sayesinde program kapanmadan üst üste işlemler yapılabilir.

## 🛠️ Nasıl Çalışır?

Sezar şifrelemesi, bir metindeki her harfin alfabede belirli bir sayı kadar kaydırılması esasına dayanır. 

**Matematiksel Formül:**
- Şifreleme: $E_n(x) = (x + n) \mod 29$
- Şifre Çözme: $D_n(x) = (x - n) \mod 29$

*(Burada 'x' harfin sırasını, 'n' ise kaydırma miktarını temsil eder.)*



## 📋 Kurulum ve Çalıştırma

1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/arsoybilal/Caesar-Cipher-TR.git
2. Proje dizinine gidin:
   ```bash
   cd proje-adiniz
2. Uygulamayı çalıştırın:
   ```bash
   python main.py 

## ⚠️ Siber Güvenlik Notu
Sezar şifrelemesi günümüz modern sistemleri için güvenli değildir. Sadece 29 olasılık (anahtar) bulunduğu için Kaba Kuvvet Saldırısı (Brute Force) ile saniyeler içinde kırılabilir. Bu proje tamamen eğitim amaçlıdır ve kriptografinin tarihsel gelişimini anlamak için tasarlanmıştır.

👤 Geliştirici
Bilal Arsoy

LinkedIn: linkedin.com/in/bilalarsoy

GitHub: github.com/arsoybilal
