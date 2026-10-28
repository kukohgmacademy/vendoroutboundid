import re

# 1. Update tentang-kami.html
with open('tentang-kami.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('assets/image/team-building.jpg', 'assets/image/kebutuhan-gambar/team-leader-instructions.webp')
with open('tentang-kami.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated tentang-kami.html")

# 2. Update paket.html
with open('paket.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('assets/image/paket/paket_team_building_1784793017845.jpg', 'assets/image/kebutuhan-gambar/team-building-flag.webp')
c = c.replace('assets/image/paket/paket-rafting-keluarga.webp', 'assets/image/kebutuhan-gambar/family-gathering-mountain.webp')
c = c.replace('assets/image/paket/ldks-batu-malang-formasi-barisan1.webp', 'assets/image/kebutuhan-gambar/students-cheering-puzzle.webp')
c = c.replace('assets/image/paket/paket_rafting_malang_1784793031028.jpg', 'assets/image/kebutuhan-gambar/group-whitewater-rafting.webp')
with open('paket.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated paket.html")

# 3. Update gallery.html
with open('gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

gallery_reps = [
    ('assets/image/paket/Rafting-by-the-concrete-waterfall.webp', 'assets/image/kebutuhan-gambar/jeeps-savannah-hill.webp'),
    ('assets/image/paket/River-rafting-adventure-under-the-waterfall.webp', 'assets/image/kebutuhan-gambar/friends-campfire-gathering.webp'),
    ('assets/image/paket/ldks-batu-malang-formasi-barisan2.webp', 'assets/image/kebutuhan-gambar/students-cheering-puzzle.webp'),
    ('assets/image/paket/paket-rafting-keluarga.webp', 'assets/image/kebutuhan-gambar/family-gathering-mountain.webp'),
    ('assets/image/paket/img-outbound-adventure.webp', 'assets/image/kebutuhan-gambar/tourists-picking-apples.webp'),
    ('assets/image/paket/ldks-batu-malang-formasi-barisan1.webp', 'assets/image/kebutuhan-gambar/student-ldks-megaphone.webp'),
    ('assets/image/paket/permainan-seru.jpg', 'assets/image/kebutuhan-gambar/schoolchildren-planting-tree.webp'),
    ('assets/image/paket/paket_team_building_1784793017845.jpg', 'assets/image/kebutuhan-gambar/team-building-flag.webp'),
    ('assets/image/paket/paket_rafting_malang_1784793031028.jpg', 'assets/image/kebutuhan-gambar/group-whitewater-rafting.webp'),
]

for old, new in gallery_reps:
    c = c.replace(old, new)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated gallery.html")

# 4. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Hero main image
# Replace hero-beranda.webp with hero-bromo-sunrise.webp in the hero section
# Note: line 464 is the hero image
c = re.sub(
    r'(<div class="hero-media-card">.*?<img src=")assets/image/hero/hero-beranda\.webp(")',
    r'\g<1>assets/image/kebutuhan-gambar/hero-bromo-sunrise.webp\g<2>',
    c,
    flags=re.DOTALL
)

# 4 cards under Destinasi & Paket Populer in hero:
# Card 1: Outbound Perusahaan
c = re.sub(
    r'(<span class="hero-dest-chip-title">Outbound Perusahaan</span>.*?<img src=")assets/image/paket/paket_team_building_[^"]+(")',
    r'\g<1>assets/image/kebutuhan-gambar/team-building-flag.webp\g<2>',
    c,
    flags=re.DOTALL
)
# If img is before title:
c = re.sub(
    r'(<img src=")assets/image/paket/paket_team_building_[^"]+(" alt="Outbound Perusahaan di Batu Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/team-building-flag.webp\g<2>',
    c
)
c = re.sub(
    r'(<img src=")assets/image/paket/paket-rafting-keluarga\.webp(" alt="Family Gathering di Batu Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/family-gathering-mountain.webp\g<2>',
    c
)
c = re.sub(
    r'(<img src=")assets/image/paket/ldks-batu-malang-formasi-barisan1\.webp(" alt="Outbound Sekolah & LDKS di Batu Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/students-listening-trainer.webp\g<2>',
    c
)
c = re.sub(
    r'(<img src=")assets/image/paket/paket_rafting_malang_[^"]+(" alt="Outbound Wisata & Rafting di Batu Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/group-whitewater-rafting.webp\g<2>',
    c
)

# Program Pilihan Unggulan (4 program cards):
# 1. Team Building
c = re.sub(
    r'(<img src=")assets/image/paket/paket_team_building_[^"]+("[\s\n]+alt="Outbound Team Building Perusahaan di Batu Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/employees-corporate-banner.webp\g<2>',
    c
)
# 2. Family Gathering
c = re.sub(
    r'(<img src=")assets/image/paket/paket-rafting-keluarga\.webp("[\s\n]+alt="Family Gathering & Rekreasi Edukasi di Batu Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/sack-race-fun-games.webp\g<2>',
    c
)
# 3. Sekolah & LDKS
c = re.sub(
    r'(<img src=")assets/image/paket/ldks-batu-malang-formasi-barisan1\.webp("[\s\n]+alt="Outbound Sekolah & LDKS Karakter Siswa di Batu Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/student-ldks-megaphone.webp\g<2>',
    c
)
# 4. Wisata Rafting & Offroad
c = re.sub(
    r'(<img src=")assets/image/paket/paket_rafting_malang_[^"]+("[\s\n]+alt="Wisata Petualangan Rafting & Offroad Jeep di Batu Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/rafting-team-celebrating.webp\g<2>',
    c
)

# Keunggulan Geografis (line 997):
c = re.sub(
    r'(<img src=")assets/image/hero/hero-beranda\.webp(" alt="Pemandangan Alam Pegunungan Batu Malang)',
    r'\g<1>assets/image/kebutuhan-gambar/dest-coban-rondo.webp\g<2>',
    c
)

# Galeri Dokumentasi (5 cards in beranda):
# 1. Coban Rondo
c = re.sub(
    r'(<img src=")assets/image/paket/paket_team_building_[^"]+("[\s\n]+alt="Simulasi Team Building Perusahaan di Wana Wisata Coban Rondo)',
    r'\g<1>assets/image/kebutuhan-gambar/low-rope-team-building.webp\g<2>',
    c
)
# 2. Selecta
c = re.sub(
    r'(<img src=")assets/image/paket/permainan-seru\.jpg(" alt="Family Gathering Outdoor Games di Taman Selecta Batu")',
    r'\g<1>assets/image/kebutuhan-gambar/family-giant-ball-game.webp\g<2>',
    c
)
# 3. Kaliwatu
c = re.sub(
    r'(<img src=")assets/image/paket/paket_rafting_malang_[^"]+("[\s\n]+alt="Wisata Rafting Arung Jeram Kaliwatu Batu)',
    r'\g<1>assets/image/kebutuhan-gambar/corporate-water-games.webp\g<2>',
    c
)
# 4. Bedengan
c = re.sub(
    r'(<img src=")assets/image/paket/ldks-batu-malang-formasi-barisan1\.webp("[\s\n]+alt="Program LDKS dan Character Building Siswa di Bumi Perkemahan Bedengan Malang")',
    r'\g<1>assets/image/kebutuhan-gambar/students-cheering-puzzle.webp\g<2>',
    c
)
# 5. Coban Talun
c = re.sub(
    r'(<img src=")assets/image/paket/River-rafting-adventure-under-the-waterfall\.webp("[\s\n]+alt="Camping dan Malam Keakraban Api Unggun di Coban Talun Kota Batu")',
    r'\g<1>assets/image/kebutuhan-gambar/friends-campfire-gathering.webp\g<2>',
    c
)

# Lightbox default placeholder:
c = re.sub(
    r'(<img src=")assets/image/paket/paket_team_building_[^"]+(" alt="" id="lightboxMainImg")',
    r'\g<1>assets/image/kebutuhan-gambar/team-building-flag.webp\g<2>',
    c
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated index.html")
