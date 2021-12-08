# Türkçe
Udp (Universel Document Page) türkçesiyle evrensel döküman sayfası basit bir şekilde dökümanlar hazırlamak ve görüntülemek için yaratılmıştır.Döküman oluşturmak için json gereklidir

Merhaba Dünya Örneği
```json
{
  "title": "Merhaba Dünya",
  "content": {
       "text": "Merhaba Dünya!",
       "align": "top"
  }
}
```

# English
Udp (Universal Document Page) has been created to prepare and view documents in a simple way. Json is required to create documents.

Hello World Example
```json
{
  "title": "Hello World",
  "content": {
       "text": "Hello World!",
       "align": "top"
  }
}
```

# View Output / Çıktıyı Görüntüleme

```
console>python udp.py run example.udp 
```
