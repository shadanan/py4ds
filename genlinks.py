import os
import re


def get_titles() -> dict[int, str]:
    problem_folders = sorted(
        [
            file
            for file in os.listdir(".")
            if os.path.isdir(file) and re.match(r"p\d{3}", file)
        ]
    )

    titles: dict[int, str] = {}
    for folder in problem_folders:
        index_md = os.path.join(folder, "index.md")
        id = int(folder[1:])
        with open(index_md) as fp:
            title = fp.readline().strip()
            if not title.startswith("# "):
                raise Exception(f"{index_md} didn't start with a header ('# ') line")
            titles[id] = title[2:]

    return titles


def generate_toc(titles: dict[int, str]) -> list[str]:
    return [
        f"- [Problem {id} - {title}](p{id:03}/index.md)" for id, title in titles.items()
    ]


def update_readme(titles: dict[int, str]):
    with open("README.md", "r") as fp:
        lines = fp.read().splitlines()

    result = []
    for line in lines:
        if line.startswith("## Table of Contents"):
            break
        result.append(line)

    result.append("## Table of Contents")
    result.append("")
    result += generate_toc(titles)

    with open("README.md", "w") as fp:
        fp.write("\n".join(result))


def main():
    titles = get_titles()
    update_readme(titles)


if __name__ == "__main__":
    main()
