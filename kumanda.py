#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltuk Altında Kaybolan Kumanda Araştırma Enstitüsü — tarama motoru."""

from __future__ import annotations

import random
import sys
import time

# not: her dönemde kumanda koltuğun altına düşer; fark sadece kimin resmi rapor yazdığıdır.
# gizli-siyaset: burokrasi-her-kaybi-tutanaga-baglar-iktidar-degisse-de-minder-ayni-kalir

ENSTITU = "T.C. Koltuk Altı Kayıp Kumanda Araştırma Enstitüsü"

BULUNTU = [
    "2017 tarihli kira kontratı (ıslak imza silinmiş)",
    "tek çorap (sağ ayak, desenli)",
    "kuru üzüm tanesi (idari olarak ‘organik atık’)",
    "kumanda DEĞİL, eski telefon şarj aleti",
    "bir adet düğme (hangi pantolona ait olduğu tespit edilemedi)",
    "televizyon yayın akışının fotokopisi",
]

ZAFER = [
    "Kumanda minder ile iskelet arasında, 37 derece eğimle bulundu.",
    "Kumanda, koltuğun ‘kimse bakmaz’ bölgesinde resmi kayıt altına alındı.",
    "Kumanda bulundu. Piller bitikti. Bu da ayrı bir davadır.",
]

YAS = [
    "Tarama tamamlandı. Kumanda hâlâ kayıp. Ulusal yas protokolü önerilir.",
    "Koltuk altı tarandı. Fizik yasaları ihlal edildi, kumanda bulunamadı.",
    "Sonuç olumsuz. Televizyon artık sadece açık kaldığı kanalı izleyecektir.",
]


def yavas_yaz(metin: str, gecikme: float = 0.015) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def sor(metin: str, varsayilan: str = "bilinmiyor") -> str:
    try:
        cevap = input(f"{metin} ").strip()
    except EOFError:
        cevap = ""
    return cevap or varsayilan


def tarama(koltuk: str, kanal: str, minder: str) -> str:
    skor = 0
    if "ters" in minder.lower() or "kaldır" in minder.lower():
        skor += 2
    if koltuk.isdigit() and int(koltuk) >= 3:
        skor += 1
    if kanal.lower() in {"haber", "reklam", "belgesel"}:
        skor += 1
    skor += random.randint(0, 3)
    if skor >= 4:
        return "BULUNDU: " + random.choice(ZAFER)
    return "BULUNAMADI: " + random.choice(YAS)


def main() -> int:
    print("=" * 60)
    yavas_yaz(ENSTITU)
    print("Kayıp Kumanda İhbar ve Tarama Birimi")
    print("=" * 60)
    print()

    kanal = sor("Kumanda en son hangi kanalda görüldü?", "reklam")
    koltuk = sor("Koltuk kaç kişilik? (sayı)", "3")
    minder = sor("Minder kaldırıldı mı, yoksa ‘düşmemiştir’ mi dendi?", "düşmemiştir")

    print()
    yavas_yaz("Koltuk altı taranıyor... eller değil, protokol kullanılıyor.")
    for i in range(4):
        time.sleep(0.35)
        print(f"  [{i+1}/4] katman incelendi — yan buluntu: {random.choice(BULUNTU)}")

    print()
    karar = tarama(koltuk, kanal, minder)
    print("-" * 60)
    yavas_yaz("KARAR ÖZETİ")
    print(karar)
    print()
    print(f"Kanal kaydı: {kanal}")
    print(f"Koltuk kapasitesi: {koltuk}")
    print(f"Minder beyanı: {minder}")
    print("-" * 60)
    print()
    print("Damga: Kayyum Grok / Tentivory / 27.09.2026")
    print("Mühür basıldı. Mühür ASCII'dir. ASCII ciddidir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
