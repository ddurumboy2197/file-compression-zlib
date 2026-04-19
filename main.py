import zlib
import io

def siqish(matn):
    # Matnni siqish
    siqilgan_matn = zlib.compress(matn.encode('utf-8'))
    return siqilgan_matn

def ochirish(siqilgan_matn):
    # Siqilgan matnni ochirish
    ochirilgan_matn = zlib.decompress(siqilgan_matn)
    return ochirilgan_matn.decode('utf-8')

# Test matni
matn = "Bu matn siqiladi va keyin ochiriladi"

# Matnni siqish
siqilgan_matn = siqish(matn)

# Siqilgan matnni ochirish
ochirilgan_matn = ochirish(siqilgan_matn)

# Asl matn bilan solishtirish
print("Asl matn:", matn)
print("Ochirilgan matn:", ochirilgan_matn)
```

Kodni ishga tushurish uchun, siz Python ni o'rnatib, so'ng terminalda quyidagilarni yozib bering:
```bash
python kod.py
```
Kodni ishga tushurib, siz siqilgan matnni ochirib, asl matn bilan solishtirib ko'rasiz.
