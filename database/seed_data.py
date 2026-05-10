"""
IliaChan TechWell — Health Education Seed Data
Comprehensive health data for 8 digital lifestyle topics.
"""

HEALTH_TOPICS = [
    {
        "topic_name": "Duduk Terlalu Lama di Depan Komputer",
        "category": "Ergonomics",
        "description": "Duduk dalam posisi statis selama berjam-jam di depan komputer tanpa istirahat yang cukup. Kebiasaan ini umum pada pekerja remote dan kantoran yang menghabiskan 8-12 jam sehari di depan layar. Tubuh manusia dirancang untuk bergerak, bukan duduk diam dalam waktu lama.",
        "risks": "Deep Vein Thrombosis (DVT), obesitas, penyakit kardiovaskular, diabetes tipe 2, degenerasi otot, masalah pencernaan, peningkatan risiko kanker kolon, penurunan sirkulasi darah ke ekstremitas bawah, herniated disc pada tulang belakang.",
        "symptoms": "Nyeri punggung bawah kronis, kaki bengkak atau kesemutan, kekakuan sendi pinggul, nyeri leher dan bahu, kelelahan berlebihan meski tidak beraktivitas fisik, penambahan berat badan, susah berkonsentrasi.",
        "solutions": "Terapkan aturan 20-20-20 (setiap 20 menit, berdiri 20 detik, lihat sejauh 20 kaki). Gunakan standing desk atau meja adjustable. Lakukan stretching ringan setiap 30-45 menit. Atur alarm pengingat untuk berdiri. Gunakan kursi ergonomis dengan penyangga lumbar. Pertimbangkan walking meeting untuk diskusi.",
        "prevention_tips": "Investasi pada standing desk converter. Set timer di HP untuk pengingat bergerak. Letakkan printer/air minum agak jauh agar harus berjalan.",
        "risk_level": "HIGH",
        "image_prompt": "Infographic showing a person sitting at a computer desk for too long with red warning indicators on spine, legs, and heart. Modern flat design, dark background, health education style, medical illustration."
    },
    {
        "topic_name": "Postur Duduk Bungkuk dan Miring",
        "category": "Posture",
        "description": "Kebiasaan duduk dengan postur tubuh yang salah seperti membungkuk ke depan, miring ke satu sisi, atau menunduk terlalu dalam saat bekerja di depan komputer. Postur buruk ini sering tidak disadari dan menjadi kebiasaan sehari-hari.",
        "risks": "Kifosis (punggung bungkuk permanen), skoliosis fungsional, carpal tunnel syndrome, tension headache kronis, kompresi saraf, hernia nukleus pulposus, forward head posture syndrome, ketidakseimbangan otot, nyeri kronis pada trapezius.",
        "symptoms": "Nyeri punggung atas dan leher persisten, sakit kepala tegang, bahu tidak sejajar, nyeri menjalar ke lengan, kesulitan bernapas dalam, kekakuan dada, postur kepala maju ke depan.",
        "solutions": "Atur monitor setinggi mata dengan jarak 50-70cm. Gunakan kursi dengan penyangga lumbar. Pastikan kaki menapak rata di lantai. Lakukan latihan penguatan otot core dan punggung. Pertimbangkan menggunakan posture corrector sementara untuk melatih kesadaran postur.",
        "prevention_tips": "Pasang cermin kecil di meja untuk cek postur. Gunakan aplikasi posture reminder. Latihan yoga atau pilates rutin.",
        "risk_level": "HIGH",
        "image_prompt": "Side-by-side comparison infographic of correct vs incorrect sitting posture at a computer desk. Left shows proper ergonomic posture, right shows hunched/slouched posture with red X marks. Modern medical illustration style, dark theme."
    },
    {
        "topic_name": "Terlalu Lama Rebahan Sambil Main HP",
        "category": "Sedentary",
        "description": "Kebiasaan berbaring di tempat tidur atau sofa sambil menggunakan smartphone dalam waktu lama. Posisi ini menyebabkan tekanan berlebih pada leher, pergelangan tangan, dan mata. Sering dilakukan saat scrolling media sosial atau menonton video.",
        "risks": "Text neck syndrome (leher teknologi), tendinitis pergelangan tangan, mata kering dan iritasi, gangguan tidur, atrofi otot, GERD (refluks asam lambung), peningkatan risiko trombosis, cervical spondylosis dini.",
        "symptoms": "Nyeri leher yang menjalar ke bahu, pergelangan tangan kaku dan nyeri, penglihatan kabur sementara, insomnia, nyeri punggung bawah, sensasi terbakar di dada (heartburn), jari-jari kesemutan.",
        "solutions": "Batasi waktu rebahan dengan HP maksimal 30 menit. Gunakan penyangga HP atau tablet holder. Jika harus rebahan, gunakan bantal yang menopang leher dengan benar. Atur HP pada mode night shift. Lakukan stretching leher secara berkala.",
        "prevention_tips": "Tetapkan zona bebas gadget di tempat tidur. Gunakan fitur Screen Time untuk membatasi. Ganti kebiasaan rebahan+HP dengan membaca buku fisik.",
        "risk_level": "MEDIUM",
        "image_prompt": "Educational illustration showing a person lying in bed using smartphone with anatomical overlay highlighting stressed neck, wrist, and eye areas in red/orange. Modern infographic style, dark background."
    },
    {
        "topic_name": "Bermain Gadget di Tempat Gelap",
        "category": "Eye Health",
        "description": "Menggunakan laptop, komputer, atau smartphone di ruangan gelap tanpa pencahayaan yang memadai dan tanpa mengurangi brightness layar atau menggunakan pelindung mata. Kontras tinggi antara layar terang dan lingkungan gelap sangat membebani mata.",
        "risks": "Digital eye strain (Computer Vision Syndrome), kerusakan retina akibat blue light berlebihan, miopi progresif, degenerasi makula dini, gangguan produksi melatonin, insomnia kronis, sakit kepala migrain, fotofobia.",
        "symptoms": "Mata perih dan berair, penglihatan kabur setelah penggunaan, sakit kepala di area dahi dan pelipis, mata kering persisten, kesulitan fokus pada objek jauh, sensitivitas cahaya meningkat, kedutan mata.",
        "solutions": "Selalu nyalakan lampu ambient saat menggunakan gadget. Aktifkan mode gelap dan night shift. Gunakan kacamata anti blue light. Terapkan aturan 20-20-20 untuk mata. Atur brightness layar sesuai pencahayaan ruangan. Gunakan aplikasi f.lux atau night light bawaan OS.",
        "prevention_tips": "Pasang lampu meja dengan cahaya hangat. Beli screen protector anti blue light. Atur auto-brightness di semua perangkat.",
        "risk_level": "HIGH",
        "image_prompt": "Dark room scene showing a person staring at a bright phone/laptop screen with blue light rays affecting their eyes. Anatomical eye detail showing strain. Health warning infographic, dark moody atmosphere, medical education style."
    },
    {
        "topic_name": "Bermain HP Sebelum Tidur Malam",
        "category": "Sleep Hygiene",
        "description": "Kebiasaan menggunakan smartphone menjelang waktu tidur, termasuk scrolling media sosial, membaca berita, atau menonton video. Blue light dari layar HP menekan produksi melatonin (hormon tidur) dan merangsang otak tetap aktif.",
        "risks": "Gangguan ritme sirkadian, insomnia kronis, penurunan kualitas tidur REM, kecemasan dan depresi, penurunan daya tahan tubuh, gangguan memori dan konsentrasi, peningkatan risiko obesitas, ketergantungan gadget (nomophobia).",
        "symptoms": "Sulit tertidur lebih dari 30 menit, sering terbangun di malam hari, merasa tidak segar saat bangun, kantuk berlebihan di siang hari, mood swing, penurunan produktivitas, lingkaran hitam di bawah mata.",
        "solutions": "Terapkan digital curfew: matikan semua gadget 1 jam sebelum tidur. Ganti kegiatan dengan membaca buku, meditasi, atau journaling. Aktifkan mode Do Not Disturb otomatis. Letakkan HP di luar jangkauan tempat tidur. Gunakan alarm fisik bukan alarm HP.",
        "prevention_tips": "Buat rutinitas wind-down tanpa gadget. Minum teh chamomile sebagai pengganti scrolling. Gunakan fitur Bedtime Reminder.",
        "risk_level": "HIGH",
        "image_prompt": "Split illustration: left side shows person in bed using phone with disrupted brain waves and suppressed melatonin, right side shows peaceful sleep with proper melatonin flow. Night time color palette, medical education infographic, dark theme."
    },
    {
        "topic_name": "Makan atau Snack di Atas Ranjang",
        "category": "Lifestyle",
        "description": "Kebiasaan makan makanan utama atau snack di atas tempat tidur, sering kali sambil menonton layar. Kebiasaan ini mengganggu sinyal lapar-kenyang otak, menciptakan asosiasi tempat tidur dengan aktivitas selain tidur, dan berpotensi menyebabkan masalah pencernaan.",
        "risks": "GERD dan refluks asam, penambahan berat badan (mindless eating), gangguan tidur karena asosiasi tempat tidur salah, alergi dari remah makanan dan tungau, masalah pencernaan, bakteri dan jamur di area tidur, tersedak saat makan sambil berbaring.",
        "symptoms": "Heartburn setelah makan di ranjang, kualitas tidur menurun, gatal-gatal kulit dari tungau, berat badan naik tanpa disadari, mual saat berbaring setelah makan, jerawat atau iritasi kulit.",
        "solutions": "Tetapkan aturan makan hanya di meja makan. Jika lapar menjelang tidur, makan snack ringan 2 jam sebelum tidur sambil duduk. Bersihkan tempat tidur secara rutin. Makan dengan mindful tanpa distraksi layar. Siapkan snack sehat di dapur.",
        "prevention_tips": "Jangan simpan makanan di kamar tidur. Buat jadwal makan teratur. Ganti snacking dengan minum air putih.",
        "risk_level": "MEDIUM",
        "image_prompt": "Infographic showing a person eating snacks in bed with warning indicators for digestive system, sleep quality, and hygiene issues. Clean medical illustration, dark background, educational health poster style."
    },
    {
        "topic_name": "Menatap Layar Tanpa Istirahat (Digital Eye Strain)",
        "category": "Eye Health",
        "description": "Menatap layar komputer, laptop, atau HP secara terus-menerus selama berjam-jam tanpa memberikan istirahat pada mata. Rata-rata pekerja digital menatap layar 10+ jam per hari, menyebabkan computer vision syndrome.",
        "risks": "Computer Vision Syndrome (CVS), mata kering kronis, miopi progresif terutama pada usia muda, astenopia (kelelahan mata), kerusakan sel retina dari blue light kumulatif, sakit kepala tension-type, penurunan kemampuan akomodasi mata.",
        "symptoms": "Mata terasa berat dan lelah, penglihatan buram intermiten, mata kering dan perih, sakit kepala area frontal, kesulitan memfokuskan pandangan, mata merah, sensasi ada benda asing di mata.",
        "solutions": "Terapkan aturan 20-20-20 secara konsisten. Kedipkan mata secara sadar (rata-rata normal 15-20x/menit, saat menatap layar turun jadi 5-7x). Gunakan artificial tears. Atur jarak layar 50-70cm. Sesuaikan font size agar tidak perlu mendekat. Periksa mata rutin ke dokter.",
        "prevention_tips": "Pasang reminder 20-20-20 di komputer. Gunakan humidifier di ruang kerja. Atur font size yang nyaman di semua perangkat.",
        "risk_level": "MEDIUM",
        "image_prompt": "Medical education infographic showing close-up of an eye with digital screen reflection, illustrating eye strain symptoms: dryness, redness, fatigue. Include 20-20-20 rule diagram. Dark theme, modern health poster."
    },
    {
        "topic_name": "Penggunaan Earphone Volume Tinggi Berkepanjangan",
        "category": "Hearing Health",
        "description": "Menggunakan earphone atau headphone dengan volume tinggi (>60% kapasitas) dalam waktu lama, terutama saat bekerja, gaming, atau mendengarkan musik. Paparan suara keras secara kumulatif menyebabkan kerusakan permanen pada sel rambut koklea di telinga dalam.",
        "risks": "Noise-Induced Hearing Loss (NIHL) permanen, tinnitus (telinga berdenging), hiperakusis (sensitivitas suara berlebih), infeksi telinga dari earphone kotor, gangguan keseimbangan, isolasi sosial akibat penurunan pendengaran, acoustic neuroma.",
        "symptoms": "Telinga berdenging setelah melepas earphone, kesulitan mendengar percakapan di keramaian, meminta orang mengulang perkataan, meningkatkan volume TV/musik secara bertahap, nyeri di dalam telinga, pusing atau vertigo ringan.",
        "solutions": "Terapkan aturan 60/60: volume maksimal 60%, durasi maksimal 60 menit kemudian istirahat. Gunakan headphone over-ear noise-cancelling yang mengurangi kebutuhan volume tinggi. Bersihkan earphone secara rutin. Pilih earphone dengan fitur volume limiter.",
        "prevention_tips": "Aktifkan volume limiter di settings HP. Gunakan noise-cancelling headphone. Istirahatkan telinga 10 menit setiap jam.",
        "risk_level": "HIGH",
        "image_prompt": "Health education infographic showing a person wearing headphones with sound wave visualization and anatomical ear cross-section highlighting damaged hair cells. Volume meter showing danger zone. Dark theme, medical illustration."
    },
]

HEALTH_JOURNALS = [
    {"topic_idx": 0, "title": "Sedentary Behaviour and Risk of All-Cause Mortality", "authors": "Biswas A, et al.", "year": 2015, "source": "Annals of Internal Medicine", "source_type": "journal", "summary": "Meta-analisis menunjukkan duduk lama meningkatkan risiko kematian dini hingga 24%, bahkan pada individu yang berolahraga rutin.", "url": "https://doi.org/10.7326/M14-1651"},
    {"topic_idx": 0, "title": "WHO Guidelines on Physical Activity and Sedentary Behaviour", "authors": "World Health Organization", "year": 2020, "source": "WHO", "source_type": "who", "summary": "WHO merekomendasikan membatasi waktu duduk dan menggantinya dengan aktivitas fisik intensitas apa pun untuk manfaat kesehatan.", "url": "https://www.who.int/publications/i/item/9789240015128"},
    {"topic_idx": 1, "title": "The Impact of Poor Posture on Musculoskeletal Health", "authors": "Korakakis V, et al.", "year": 2019, "source": "Musculoskeletal Science and Practice", "source_type": "journal", "summary": "Postur duduk yang buruk secara konsisten dikaitkan dengan nyeri muskuloskeletal kronis, terutama di area leher dan punggung.", "url": "https://doi.org/10.1016/j.msksp.2019.03.008"},
    {"topic_idx": 1, "title": "Ergonomic Workspace Design Guidelines", "authors": "OSHA", "year": 2021, "source": "Occupational Safety and Health Administration", "source_type": "government", "summary": "Panduan ergonomi tempat kerja termasuk pengaturan monitor, kursi, dan meja yang tepat untuk mencegah cedera postur.", "url": "https://www.osha.gov/ergonomics"},
    {"topic_idx": 2, "title": "Text Neck Syndrome in Smartphone Users", "authors": "Neupane S, et al.", "year": 2017, "source": "Journal of Family Medicine and Primary Care", "source_type": "journal", "summary": "Penggunaan smartphone dengan posisi menunduk menyebabkan beban pada vertebra servikal hingga 27kg, memicu text neck syndrome.", "url": "https://doi.org/10.4103/jfmpc.jfmpc_298_16"},
    {"topic_idx": 3, "title": "Blue Light and Its Effect on the Retina", "authors": "Zhao ZC, et al.", "year": 2018, "source": "International Journal of Ophthalmology", "source_type": "journal", "summary": "Paparan blue light berlebihan dari layar digital menyebabkan stres oksidatif pada sel retina dan berpotensi mempercepat degenerasi makula.", "url": "https://doi.org/10.18240/ijo.2018.12.20"},
    {"topic_idx": 3, "title": "Digital Eye Strain and Blue Light Exposure", "authors": "Sheppard AL, Wolffsohn JS", "year": 2018, "source": "BMJ Open Ophthalmology", "source_type": "journal", "summary": "Penggunaan layar di lingkungan gelap meningkatkan kontras cahaya yang menyebabkan kelelahan mata digital lebih cepat.", "url": "https://doi.org/10.1136/bmjophth-2018-000152"},
    {"topic_idx": 4, "title": "Evening Use of Light-Emitting Devices Negatively Affects Sleep", "authors": "Chang AM, et al.", "year": 2015, "source": "Proceedings of the National Academy of Sciences", "source_type": "journal", "summary": "Penggunaan perangkat layar sebelum tidur menekan melatonin, menunda onset tidur, dan mengurangi kualitas tidur REM.", "url": "https://doi.org/10.1073/pnas.1418490112"},
    {"topic_idx": 4, "title": "Screen Time and Sleep Among Adolescents and Adults", "authors": "Hale L, Guan S", "year": 2015, "source": "Sleep Medicine Reviews", "source_type": "journal", "summary": "Review sistematis menunjukkan korelasi kuat antara screen time malam hari dengan berkurangnya durasi dan kualitas tidur.", "url": "https://doi.org/10.1016/j.smrv.2014.07.007"},
    {"topic_idx": 5, "title": "Eating Behaviors and Sleep Quality", "authors": "Zhao M, et al.", "year": 2020, "source": "Journal of Clinical Sleep Medicine", "source_type": "journal", "summary": "Makan terlalu dekat waktu tidur dikaitkan dengan peningkatan gejala GERD dan penurunan kualitas tidur secara signifikan.", "url": "https://doi.org/10.5664/jcsm.8356"},
    {"topic_idx": 6, "title": "Computer Vision Syndrome: A Review", "authors": "Loh K, Redd S", "year": 2008, "source": "Survey of Ophthalmology", "source_type": "journal", "summary": "CVS mempengaruhi 50-90% pekerja komputer dengan gejala utama mata kering, kelelahan mata, dan penglihatan kabur.", "url": "https://doi.org/10.1016/j.survophthl.2007.12.003"},
    {"topic_idx": 6, "title": "The 20-20-20 Rule: Evidence and Application", "authors": "AAO", "year": 2022, "source": "American Academy of Ophthalmology", "source_type": "journal", "summary": "Aturan 20-20-20 terbukti efektif mengurangi gejala digital eye strain pada 78% pengguna layar rutin.", "url": "https://www.aao.org/eye-health/tips-prevention/computer-usage"},
    {"topic_idx": 7, "title": "Noise-Induced Hearing Loss in Young Adults", "authors": "Le TN, et al.", "year": 2017, "source": "Journal of Otolaryngology", "source_type": "journal", "summary": "1.1 miliar anak muda berisiko mengalami gangguan pendengaran akibat penggunaan earphone dengan volume berlebihan.", "url": "https://doi.org/10.1186/s40463-017-0234-1"},
    {"topic_idx": 7, "title": "Safe Listening: WHO Standards for Personal Audio Devices", "authors": "WHO", "year": 2022, "source": "World Health Organization", "source_type": "who", "summary": "WHO merekomendasikan batas volume 60% dan durasi penggunaan earphone maksimal 60 menit per sesi.", "url": "https://www.who.int/activities/making-listening-safe"},
]

HEALTH_RECOMMENDATIONS = [
    # Topic 0: Duduk terlalu lama
    {"topic_idx": 0, "recommendation": "Gunakan standing desk atau desk converter agar bisa bergantian duduk-berdiri setiap 30 menit", "difficulty": "medium", "time_required": "Investasi sekali, manfaat jangka panjang", "equipment_needed": "Standing desk converter (Rp 500rb-2jt)"},
    {"topic_idx": 0, "recommendation": "Set alarm setiap 25 menit (teknik Pomodoro) untuk berdiri dan stretching 5 menit", "difficulty": "easy", "time_required": "5 menit per sesi", "equipment_needed": "Timer/aplikasi Pomodoro"},
    {"topic_idx": 0, "recommendation": "Lakukan walking meeting untuk diskusi yang tidak memerlukan layar", "difficulty": "easy", "time_required": "Durasi meeting", "equipment_needed": "Tidak ada"},
    # Topic 1: Postur bungkuk
    {"topic_idx": 1, "recommendation": "Atur tinggi monitor agar bagian atas layar sejajar dengan mata, jarak 50-70cm", "difficulty": "easy", "time_required": "5 menit setup", "equipment_needed": "Monitor stand atau buku tebal sebagai pengganjal"},
    {"topic_idx": 1, "recommendation": "Lakukan latihan wall angel 3x sehari (10 repetisi) untuk melatih postur tegak", "difficulty": "easy", "time_required": "5 menit per sesi", "equipment_needed": "Dinding rata"},
    {"topic_idx": 1, "recommendation": "Gunakan lumbar support cushion pada kursi kerja untuk menjaga kelengkungan alami tulang belakang", "difficulty": "easy", "time_required": "Setup sekali", "equipment_needed": "Lumbar cushion (Rp 100rb-300rb)"},
    # Topic 2: Rebahan + HP
    {"topic_idx": 2, "recommendation": "Batasi screen time saat rebahan maksimal 20 menit, gunakan timer otomatis", "difficulty": "medium", "time_required": "Pengaturan sekali", "equipment_needed": "Fitur Screen Time bawaan HP"},
    {"topic_idx": 2, "recommendation": "Gunakan tablet/phone holder yang bisa di-mount di samping tempat tidur untuk mengurangi beban leher", "difficulty": "easy", "time_required": "Setup sekali", "equipment_needed": "Phone holder/gooseneck mount (Rp 50rb-150rb)"},
    # Topic 3: Gadget di tempat gelap
    {"topic_idx": 3, "recommendation": "Pasang lampu LED strip warm white di belakang monitor sebagai bias lighting", "difficulty": "easy", "time_required": "15 menit instalasi", "equipment_needed": "LED strip USB (Rp 30rb-80rb)"},
    {"topic_idx": 3, "recommendation": "Gunakan kacamata anti blue light saat bekerja di depan layar lebih dari 2 jam", "difficulty": "easy", "time_required": "Pakai saat bekerja", "equipment_needed": "Kacamata anti blue light (Rp 50rb-500rb)"},
    {"topic_idx": 3, "recommendation": "Aktifkan fitur Night Light/Night Shift di semua perangkat dan atur jadwal otomatis", "difficulty": "easy", "time_required": "5 menit pengaturan", "equipment_needed": "Tidak ada (fitur bawaan OS)"},
    # Topic 4: HP sebelum tidur
    {"topic_idx": 4, "recommendation": "Terapkan digital curfew: letakkan semua gadget di ruangan lain 1 jam sebelum tidur", "difficulty": "hard", "time_required": "Konsistensi harian", "equipment_needed": "Jam alarm fisik sebagai pengganti alarm HP"},
    {"topic_idx": 4, "recommendation": "Ganti scrolling HP dengan rutinitas wind-down: baca buku fisik, journaling, atau meditasi", "difficulty": "medium", "time_required": "15-30 menit", "equipment_needed": "Buku/jurnal tulis"},
    # Topic 5: Makan di ranjang
    {"topic_idx": 5, "recommendation": "Tetapkan aturan zero food in bed, makan selalu di meja makan", "difficulty": "medium", "time_required": "Perubahan kebiasaan", "equipment_needed": "Tidak ada"},
    {"topic_idx": 5, "recommendation": "Jika lapar malam, siapkan snack sehat di dapur dan makan sambil duduk minimal 2 jam sebelum tidur", "difficulty": "easy", "time_required": "10 menit", "equipment_needed": "Snack sehat (buah, kacang)"},
    # Topic 6: Menatap layar tanpa istirahat
    {"topic_idx": 6, "recommendation": "Install aplikasi pengingat 20-20-20 seperti Eye Care 20 20 20 atau EyeLeo", "difficulty": "easy", "time_required": "5 menit install", "equipment_needed": "Aplikasi gratis"},
    {"topic_idx": 6, "recommendation": "Gunakan artificial tears (tetes mata) setiap 2-3 jam saat bekerja di depan layar", "difficulty": "easy", "time_required": "30 detik per aplikasi", "equipment_needed": "Artificial tears (Rp 30rb-80rb)"},
    # Topic 7: Earphone volume tinggi
    {"topic_idx": 7, "recommendation": "Aktifkan fitur volume limiter di pengaturan HP (biasanya di Health/Sound settings)", "difficulty": "easy", "time_required": "2 menit pengaturan", "equipment_needed": "Tidak ada (fitur bawaan)"},
    {"topic_idx": 7, "recommendation": "Investasi pada headphone noise-cancelling agar tidak perlu menaikkan volume untuk mengalahkan suara sekitar", "difficulty": "medium", "time_required": "Investasi sekali", "equipment_needed": "Noise-cancelling headphone (Rp 300rb-3jt)"},
]
