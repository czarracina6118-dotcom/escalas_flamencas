"""Bundle the existing CC0 FreePats guitar samples for offline APK playback."""
from pathlib import Path
from urllib.request import urlopen
import hashlib

REVISION = '6f4eb1b092acc88f5448cea1a0001bd07b971af8'
EXPECTED = {'E2.flac': '18ce73f4243991132901b47efe3affa155c1b934d838cf02a29df5c62c8706a8', 'G2.flac': '71e69e5eff738f668b4e3e2f53f72de7725fd3b7969339bb44aba8e7c1df78d2', 'A2.flac': '692be630714f59824b612502034b53e9c376374386cb255b81a0bd3c4cdcdd92', 'C3.flac': 'eac0fe1fc03225d81f813667babee072662c101800bc5ad7fb12d9ef3324b986', 'E3.flac': 'f8cc3192a328f10cdb774ff3bf5efb06d1015e64c5ae141c1c31143bb329c915', 'G3.flac': 'd4f3277f48067a3b7e1818b34d08eeec66d727101c744554632397aeb7dd844d', 'A3.flac': '08d2e90e80839bdb77342d7dcc8a73e0ec8849607d1a750ce433f9e7f0789e06', 'C4.flac': 'e8fcd63c262ebef3e84d1f24242918cc578f8b0db54049ad109815b01d1226f0', 'E4.flac': 'b8882fbba2b6a9d0cbae02867be4273aa8f0fddd00bc6f3d993dff6c77997246', 'G4.flac': '5e3423ab0440fe8cc337ada529c2bb1696914e4465b336d3635630b4ea7b4916', 'A4.flac': 'bac918520eb26172cd734e79df9c53fc206e5aab60884583dd7d9ab5b17d16d1', 'C5.flac': '84b8a00c7caff015d8b7165330f0c868fd73d300adb3199cb15452841d1c5444', 'E5.flac': 'f8323fb0fb66dd655683e1944f0073281e44a6244fdb3f2922851a9cb120bc81', 'G5.flac': '0d887f7f14d526e5af1a1aa7060af92c49e3dc57f1e534c215ce93b8e3f31cc8', 'A5.flac': 'a0111ff90a40a7d68155803d0708c3c025cc1db44c3e222270c900d56b845a43', 'B5.flac': '0c417e8aa71eb880d612e298285e78dc9762277a46227f9b04345e8be7d17066', 'LICENSE': 'a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499'}
BASE = "https://raw.githubusercontent.com/freepats/spanish-classical-guitar/" + REVISION + "/"

def main():
    dest = Path(__file__).resolve().parent / "app/src/main/assets/samples"
    dest.mkdir(parents=True, exist_ok=True)
    for name, expected in EXPECTED.items():
        relative = "LICENSE" if name == "LICENSE" else "samples/" + name
        with urlopen(BASE + relative, timeout=30) as response:
            data = response.read()
        if hashlib.sha256(data).hexdigest() != expected:
            raise RuntimeError("Sample integrity mismatch: " + name)
        (dest / name).write_bytes(data)
    print("Verified and bundled", len(EXPECTED)-1, "guitar samples and CC0 license")

if __name__ == "__main__":
    main()
