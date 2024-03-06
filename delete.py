import os
import time
from multiprocessing import Process

def silme_kontrol(dosya_adı):
    dosya_silme_listesi = ["main.py","delete.py","name.py",
    "runmovie.py","runmain.py","wsgimain.py",
    "wsgimovie.py","wsginame.py" ,"__pycache__"]
    return dosya_adı not in dosya_silme_listesi

def dosyalari_temizle(klasor_yolu):
    while True:
        try:
            for dosya in os.listdir(klasor_yolu):
                dosya_yolu = os.path.join(klasor_yolu, dosya)
                if os.path.isfile(dosya_yolu) and silme_kontrol(dosya):
                    os.remove(dosya_yolu)
                    print(f"{dosya} silindi.")
                elif os.path.isdir(dosya_yolu) and silme_kontrol(dosya):
                    os.rmdir(dosya_yolu)
                    print(f"{dosya} klasörü silindi.")
        except Exception as e:
            print(f"Hata oluştu: {str(e)}")

        time.sleep(1)  # Her 60 saniyede bir kontrol et

if __name__ == "__main__":
    klasor_yolu = "C:/Users/Dell/Desktop/youtube dowlander-bckd"

    # Çalışan süreç oluştur
    temizleme_sureci = Process(target=dosyalari_temizle, args=(klasor_yolu,))

    # Süreci başlat
    temizleme_sureci.start()

    try:
        # Programın sona ermemesi için ana sürecin beklemesi
        temizleme_sureci.join()
    except KeyboardInterrupt:
        # Kullanıcı Ctrl+C ile programı durdurma isterse süreci sonlandır
        temizleme_sureci.terminate()
