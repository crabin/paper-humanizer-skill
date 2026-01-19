#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def main():
    ap = argparse.ArgumentParser(description="Build a prompt for academic humanization (CN/EN).")
    ap.add_argument("--text-file", type=str, help="Input text file path. If omitted, read from stdin.")
    ap.add_argument("--language", default="auto", choices=["auto", "zh", "en"])
    ap.add_argument("--field", default="computer science")
    ap.add_argument("--audience", default="academic")
    ap.add_argument("--tone", default="formal", choices=["formal", "semi-formal", "concise", "persuasive"])
    ap.add_argument("--strict-factuality", action="store_true", default=True)
    ap.add_argument("--no-strict-factuality", action="store_false", dest="strict_factuality")
    ap.add_argument("--keep-citations", action="store_true", default=True)
    ap.add_argument("--drop-citations", action="store_false", dest="keep_citations")
    ap.add_argument("--blacklist-level", default="high", choices=["low", "medium", "high"])

    ap.add_argument("--system", default="prompts/system.md")
    ap.add_argument("--template", default="prompts/user_template.md")
    ap.add_argument("--out", default="", help="Write the composed prompt to file (optional).")

    args = ap.parse_args()

    root = Path(__file__).resolve().parents[1]
    system_md = read_text(root / args.system)
    template_md = read_text(root / args.template)

    if args.text_file:
        text = read_text(Path(args.text_file))
    else:
        import sys
        text = sys.stdin.read()

    composed = []
    composed.append("### SYSTEM\n")
    composed.append(system_md.strip() + "\n\n")
    composed.append("### USER\n")
    user = template_md
    user = user.replace("{{language}}", args.language)
    user = user.replace("{{field}}", args.field)
    user = user.replace("{{audience}}", args.audience)
    user = user.replace("{{tone}}", args.tone)
    user = user.replace("{{strict_factuality}}", str(args.strict_factuality).lower())
    user = user.replace("{{keep_citations}}", str(args.keep_citations).lower())
    user = user.replace("{{output_format}}", "four_sections")
    user = user.replace("{{blacklist_level}}", args.blacklist_level)
    user = user.replace("{{text}}", text.strip())
    composed.append(user.strip() + "\n")

    final_prompt = "\n".join(composed)

    if args.out:
        Path(args.out).write_text(final_prompt, encoding="utf-8")
    else:
        print(final_prompt)

if __name__ == "__main__":
    main()