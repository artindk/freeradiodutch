# FreeRadio — NVDA Eklentisi

FreeRadio, ekran okuyucu NVDA için geliştirilmiş bir internet radyo eklentisidir. Temel amacı, kullanıcıların binlerce internet radyo istasyonuna kolayca erişebilmesini sağlamaktır. Tüm arayüz ve işlevler NVDA ile tam erişilebilirlik gözetilerek tasarlanmıştır.

## Radio Browser Dizini

FreeRadio, istasyon kataloğu için [Radio Browser](https://www.radio-browser.info/) açık veritabanını kullanır. Radio Browser; dünya genelinde 50.000'i aşkın internet radyo istasyonunu barındıran, topluluk tarafından yönetilen ücretsiz bir dizindir. Kayıt veya hesap gerektirmez ve API'si herkese açıktır. Her istasyon için adres, ülke, tür, dil ve bit hızı bilgileri mevcuttur; istasyonlar kullanıcı oylarıyla sıralanır. FreeRadio bu API'ye Almanya, Hollanda ve Avusturya'da bulunan yansı sunucuları üzerinden bağlanır; bir sunucuya ulaşılamazsa otomatik olarak bir sonrakine geçer.

## Gereksinimler

- NVDA 2024.1 veya üzeri
- Windows 10 veya üzeri
- İnternet bağlantısı

## Kurulum

`.nvda-addon` dosyasını indirin, üzerine Enter'a basın ve istendiğinde NVDA'yı yeniden başlatın.

## Klavye Kısayolları

NVDA Menüsü → Tercihler → Girdi Hareketleri → FreeRadio bölümünden yeniden atanabilir. Bu kısayollar, odak hangi pencerede olursa olsun her yerden çalışır.

| Kısayol | İşlev | Açıklama |
|---|---|---|
| `Ctrl+Win+R` | İstasyon tarayıcısını aç | Tarayıcı penceresi kapalıysa açar, açıksa öne getirir. |
| `Ctrl+Win+P` | Duraklat / devam et | Çalan istasyon varsa duraklatır; duraklatılmışsa devam ettirir. Hiç istasyon çalmıyorsa ayara göre son istasyonu başlatır veya favoriler listesini açar. İki kez basıldığında ayara göre farklı bir sekmeye doğrudan atlanır. Üç kez basıldığında ayara bağlı olarak ayrı bir işlem tetiklenebilir. |
| `Ctrl+Win+S` | Durdur | Çalan istasyonu tamamen durdurur ve oynatıcıyı sıfırlar. |
| `Ctrl+Win+→` | Sonraki favori | Favoriler listesindeki bir sonraki istasyona geçer. Liste sonuna gelindiğinde başa döner. |
| `Ctrl+Win+←` | Önceki favori | Favoriler listesindeki bir önceki istasyona geçer. Listenin başındayken sona atlar. |
| `Ctrl+Win+↑` | Ses artır | Ses seviyesini 10 birim artırır; azami 100. |
| `Ctrl+Win+↓` | Ses azalt | Ses seviyesini 10 birim düşürür; asgari 0. |
| `Ctrl+Win+V` | Favorilere ekle | O an çalan istasyonu favoriler listesine ekler. İstasyon zaten listedeyse bildirir. |
| `Ctrl+Win+İ` | İstasyon bilgisi | Çalan istasyonu seslendirir. İki kez basıldığında ülke, tür, bit hızı gibi ayrıntıları bir iletişim kutusunda gösterir. Üç kez basıldığında çalan parça bilgisi (ICY metadata) varsa panoya kopyalar; yoksa Shazam ile müzik tanıma başlatır. Dört kez basıldığında çalan parça bilgisi (ICY metadata) yanlışsa müzik tanıma servisini başlatmaya zorlar. |
| `Ctrl+Win+M` | Ses yansıtma | O an çalan akışı ek bir çıkış aygıtına yansıtır. Yansıtma zaten aktifse durdurur. |
| `Ctrl+Win+E` | Anlık kayıt | Bir kez basıldığında çalan istasyonu kaydetmeye başlar; tekrar basıldığında durdurur. **İki kez** basıldığında **şarkı kaydı** başlar — dosya o anki parça adıyla adlandırılır ve parça değiştiğinde kayıt otomatik olarak durur. Şarkı kaydı aktifken tekrar iki kez basılması kaydı erken sonlandırır. Oynatma tüm kayıt modlarında kesintisiz sürer. Yalnızca ICY metadata yayınlayan istasyonlarda kullanılabilir. |
| `Ctrl+Win+W` | Kayıt klasörünü aç | Kaydedilen dosyaların bulunduğu klasörü Dosya Gezgini'nde açar. |
| *(atanmamış)* | Bildirimleri sessize al / aç | Bildirim sessize alma ayarını anlık olarak değiştirir. NVDA Menüsü → Tercihler → Girdi Hareketleri → FreeRadio bölümünden bir tuş kombinasyonu atanabilir. |

Sonraki / önceki kısayollar yalnızca favoriler listesinde dolaşır; tüm istasyonlar listesinde çalışmaz. Tarayıcı penceresinde listeler odaklanmışken sol ve sağ ok tuşları da aynı işlevi görür: bkz. Diyalog İçi Kısayollar.

## İstasyon Tarayıcısı

FreeRadio ayrıca NVDA Araçlar menüsüne **FreeRadio** adlı bir alt menü ekler. Bu alt menüden İstasyon Tarayıcısı'nı ve FreeRadio Ayarları'nı doğrudan açabilirsiniz.

`Ctrl+Win+R` ile açılan pencerede beş sekme bulunur: Tüm İstasyonlar, Favoriler, Kayıt, Zamanlayıcı ve Beğenilen Şarkılar. Sekmeler arasında `Ctrl+Tab` ile dolaşılabilir.

Tüm İstasyonlar sekmesi açıldığında Radio Browser'dan en çok oylanan 1000 istasyon otomatik olarak yüklenir. Ülke açılır listesinden bir ülke seçildiğinde liste o ülkenin istasyonlarıyla güncellenir. Arama alanına harf girilmesi anlık olarak   Radio Browser'ın tamamında ad, ülke ve tür üzerinden eş zamanlı arama yapar.

Tarayıcı penceresinin alt kısmında sekmelerin dışında yer alan **Çıkış Cihazı** açılır listesi, o an BASS tarafından tanınan ses çıkış aygıtlarını listeler. Listeden bir aygıt seçildiğinde ses çıkışı anında o aygıta yönlendirilir ve seçim kalıcı olarak kaydedilir; bir sonraki oturumda aynı aygıt otomatik olarak kullanılır. Seçili aygıt sisteme bağlı değilse otomatik olarak sistem varsayılanına dönülür. Bu denetim yalnızca BASS arka ucu aktifken işlev görür.

Aynı bölümde yer alan **Ses Seviyesi** (0–200) ve **Efektler** denetim çubuğu, pencere açıkken anlık olarak ayarlanabilir. Efektler listesinden Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb ile EQ: Bass Boost, EQ: Treble Boost ve EQ: Vocal Boost seçenekleri aynı anda birden fazla seçilerek etkinleştirilebilir; değişiklikler çalan akışa anında uygulanır. Bu denetimler yalnızca BASS arka ucu aktifken tam işlev görür.

Pencerenin alt kısmında ayrıca **Çal/Duraklat** düğmesi bulunur. Herhangi bir istasyon çalmıyorsa seçili istasyonu başlatır; bir istasyon çalıyorsa oynatmayı duraklatır.

Listede bir istasyon seçiliyken **İstasyon Detayları** düğmesi, o istasyona ait ülke, dil, tür, format, bit hızı, web sitesi ve akış adresi gibi bilgileri ayrı bir iletişim kutusunda gösterir. İletişim kutusunda her alan ayrı bir salt-okunur metin kutusunda yer alır; Tab tuşuyla alanlar arasında gezinilebilir. **Tümünü panoya kopyala** düğmesiyle tüm bilgiler tek seferde panoya alınabilir. Bu düğme hem Tüm İstasyonlar hem de Favoriler sekmesinde bulunur.

### Diyalog İçi Kısayollar

Aşağıdaki tuşlar yalnızca İstasyon Tarayıcısı penceresi etkinken çalışır.

### F Tuşları

| Kısayol | İşlev | Açıklama |
|---|---|---|
| `F1` | Yardım kılavuzu | Eklentinin yardım dosyasını varsayılan tarayıcıda açar. Önce etkin NVDA diline ait kılavuz aranır; yoksa varsayılan kılavuz açılır. |
| `F2` | Ne çalıyor | Çalan istasyon adını ve varsa ICY metadata parça bilgisini seslendirir. |
| `F3` | Önceki istasyon | Tüm İstasyonlar veya Favoriler sekmesinde bir önceki istasyona geçer ve hemen çalmaya başlar. Listenin başındayken sona atlar. |
| `F4` | Sonraki istasyon | Tüm İstasyonlar veya Favoriler sekmesinde bir sonraki istasyona geçer ve hemen çalmaya başlar. Liste sonuna gelindiğinde başa döner. |
| `F5` | Ses azalt | Ses seviyesini 10 birim düşürür (asgari 0). |
| `F6` | Ses artır | Ses seviyesini 10 birim artırır (azami 200). |
| `F7` | Duraklat / devam et | Çalan istasyon varsa duraklatır; duraklatılmışsa ve medya yüklüyse oynatmayı sürdürür. |
| `F8` | Durdur | Çalan istasyonu tamamen durdurur ve oynatıcıyı sıfırlar. |
| `F9` | Yeniden adlandır | Favoriler sekmesinde odaklanan istasyonun yeniden adlandırılabilmesi için bir iletişim kutusu açar. |

### Liste ve Gezinme Kısayolları

| Kısayol | İşlev | Açıklama |
|---|---|---|
| `→` | Sonraki istasyon | Tüm İstasyonlar veya Favoriler listesi odaklanmışken bir sonraki istasyona geçer ve hemen çalar. Liste sonunda başa döner. |
| `←` | Önceki istasyon | Tüm İstasyonlar veya Favoriler listesi odaklanmışken bir önceki istasyona geçer ve hemen çalar. Listenin başındayken sona atlar. |
| `Enter` | Çal | Tüm İstasyonlar veya Favoriler listesi odaklanmışken seçili istasyonu doğrudan çalmaya başlar. Başka bir istasyon çalıyor olsa bile çalmayı keserek seçili istasyona geçer. |
| `Boşluk` | Çal / Duraklat | Çalan istasyon varsa duraklatır; yoksa listede seçili istasyonu çalmaya başlar. |
| `Ctrl+Tab` | Sonraki sekme | Bir sonraki sekmeye geçer (Tüm İstasyonlar → Favoriler → Kayıt → Zamanlayıcı → Beğenilen Şarkılar). |
| `Ctrl+Shift+Tab` | Önceki sekme | Bir önceki sekmeye döner. |
| `Escape` | Gizle | Pencereyi gizler; eklenti arka planda çalmaya devam eder. |

### Ses Kısayolları

| Kısayol | İşlev | Açıklama |
|---|---|---|
| `Ctrl+↑` | Ses artır | Ses seviyesini 10 birim artırır. Yalnızca tarayıcı penceresi açıkken çalışır. |
| `Ctrl+↓` | Ses azalt | Ses seviyesini 10 birim düşürür. Yalnızca tarayıcı penceresi açıkken çalışır. |

### Alt Kısayolları

| Kısayol | İşlev | Açıklama |
|---|---|---|
| `Alt+R` | Arama alanına git | Odağı arama metin kutusuna taşır. Yazıldıkça ad, ülke ve tür eş zamanlı aranır. |
| `Alt+V` | Favori ekle / kaldır | Seçili istasyonu favorilere ekler; zaten listedeyse kaldırır. |
| `Alt+1` | Tüm İstasyonlar | Tüm İstasyonlar sekmesine geçer. |
| `Alt+2` | Favoriler | Favoriler sekmesine geçer. |
| `Alt+3` | Kayıt | Kayıt sekmesine geçer. |
| `Alt+4` | Zamanlayıcı | Zamanlayıcı sekmesine geçer. |
| `Alt+5` | Beğenilen Şarkılar | Beğenilen Şarkılar sekmesine geçer. |
| `Alt+K` | Kapat | Pencereyi kapatır; eklenti arka planda çalmaya devam eder. |

## Favoriler

Favoriler listesi, kalıcı olarak saklanan kişisel bir istasyon koleksiyonudur. İstasyon eklemek için listeden istasyonu seçip Favorilere Ekle düğmesine basın ya da `Alt+V` kısayolunu kullanın. Seçili istasyon zaten listedeyse aynı kısayol istasyonu listeden kaldırır.

Favoriler `Ctrl+Win+→` ve `Ctrl+Win+←` ile çalınabilir; bu kısayollar tarayıcı penceresi açık olmasa da çalışır.

Favoriler listesinden bir istasyonu silmek için istasyonu seçip **İstasyonu Sil** düğmesine veya `Delete` tuşuna basın. Silme işleminin ardından odak ve seçim listedeki bir sonraki istasyona otomatik olarak taşınır. Silinen istasyon listedeki sonuncusuysa odak bir önceki istasyona geçer. Liste tamamen boşalırsa odak Çal düğmesine taşınır.

### Favorileri Yeniden Sıralama

Favoriler sekmesinde bir istasyon seçiliyken `*` tuşuna basarak taşıma moduna girin — bir bip sesi duyarsınız. Ok tuşlarıyla hedef konuma gidin, ardından `*` tuşuna tekrar basın. İstasyon seçilen konuma yerleştirilir ve yeni sıra anında kaydedilir. Aynı konumda tekrar `*` tuşuna basılması taşımayı iptal eder.

### Özel İstasyon Ekleme

Radio Browser'da bulunmayan bir istasyon eklemek için Özel İstasyon Ekle düğmesini kullanın. Açılan iletişim kutusuna istasyon adını ve akış adresini girerek istasyonu doğrudan favorilerinize ekleyebilirsiniz. Özel istasyonlar diğer favoriler gibi çalınabilir ve yeniden sıralanabilir.

### İstasyon Ses Profili

Favoriler sekmesinde per-istasyon ses ayarlarını yönetmek için iki düğme bulunur:

**Bu İstasyon İçin Ses Profili Kaydet** — mevcut ses seviyesini ve aktif efektleri (chorus, EQ vb.) o istasyona özgü bir profil olarak kaydeder. Bu istasyon her çalmaya başladığında kaydedilmiş ses seviyesi ve efektler otomatik olarak uygulanır; global varsayılanların yerine geçer.

**Ses Profilini Temizle** — seçili istasyondaki kayıtlı ses profilini kaldırır. Temizlendikten sonra istasyon global ses seviyesi ve efekt ayarlarına geri döner. Bu düğme yalnızca seçili istasyonda kayıtlı bir profil bulunduğunda etkinleşir.

Her iki düğme de favoriler listesinin altında yer alır ve yalnızca listeden bir istasyon seçiliyken etkin olur.

## Müzik Tanıma

`Ctrl+Win+İ` kısayoluna üç kez basıldığında çalan akış için Shazam tabanlı müzik tanıma başlar. Tanıma yalnızca ICY metadata (istasyon tarafından yayınlanan parça bilgisi) mevcut olmadığında başlar; metadata varsa bunun yerine panoya kopyalanır.

Tanıma şu şekilde çalışır: ffmpeg kullanılarak akıştan kısa bir ses örneği alınır, Shazam parmak izi algoritması uygulanır ve sonuç Shazam sunucularına gönderilir. Tanıma başarılı olursa parça adı, sanatçı, albüm ve yayın yılı NVDA tarafından seslendirilir ve otomatik olarak panoya kopyalanır. **Beğenilen şarkıları metin dosyasına kaydet** seçeneği açıksa tanıma sonucu `likedSongs.txt` dosyasına da eklenir.

**Sesli geri bildirim:** Tanıma başladığında iki yükselen bip, bittiğinde iki alçalan bip sesi duyulur. İşlem süresince her 2 saniyede bir kısa bir bip çalar.

**Gereksinim:** ffmpeg.exe gereklidir. Eklenti klasörüne yerleştirilen ffmpeg.exe otomatik olarak kullanılır; farklı bir konumdaysa yol Ayarlar'dan belirtilebilir. ffmpeg'i [ffmpeg.org](https://ffmpeg.org/download.html) adresinden indirin.

## Ses Yansıtma

`Ctrl+Win+M` kısayolu, çalan akışı eş zamanlı olarak ikinci bir ses çıkış aygıtına yansıtır. Hoparlör ve kulaklık gibi iki farklı aygıttan aynı anda dinlemek için kullanışlıdır.

İlk basışta mevcut çıkış aygıtlarını listeleyen bir seçim iletişim kutusu açılır. Bir aygıt seçildiğinde yansıtma başlar ve ana oynatma kesintisiz devam eder. Kısayola tekrar basıldığında yansıtma durdurulur.

**Kullanım senaryoları:**
- **Hoparlör + kulaklık** — Siz bilgisayar hoparlöründen dinlerken bir misafirin aynı yayını kulaklıkla takip etmesini sağlayın.
- **Kayıt kurulumu** — Ana çıkışı hoparlöre, ikinci çıkışı harici bir kayıt cihazına veya ses arabirimine yönlendirin.
- **Çok odalı** — Bluetooth hoparlör ve dahili hoparlörden eş zamanlı çalın; sesi başka bir odaya taşımak için ek yazılım gerekmez.
- **Uzaktan izleme** — Ekran paylaşımı veya uzak masaüstü oturumunda hem yerel hem de uzak taraf aynı akışı eş zamanlı duyabilir.

> **Not:** Ses yansıtma yalnızca BASS arka ucu aktifken kullanılabilir. Yansıtma aktifken ses seviyesi değiştirilirse her iki çıkış da eş zamanlı güncellenir.

## Kayıt

Kayıtlar varsayılan olarak `Belgeler\FreeRadio Recordings\` klasörüne kaydedilir. Dosya adı istasyon adını (veya şarkı kaydı modunda parça adını) ve kayıt başlangıç saatini içerir. Kayıt klasörü NVDA Menüsü → Tercihler → Ayarlar → FreeRadio → **Kayıt klasörü** seçeneğinden istediğiniz zaman değiştirilebilir. Kayıt motoru doğrudan akışa bağlandığından ses, alındığı hâliyle diske yazılır; herhangi bir işleme veya yeniden kodlama uygulanmaz; kayıt kalitesi yayın kalitesiyle özdeştir.

**Anlık kayıt:** Bir istasyon çalarken `Ctrl+Win+E` tuşuna bir kez basın. Durdurmak için tekrar basın. Oynatma süresince kesintisiz devam eder.

**Şarkı kaydı:** ICY metadata yayınlayan bir istasyon çalarken `Ctrl+Win+E` tuşuna **hızlıca iki kez** basın. Kayıt hemen başlar ve o anki parça adıyla adlandırılır. Parça değiştiğinde kayıt otomatik olarak durur ve NVDA kaydedilen dosya adını seslendirir. Parça bitmeden kaydı erken sonlandırmak istiyorsanız `Ctrl+Win+E` tuşuna tekrar iki kez basın. Çalan istasyon ICY metadata yayınlamıyorsa şarkı kaydı kullanılamaz ve NVDA bunu bildirir.

**Zamanlanmış kayıt:** Tarayıcıda Kayıt sekmesini açın. Favorilerden bir istasyon seçin, başlangıç saatini SS:DD biçiminde ve süreyi dakika cinsinden girin, ardından bir kayıt modu seçin:

- **Dinleyerek kaydet** — eş zamanlı olarak çalar ve kaydeder. BASS → VLC → PotPlayer → Windows Media Player öncelik sırası kullanılarak bir oynatma arka ucu başlatılır.
- **Yalnızca kaydet** — herhangi bir ses çıkışı olmaksızın arka planda sessizce kaydeder; kayıt motoru doğrudan akışa bağlanır.

Girilen saat geçmişse kayıt ertesi güne planlanır. NVDA kayıt başladığında ve bittiğinde bildirim verir.

## Zamanlayıcı

İstasyon tarayıcısında Zamanlayıcı sekmesini açın (`Alt+4`). İki tür zamanlayıcı eklenebilir:

**Alarm — radyoyu başlat:** Belirtilen saatte favoriler listesinden seçilen istasyonu otomatik olarak çalmaya başlar. İstasyonu ve saati SS:DD biçiminde girin.

**Uyku — radyoyu durdur:** Belirtilen saatte oynatmayı durdurur. Zamanlayıcı tetiklendiğinde ses 60 saniye boyunca kademeli olarak kısılır, ardından oynatma durur. İstasyon seçmeye gerek yoktur; yalnızca saat girilmesi yeterlidir.

Her iki tür için de girilen saat geçmişse işlem ertesi güne planlanır. Bekleyen zamanlayıcılar sekmede listelenir; listeden seçip Seçili Zamanlayıcıyı Kaldır düğmesine basılarak iptal edilebilir.

## Ayarlar

NVDA Menüsü → Tercihler → Ayarlar → FreeRadio bölümünden aşağıdaki seçenekler yapılandırılabilir:

| Seçenek | Açıklama |
|---|---|
| Ses çıkış cihazı (BASS arka ucu) | Radyo sesinin yönlendirileceği çıkış aygıtını belirler. Listede sistemdeki BASS uyumlu tüm ses aygıtları ve "Sistem varsayılanı" seçeneği yer alır. Kaydedildiğinde değişiklik anında uygulanır; seçili aygıt bağlantısı kesilirse otomatik olarak sistem varsayılanına dönülür ve bildirim verilir. Yalnızca BASS arka ucu aktifken geçerlidir. |
| Ses seviyesi | Eklentinin başlangıç ses seviyesini belirler (0–200). Çalma sırasında `Ctrl+Win+↑` / `Ctrl+Win+↓` ile değiştirilen değer buraya da yansır. |
| Başlangıç ses efekti | NVDA başladığında veya istasyon çalmaya başladığında uygulanacak varsayılan ses efektini belirler. Seçilen efekt, İstasyon Tarayıcısı'nda Efektler listesindeki seçimle eşleşir. Yalnızca BASS arka ucu aktifken geçerlidir. |
| İstasyon geçiş efekti (BASS arka ucu) | İstasyonlar arasında geçiş yapılırken uygulanacak davranışı belirler. **Anlık kesme** (varsayılan) yeni istasyon başlamadan önce eskisini hemen durdurur. **Kısa geçiş efekti (1 saniye)** ve **Normal geçiş efekti (2 saniye)** seçeneklerinde yeni istasyon hiç boşluk olmadan hemen başlar; yeni akışın aktif olduğu onaylandıktan sonra eski istasyonun sesi arka planda kademeli olarak azaltılarak kesilir. Anlık kesme seçiliyken herhangi bir performans etkisi yoktur. Yalnızca BASS arka ucu aktifken geçerlidir. |
| NVDA başlangıcında devam ettir | Açıksa NVDA her başlatıldığında en son çalınan istasyon otomatik olarak yeniden başlar. |
| Parça değişimlerini otomatik seslendir (ICY metadata) | Açıksa çalan istasyon ICY metadata yayınlıyorken parça her değiştiğinde NVDA yeni parça adını otomatik olarak okur. İstasyon değiştiğinde de ilk parça bilgisi anında seslendirilir. Varsayılan olarak kapalıdır. |
| Bildirimleri sessize al | Açıksa NVDA; istasyon değişikliklerini, oynatma durumu değişikliklerini (çal, duraklat, durdur) ve kayıt olaylarını (başladı, durdu, bitti) anons etmez. Hata mesajları, favori geri bildirimleri, müzik tanıma sonuçları ve güncelleme bildirimleri bu kapsamın dışındadır. Atanmamış bir girdi hareketi aracılığıyla anlık olarak da değiştirilebilir. Varsayılan olarak kapalıdır. |
| Beğenilen şarkıları metin dosyasına kaydet | Açıksa `Ctrl+Win+İ` üç kez basıldığında panoya kopyalanan parça bilgisi, kayıt klasöründeki `likedSongs.txt` dosyasına da eklenir. ICY metadata yoksa Shazam tanıma sonucu da aynı dosyaya kaydedilir. Varsayılan olarak kapalıdır. |
| Ctrl+Win+P hiç istasyon çalmıyorken: | Bu kısayola basıldığında aktif oynatma yoksa ne yapılacağını belirler: son çalınan istasyonu başlat veya favoriler listesini aç. |
| Ctrl+Win+P iki kez basıldığında: | Kısayola art arda iki kez basıldığında gerçekleşecek işlemi seçer: hiçbir şey yapma, favoriler listesini aç, kayıt sekmesini aç veya zamanlayıcı sekmesini aç. "Hiçbir şey yapma" seçiliyken ilk basışta gecikme uygulanmaz ve yanıt anında gerçekleşir. |
| Ctrl+Win+P üç kez basıldığında: | Kısayola art arda üç kez basıldığında gerçekleşecek işlemi seçer: hiçbir şey yapma, favoriler listesini aç, arama sekmesini aç, kayıt sekmesini aç veya zamanlayıcı sekmesini aç. |
| ffmpeg.exe yolu | Müzik tanıma için kullanılan ffmpeg.exe'nin konumu. Boş bırakılırsa eklenti klasöründeki ffmpeg.exe otomatik olarak kullanılır. |
| VLC yolu | VLC kurulu değilse veya standart dışı bir konumdaysa yürütülebilir dosyanın tam yolu buraya girilebilir. |
| wmplayer.exe yolu | Windows Media Player'ın yolu gerekiyorsa buraya girilebilir. |
| PotPlayer yolu | PotPlayer standart dışı bir konumdaysa yolu buraya girilebilir. |
| Kayıt klasörü | Kayıt dosyalarının yazılacağı klasörü belirler. Boş bırakılırsa varsayılan konum olan `Belgeler\FreeRadio Recordings\` kullanılır. Gözat düğmesiyle klasör seçilebilir. Değişiklikler kaydedildikten hemen sonra geçerli olur. |
| Güncellemeleri otomatik denetle | Açıksa NVDA her başlatıldığında arka planda güncelleme kontrolü yapılır; yeni sürüm bulunursa bildirim verilir. Kapatıldığında otomatik kontrol devre dışı kalır, elle kontrol hâlâ kullanılabilir. |
| İstasyon çalmadan önce internet bağlantısı kontrolünü devre dışı bırak | İstasyon çalmaya başlamadan önce gecikme yaşayan kullanıcılar için önerilir. DNS'in engellendiği durumlarda da faydalıdır. |

## Bildirimleri Sessize Alma

Ayarlar'dan **Bildirimleri sessize al** seçeneği açıldığında NVDA aşağıdaki otomatik anonsları susturur:

- Yeni istasyon çalmaya başladığında istasyon adı
- Oynatma durumu değişiklikleri: çal, duraklat, durdur
- Kayıt olayları: başladı, durdu, bitti (anlık, şarkı ve zamanlanmış kayıtlar)
- Parça değişimi anonsları — **Parça değişimlerini otomatik seslendir** seçeneği açık olsa bile

Aşağıdakiler bu ayardan kasıtlı olarak **etkilenmez:** hata mesajları, favori geri bildirimleri (eklendi / zaten listede), müzik tanıma sonuçları ve güncelleme bildirimleri.

Ayar NVDA Menüsü → Tercihler → Ayarlar → FreeRadio bölümünden açılıp kapatılabileceği gibi atanmamış bir girdi hareketi aracılığıyla da anlık olarak değiştirilebilir (NVDA Menüsü → Tercihler → Girdi Hareketleri → FreeRadio). Değiştirildiğinde NVDA, işlemi onaylamak için bir kez "Bildirimler sessize alındı" veya "Bildirimler açıldı" anonsunu yapar.

## Otomatik Parça Bildirimi

Ayarlar'dan **Parça değişimlerini otomatik seslendir** seçeneği açıldığında FreeRadio, çalan istasyonun ICY metadata akışını arka planda yaklaşık her 5 saniyede bir kontrol eder. Parça bilgisi değiştiğinde yeni başlık NVDA tarafından otomatik olarak okunur; herhangi bir tuşa basmak gerekmez.

İstasyon değiştirildiğinde yeni istasyonun ilk parça bilgisi bağlantı kurulur kurulmaz seslendirilir. ICY metadata yayınlamayan bir istasyona geçildiğinde sistem sessiz kalır ve bir önceki istasyonun parça bilgisi tekrar edilmez.

Bu özellik varsayılan olarak kapalıdır; NVDA Menüsü → Tercihler → Ayarlar → FreeRadio bölümünden açılıp kapatılabilir.

## Beğenilen Şarkılar

Ayarlar'dan **Beğenilen şarkıları metin dosyasına kaydet** seçeneği açıldığında `Ctrl+Win+İ` kısayoluna üç kez basıldığında panoya kopyalanan parça bilgisi, kayıt klasöründeki `likedSongs.txt` dosyasına da satır satır eklenir (varsayılan: `Belgeler\FreeRadio Recordings\likedSongs.txt`).

ICY metadata mevcut olan istasyonlarda parça adı ve sanatçı bilgisi, metadata bulunmayan istasyonlarda ise Shazam tanıma sonucu kaydedilir; her iki durumda da aynı dosya kullanılır. Dosya yoksa otomatik oluşturulur; her kayıt dosyanın sonuna eklenir, önceki girişler silinmez.

## Beğenilen Şarkılar Sekmesi

İstasyon tarayıcısındaki **Beğenilen Şarkılar** sekmesi, `likedSongs.txt` dosyasına kaydedilmiş tüm parçaları listeler. Sekme her açıldığında liste dosyadan otomatik olarak yeniden yüklenir.

Listeden bir parça seçildiğinde üç işlem yapılabilir:

- **Spotify'da Çal:** Önce Spotify masaüstü uygulamasını açmayı dener. Uygulama kurulu değilse Spotify web sitesinde aramayı başlatır ve ilk sonucu otomatik oynatır.
- **YouTube'da Çal (`Alt+O`):** Seçili parçayla YouTube'da arama yapar ve sonuçları varsayılan tarayıcıda açar.
- **Sil (`Alt+M`):** Seçili parçayı `likedSongs.txt` dosyasından kaldırır ve listeyi günceller. Liste odaklanmışken `Delete` tuşu da aynı işlevi görür.
- **Yenile (`Alt+E`):** Listeyi dosyadan yeniden yükler.

Spotify ve YouTube düğmeleri ile Sil düğmesi, yalnızca listeden gerçek bir parça seçiliyken etkin olur.

## Oynatma

Eklenti ses çıkışı için şu öncelik sırasıyla bir arka uç seçer:

1. **BASS** — varsayılan ve birincil arka uç. Ayrı bir kurulum gerektirmez; eklentiyle birlikte gelir. BASS, sesi doğrudan Windows ses yığınına gönderir ve Windows ses mikseri üzerinde **pythonw.exe** adıyla bağımsız bir kaynak olarak görünür. Bu, FreeRadio sesinin NVDA konuşmasından tamamen ayrı bir kanal üzerinde aktığı anlamına gelir: NVDA bir şeyler okurken radyo sesi kesilmez, karışmaz ve NVDA'nın kendi ses ayarlarından etkilenmez. Kullanıcı Windows Ses Mikseri'nden radyo ses düzeyini NVDA'dan bağımsız olarak ayarlayabilir. HTTP, HTTPS ve gömülü çoğu akış biçimini destekler. Ses yansıtma yalnızca bu arka uçla kullanılabilir.
2. **VLC** — BASS başarısız olursa devreye girer. Yaygın kurulum konumlarında, kullanıcı profili klasörlerinde ve sistem PATH'inde otomatik aranır.
3. **PotPlayer** — VLC bulunamazsa denenir. Yaygın kurulum konumlarında otomatik aranır.
4. **Windows Media Player** — son seçenek olarak kullanılır; sistem üzerinde WMP bileşeni kurulu olmasını gerektirir.

## Güncelleme Kontrolü

FreeRadio, yeni sürüm olup olmadığını GitHub üzerinden otomatik olarak kontrol eder.

**Otomatik kontrol:** NVDA başladıktan 15 saniye sonra arka planda sessizce çalışır. Yeni bir sürüm bulunursa bildirim verilir; bulunamazsa herhangi bir mesaj gösterilmez.

**Elle kontrol:** NVDA Araçlar → FreeRadio → **Güncellemeleri Denetle...** menü öğesiyle istendiğinde tetiklenebilir. Bu yoldan başlatıldığında sürüm güncel olsa bile sonuç seslendirilir.

**Güncelleme bulunduğunda:** Sürüm numarasını ve yüklü sürümünüzü gösteren bir iletişim kutusu açılır.

- GitHub release'inde doğrudan indirilebilir bir `.nvda-addon` dosyası mevcutsa **İndir ve Kur** düğmesi gösterilir. Onaylandıktan sonra dosya arka planda indirilir, indirme başladığında NVDA bunu seslendirir ve ardından NVDA'nın kendi kurulum ekranı otomatik olarak açılır.
- Doğrudan indirme bağlantısı mevcut değilse **Sayfayı Aç** düğmesi gösterilir ve GitHub release sayfası varsayılan tarayıcıda açılır.

**Otomatik kontrolü devre dışı bırakmak için:** NVDA Menüsü → Tercihler → Ayarlar → FreeRadio bölümünden **Güncellemeleri otomatik denetle** seçeneği kapatılabilir.

## Lisans

GPL v2