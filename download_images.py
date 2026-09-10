#!/usr/bin/env python3
"""Download all Squarespace CDN images for the rediscoveryourworld.com migration.
Saves web-sized versions (?format=1600w) into assets/img/."""
import os, re, urllib.request, urllib.parse, time

DEST = os.path.expanduser("~/workspace/rediscoveryourworld-site/assets/img")
os.makedirs(DEST, exist_ok=True)

CDN = "https://images.squarespace-cdn.com/content/v1/587453dcbe65949768debce2"

def sq(path, web=True):
    url = CDN + path
    return url + ("?format=1600w" if web and not path.lower().endswith(".png") else "")

MANIFEST = [
    # home
    ("home-salem-water-log.jpg", sq("/1560915849018-6HSHSIPNIGZFZN0EZFWR/Salem_Water_Log.jpg")),
    ("home-church-flag-lake-sunset.jpg", sq("/1484162966746-CVY1T0O4FEJRUWLMKGGN/High+White+Church%2C+Flag+and+Lake+Close+Together+at+Sunset.jpg")),
    ("home-stormy-sunset.jpg", sq("/1484114032978-JT3GR7Y0DYJ63YLWXDLH/Stormy+Sunset.jpg")),
    ("home-fog-in-valley.jpg", sq("/1515785047174-FHX2XGX1W3SPS3W7GC0L/Fog+In+Valley+1.jpg")),
    ("home-client-grid.png", sq("/1539360395830-SYC2QM2VLWCJ9GX0BNFH/Client+Grid+3.png")),
    # about
    ("about-wakefield-center.jpg", sq("/1484432645001-RSH8T1P1K0T5IMBX2PD1/Wakefield+Center+2.jpg")),
    ("about-team-graphic.png", sq("/1491009367666-2IMOXLB2RKJTMECEY3LY/image-asset.png")),
    # images gallery
    ("gallery-whale-photo.jpg", sq("/1543199945700-P2J04QMMXJO23RRC0OJL/The+Whale+Photo.JPG")),
    ("gallery-soaring-with-bird.jpg", sq("/1543199959418-9P0E4H0NUSS8PS2VE5XE/Soaring+with+Bird.JPG")),
    ("gallery-geese-textured-water.jpg", sq("/1543199950457-NEYUC67T0VQ4U5EHZP60/Geese+In+Textured+Water.JPG")),
    ("gallery-main-building.jpg", sq("/1543199954314-XWWAC40W6FN3JG16NVPK/Main_Building_1.JPG")),
    ("gallery-salem-lighthouse.jpg", sq("/1543199955405-MBWR0PPO9AVGLG218YMZ/Salem+Lighthouse.JPG")),
    ("gallery-mit-over-water.jpg", sq("/1543199961593-YIJDKVR2C1ZBKKABWNZM/MIT_Over_Water.JPG")),
    ("gallery-incarnation-church.jpg", sq("/1543199958874-1G232EQDZT2ZX517U93V/Incarnation_Church.JPG")),
    ("gallery-scituate-lighthouse.jpg", sq("/1543199959578-U62P6NEOKI6F7ZCFT94W/Scituate_Lighthouse.JPG")),
    ("gallery-hilltop-house.jpg", sq("/1543199948168-DX4J85BP41MN9T0T2AV6/Hilltop+House.JPG")),
    ("gallery-baseball-low-close.jpg", sq("/1543199955475-XFOLEPFUAPZIPA9H2DQ6/Baseball+Low+Close.JPG")),
    ("gallery-campfire.jpg", sq("/1543199950105-VCQNH3DPQH079TBT0GD9/Campfire.JPG")),
    ("gallery-fisherman-working.jpg", sq("/1543199957516-4L4FOBURCPQM5KGEZHAL/Fisherman+Working.JPG")),
    ("gallery-mountain-valley-resort.jpg", sq("/1484432125814-SW28JBR4HD0H244YZEM2/Mountain+Valley+Resort+1.jpg")),
    # panoramas
    ("pano-grahamville-ludlow-vt.jpg", sq("/1484180464955-XZGXVGORB0EODWSZW7ZE/FoggySunrise")),
    ("pano-glacier-point-yosemite.jpg", sq("/30ae7b5f-7530-40bd-a780-129f0973a348/Yosemite")),
    ("pano-mount-sheridan-yellowstone.jpg", sq("/670fcf68-cd7a-43e9-81b0-15b2f3875fac/DSC00126-Pano.jpg")),
    ("pano-mit-cambridge.jpg", sq("/1501087015570-5Z90973T2CPDDSK20D79/MIT+Panorama+2.jpg")),
    ("pano-jackson-gore-ludlow-vt.jpg", sq("/1484180534334-KV8RJP1F7F07QQLBP1FY/JacksonGore")),
    ("pano-norris-geyser-basin.jpg", sq("/a0e2e3b1-6862-4663-9c2f-21e146d60603/DSC00292-Pano.jpg")),
    ("pano-charles-river-boston.jpg", sq("/1515373373029-0KO4K9DN0R2V62M1JDPK/Charles+River.jpg")),
    ("pano-lower-falls-yellowstone.jpg", sq("/58af3902-005f-44a6-a736-719764a68f7d/DSC00787-Pano-2.jpg")),
    ("pano-main-building-notre-dame.jpg", sq("/1539360541231-GSW90CSGSGYLNFGYP0K9/Pano1_20.jpg")),
    ("pano-ell-pond-melrose.jpg", sq("/1484180712358-NQG0889F97RQ250EF9PE/Ell+Pond")),
    ("pano-spot-pond-stoneham.jpg", sq("/1484180677392-0V3CK657NC3LDK7KC4YH/Spot+Pond")),
    ("pano-county-hwy-ab-wisconsin.jpg", sq("/94c8cdcf-be26-453d-8c4f-7ad35ff94714/IMG_0180-Pano.jpg")),
    ("pano-winter-island-salem.jpg", sq("/1528577635154-SRBJL4BHNJFM3QPIXRRR/Salem+Full+Landscape+3.5x1+Medium.jpg")),
    ("pano-lake-quannapowitt-wakefield.jpg", sq("/1484180831541-45SM82NH2UMKG9M8UCM5/Quannapowitt")),
    ("pano-fellsway-ponds.jpg", sq("/1484182961723-LRS6J4EIOYKS13GDFKRD/Fellsway+Ponds.jpg")),
    # videos header, puckerman, contact, assembly row
    ("videos-wakefield-center.jpg", sq("/1484433409337-0PG4IQ8T6G9K164MVJO6/Wakefield+Center.jpg")),
    ("puckerman-snow-day.jpg", sq("/1484092048215-B009DHIPJ36FSQVMERZ3/c4bca6ec3ba8bd61f57ded620d183dad_day_1316_866.jpg")),
    ("contact-wakefield-sunrise.jpg", sq("/1484432401687-3SHU5KCDH32I95BAA392/Wakefield+Center+Sunrise+4.jpg")),
    ("assembly-row-135ft.jpg", sq("/1500473484970-DJJ69O9G1OKIEQDALLJT/135FeetAssemblyPano")),
    ("assembly-row-145ft.jpg", sq("/1500473734062-RFHFWCQ06P4W5CWN7MG3/145FeetAssemblyPano")),
]

total = 0
failed = []
for name, url in MANIFEST:
    dest = os.path.join(DEST, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        total += os.path.getsize(dest)
        continue
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
            data = r.read()
            f.write(data)
            total += len(data)
        print(f"OK  {name} ({len(data)//1024} KB)")
        time.sleep(0.3)
    except Exception as e:
        failed.append((name, str(e)))
        print(f"FAIL {name}: {e}")

print(f"\nDownloaded: {len(MANIFEST)-len(failed)}/{len(MANIFEST)}, total {total/1024/1024:.1f} MB")
if failed:
    print("Failed:", failed)
