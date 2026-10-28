import glob, re, os

# Mapping definitions for the 20 packages
PACKAGES_MAP = {
    'character-building.html': {
        'main': 'students-cheering-puzzle.webp',
        'thumbs': [
            'students-cheering-puzzle.webp',
            'young-adults-log-bridge.webp',
            'team-solving-puzzle-obstacle.webp',
            'low-rope-team-building.webp',
            'students-listening-trainer.webp'
        ]
    },
    'corporate-gathering.html': {
        'main': 'employees-corporate-banner.webp',
        'thumbs': [
            'employees-corporate-banner.webp',
            'corporate-gala-dinner.webp',
            'morning-stretching-gathering.webp',
            'team-building-flag.webp',
            'prog-gala-dinner.webp'
        ]
    },
    'edukasi.html': {
        'main': 'schoolchildren-planting-tree.webp',
        'thumbs': [
            'schoolchildren-planting-tree.webp',
            'group-forest-orientation.webp',
            'students-wooden-clogs-bakiak.webp',
            'tourists-picking-apples.webp',
            'students-listening-trainer.webp'
        ]
    },
    'family-gathering.html': {
        'main': 'family-gathering-mountain.webp',
        'thumbs': [
            'family-gathering-mountain.webp',
            'family-gathering-lakeside.webp',
            'family-picnic-gathering.webp',
            'family-giant-ball-game.webp',
            'family-tug-of-war.webp'
        ]
    },
    'fun-games.html': {
        'main': 'sack-race-fun-games.webp',
        'thumbs': [
            'sack-race-fun-games.webp',
            'students-wooden-clogs-bakiak.webp',
            'family-giant-ball-game.webp',
            'family-carnival-games.webp',
            'family-tug-of-war.webp'
        ]
    },
    'ldks-leadership.html': {
        'main': 'student-ldks-megaphone.webp',
        'thumbs': [
            'student-ldks-megaphone.webp',
            'students-listening-trainer.webp',
            'young-adults-log-bridge.webp',
            'group-forest-orientation.webp',
            'team-leader-instructions.webp'
        ]
    },
    'leadership-camp.html': {
        'main': 'young-adults-log-bridge.webp',
        'thumbs': [
            'young-adults-log-bridge.webp',
            'student-ldks-megaphone.webp',
            'group-forest-orientation.webp',
            'friends-campfire-gathering.webp',
            'team-solving-puzzle-obstacle.webp'
        ]
    },
    'outbound-camping.html': {
        'main': 'friends-campfire-gathering.webp',
        'thumbs': [
            'friends-campfire-gathering.webp',
            'prog-camping.webp',
            'prog-glamping.webp',
            'family-pine-forest.webp',
            'family-picnic-gathering.webp'
        ]
    },
    'outbound-offroad.html': {
        'main': 'land-rovers-mud-offroad.webp',
        'thumbs': [
            'land-rovers-mud-offroad.webp',
            'jeeps-savannah-hill.webp',
            'prog-offroad-jeep.webp',
            'hero-bromo-sunrise.webp',
            'tour-group-celebration.webp'
        ]
    },
    'outbound-pelajar.html': {
        'main': 'students-listening-trainer.webp',
        'thumbs': [
            'students-listening-trainer.webp',
            'students-cheering-puzzle.webp',
            'students-wooden-clogs-bakiak.webp',
            'young-adults-log-bridge.webp',
            'schoolchildren-planting-tree.webp'
        ]
    },
    'outbound-perusahaan.html': {
        'main': 'team-building-flag.webp',
        'thumbs': [
            'team-building-flag.webp',
            'employees-corporate-banner.webp',
            'employees-balance-challenge.webp',
            'low-rope-team-building.webp',
            'team-leader-instructions.webp'
        ]
    },
    'outbound-plus-wisata.html': {
        'main': 'tourists-picking-apples.webp',
        'thumbs': [
            'tourists-picking-apples.webp',
            'tour-group-celebration.webp',
            'dest-batu-malang.webp',
            'jeeps-savannah-hill.webp',
            'family-gathering-mountain.webp'
        ]
    },
    'outbound-rafting.html': {
        'main': 'group-whitewater-rafting.webp',
        'thumbs': [
            'group-whitewater-rafting.webp',
            'rafting-team-celebrating.webp',
            'corporate-water-games.webp',
            'team-building-flag.webp',
            'tour-group-celebration.webp'
        ]
    },
    'outbound-sekolah.html': {
        'main': 'schoolchildren-planting-tree.webp',
        'thumbs': [
            'schoolchildren-planting-tree.webp',
            'students-listening-trainer.webp',
            'students-cheering-puzzle.webp',
            'students-wooden-clogs-bakiak.webp',
            'group-forest-orientation.webp'
        ]
    },
    'outbound-wisata.html': {
        'main': 'tour-group-celebration.webp',
        'thumbs': [
            'tour-group-celebration.webp',
            'tourists-picking-apples.webp',
            'dest-batu-malang.webp',
            'jeeps-savannah-hill.webp',
            'family-gathering-lakeside.webp'
        ]
    },
    'paket-custom.html': {
        'main': 'employees-corporate-banner.webp',
        'thumbs': [
            'employees-corporate-banner.webp',
            'group-whitewater-rafting.webp',
            'family-gathering-mountain.webp',
            'land-rovers-mud-offroad.webp',
            'corporate-gala-dinner.webp'
        ]
    },
    'paket-hemat.html': {
        'main': 'sack-race-fun-games.webp',
        'thumbs': [
            'sack-race-fun-games.webp',
            'low-rope-team-building.webp',
            'family-pine-forest.webp',
            'students-wooden-clogs-bakiak.webp',
            'family-picnic-gathering.webp'
        ]
    },
    'paket-premium.html': {
        'main': 'corporate-gala-dinner.webp',
        'thumbs': [
            'corporate-gala-dinner.webp',
            'prog-glamping.webp',
            'family-highland-park.webp',
            'jeeps-savannah-hill.webp',
            'group-whitewater-rafting.webp'
        ]
    },
    'paket-standard.html': {
        'main': 'team-building-flag.webp',
        'thumbs': [
            'team-building-flag.webp',
            'low-rope-team-building.webp',
            'sack-race-fun-games.webp',
            'family-gathering-lakeside.webp',
            'morning-stretching-gathering.webp'
        ]
    },
    'team-building.html': {
        'main': 'team-building-flag.webp',
        'thumbs': [
            'team-building-flag.webp',
            'employees-balance-challenge.webp',
            'low-rope-team-building.webp',
            'team-solving-puzzle-obstacle.webp',
            'employees-corporate-banner.webp'
        ]
    }
}

def update_detail_page(filename):
    filepath = os.path.join('paket', filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    cfg = PACKAGES_MAP[filename]
    main_img = f"../assets/image/kebutuhan-gambar/{cfg['main']}"
    thumbs = [f"../assets/image/kebutuhan-gambar/{t}" for t in cfg['thumbs']]

    # 1. Update productMainImage
    content = re.sub(
        r'(<img\s+id=["\']productMainImage["\'][^>]*src=["\'])[^"\']*(["\'])',
        rf'\g<1>{main_img}\g<2>',
        content
    )
    # Also if id is after src
    content = re.sub(
        r'(<img[^>]*src=["\'])[^"\']*(["\'][^>]*id=["\']productMainImage["\'])',
        rf'\g<1>{main_img}\g<2>',
        content
    )

    # 2. Update 5 thumbnails in prod-thumbs-wrapper
    def replace_thumbs(match):
        block = match.group(0)
        # find each button.prod-thumb-btn
        btns = list(re.finditer(r'(<button[^>]*class=["\']prod-thumb-btn[^>]*>.*?)(</button>)', block, re.DOTALL))
        for idx, btn_match in enumerate(btns):
            if idx < len(thumbs):
                new_t = thumbs[idx]
                btn_str = btn_match.group(1)
                # replace data-img
                btn_str = re.sub(r'data-img=["\'][^"\']*["\']', f'data-img="{new_t}"', btn_str)
                # replace img src
                btn_str = re.sub(r'(<img[^>]*src=["\'])[^"\']*(["\'])', rf'\g<1>{new_t}\g<2>', btn_str)
                full_btn = btn_str + btn_match.group(2)
                block = block.replace(btn_match.group(0), full_btn)
        return block

    content = re.sub(
        r'<div class=["\']prod-thumbs-wrapper["\'].*?</div>\s*</div>',
        replace_thumbs,
        content,
        count=1,
        flags=re.DOTALL
    )

    # 3. Update related cards: replace old paket/*.jpg or *.webp with contextual ones
    related_replacements = [
        (r'../assets/image/paket/paket_team_building_[^"\']+', '../assets/image/kebutuhan-gambar/team-building-flag.webp'),
        (r'../assets/image/paket/permainan-seru\.(?:jpg|webp)', '../assets/image/kebutuhan-gambar/sack-race-fun-games.webp'),
        (r'../assets/image/paket/paket_rafting_malang_[^"\']+', '../assets/image/kebutuhan-gambar/group-whitewater-rafting.webp'),
        (r'../assets/image/paket/paket-rafting-keluarga\.webp', '../assets/image/kebutuhan-gambar/family-gathering-mountain.webp'),
        (r'../assets/image/paket/ldks-batu-malang-formasi-barisan1\.webp', '../assets/image/kebutuhan-gambar/student-ldks-megaphone.webp'),
        (r'../assets/image/paket/ldks-batu-malang-formasi-barisan2\.webp', '../assets/image/kebutuhan-gambar/students-cheering-puzzle.webp'),
        (r'../assets/image/paket/River-rafting-adventure-under-the-waterfall\.webp', '../assets/image/kebutuhan-gambar/group-whitewater-rafting.webp'),
        (r'../assets/image/paket/Rafting-by-the-concrete-waterfall\.webp', '../assets/image/kebutuhan-gambar/rafting-team-celebrating.webp'),
        (r'../assets/image/paket/img-outbound-adventure\.webp', '../assets/image/kebutuhan-gambar/tourists-picking-apples.webp'),
        (r'../assets/image/paket/img-outbound\.webp', '../assets/image/kebutuhan-gambar/low-rope-team-building.webp'),
        (r'../assets/image/paket/vendor-outbound-batu-malang-fasilitas\.webp', '../assets/image/kebutuhan-gambar/corporate-gala-dinner.webp'),
        (r'../assets/image/paket/paket-all-in-outbound-batu-malang\.webp', '../assets/image/kebutuhan-gambar/employees-corporate-banner.webp'),
        (r'../assets/image/paket/mini-squad-rafting-outbound\.webp', '../assets/image/kebutuhan-gambar/corporate-water-games.webp'),
        (r'../assets/image/paket/perbandingan-budget-rafting-tim-kecil-sekantor\.webp', '../assets/image/kebutuhan-gambar/morning-stretching-gathering.webp'),
        (r'../assets/image/paket/rombongan-rafting-sungai\.webp', '../assets/image/kebutuhan-gambar/group-whitewater-rafting.webp'),
        (r'../assets/image/paket/minimal-peserta-booking-rafting\.webp', '../assets/image/kebutuhan-gambar/rafting-team-celebrating.webp'),
    ]

    for pat, rep in related_replacements:
        content = re.sub(pat, rep, content)

    # 4. Also replace in schema JSON-LD if present
    content = re.sub(
        r'(https://venroroutbound\.id/)assets/image/paket/[^"\']+',
        rf'\g<1>assets/image/kebutuhan-gambar/{cfg["main"]}',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

for fname in PACKAGES_MAP:
    update_detail_page(fname)
