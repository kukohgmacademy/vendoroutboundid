with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix Program Card 1 & 2
c = c.replace(
    'src="assets/image/paket/paket_team_building_1784793017845.jpg"',
    'src="assets/image/kebutuhan-gambar/employees-corporate-banner.webp"'
)
c = c.replace(
    'src="assets/image/paket/paket-rafting-keluarga.webp"',
    'src="assets/image/kebutuhan-gambar/sack-race-fun-games.webp"'
)

# Fix Bento data-src attributes
c = c.replace(
    'data-src="assets/image/paket/paket_team_building_1784793017845.jpg"',
    'data-src="assets/image/kebutuhan-gambar/low-rope-team-building.webp"'
)
c = c.replace(
    'data-src="assets/image/paket/permainan-seru.jpg"',
    'data-src="assets/image/kebutuhan-gambar/family-giant-ball-game.webp"'
)
c = c.replace(
    'data-src="assets/image/paket/paket_rafting_malang_1784793031028.jpg"',
    'data-src="assets/image/kebutuhan-gambar/corporate-water-games.webp"'
)
c = c.replace(
    'data-src="assets/image/paket/ldks-batu-malang-formasi-barisan1.webp"',
    'data-src="assets/image/kebutuhan-gambar/students-cheering-puzzle.webp"'
)
c = c.replace(
    'data-src="assets/image/paket/River-rafting-adventure-under-the-waterfall.webp"',
    'data-src="assets/image/kebutuhan-gambar/friends-campfire-gathering.webp"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed index.html remaining old references!")
