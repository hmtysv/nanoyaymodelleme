# Nanoyay Modelleme
Moleküler Simülasyon için Nanoyay oluşturma 
Program MD simülasyon programları için nanoyay oluşturuyor. Nanoyay tek atomdan oluşabilir ve  kor@kabuk (core-shell) yapılar oluşturabiliyor.
Üç farklı formatta çıktı veriyor; lmp (LAMMPS), [xml](https://www.microsoft.com/en-us/p/ball-stick/9nblggh4s694), xyz. Çıktı görüntülemek için [OVITO](https://www.ovito.org/)


Program şu kristal yapıları tanıyor.
- sc
- fcc
- bcc
-diamond

Yay oluşturmak için yay parametreleri (r,R,N,P)ve element ismi kristal lattice uzunluğu (a) ve tel yarıçapını input olarak alıyor.
[Nanoyay ](https://en.wikipedia.org/wiki/Spring_(mathematics))

# Görsel Arayüz

Arayüz kor@kabuk yapılara uygun olarak hazırlandı.Tek atomlu yay için arayüz ilk sütunu doldurmak yeterli.
Kor ve kabukların R,N,P parametreleri aynı olmalı


# Batch

Yaylar aynı zamanda toplu olarak üretilebilir. Batch klasöründeki csv uzanltılı dosyalardan birini seçmelisiniz. Not Defteri ile düzenlenebilir. Openoffice ve MS excel ile görüntülenebilir. 



