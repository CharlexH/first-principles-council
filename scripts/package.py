"""Maintainer-only packaging. Recipients need no Python or dependencies."""
from pathlib import Path
import hashlib
import shutil
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.3.0"
OUT = ROOT / "dist"


def build():
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="first-principles-package-") as tmp:
        stage = Path(tmp)
        shutil.copytree(ROOT / "skills/first-principles-thinking", stage / "first-principles-thinking")
        for name in ("START-HERE.txt", "LICENSE", "THIRD_PARTY_NOTICES.md"):
            shutil.copy2(ROOT / name, stage / name)
        for name in ("source-review.md", "method-sources.md"):
            dest = stage / "docs" / name
            dest.parent.mkdir(exist_ok=True)
            shutil.copy2(ROOT / "docs" / name, dest)
        (stage / "EVALUATION.md").write_text("# 效果对照\n\n请打开 [完整评测](docs/evaluation.md)。原始案例和答卷在 evals/ 目录；未验证真实收入。\n")
        shutil.copy2(ROOT / "docs/evaluation.md", stage / "docs/evaluation.md")
        shutil.copytree(ROOT / "evals", stage / "evals")
        core = (ROOT / "skills/first-principles-thinking/SKILL.md").read_text()
        sources = (ROOT / "skills/first-principles-thinking/references/method-notes.md").read_text()
        paste = "请在本轮对话使用以下方法；随后回答我补充的问题。用我的语言作答。\n\n" + core + "\n\n" + sources + "\n\n我的问题：\n"
        (stage / "PASTE-INTO-AGENT.txt").write_text(paste, encoding="utf-8-sig")
        files = sorted(p for p in stage.rglob("*") if p.is_file())
        checksum = "".join(hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.relative_to(stage).as_posix() + "\n" for p in files)
        (stage / "CHECKSUMS.sha256").write_text(checksum)
        archive = OUT / f"first-principles-council-v{VERSION}-offline.zip"
        with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(stage.rglob("*")):
                if p.is_file():
                    info = zipfile.ZipInfo(p.relative_to(stage).as_posix(), date_time=(2026, 11, 4, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    z.writestr(info, p.read_bytes())
        with zipfile.ZipFile(archive) as z:
            assert z.testzip() is None
            for line in z.read("CHECKSUMS.sha256").decode().splitlines():
                digest, name = line.split("  ", 1)
                assert hashlib.sha256(z.read(name)).hexdigest() == digest
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        (OUT / "SHA256SUMS").write_text(f"{digest}  {archive.name}\n")
        print(f"{archive.name}: {archive.stat().st_size} bytes; SHA256 {digest}")


if __name__ == "__main__":
    build()
