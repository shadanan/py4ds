import os
import re
from dataclasses import dataclass


@dataclass
class LinkManager:
    titles: dict[int, str]

    @staticmethod
    def create() -> "LinkManager":
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
                    raise Exception(
                        f"{index_md} didn't start with a header ('# ') line"
                    )
                titles[id] = title[2:]

        return LinkManager(titles)

    def get_link(self, id: int) -> str:
        return f"[Problem {id} - {self.titles[id]}](p{id:03}/index.md)"

    def update_readme(self):
        with open("README.md", "r") as fp:
            lines = fp.read().splitlines()

        result = []
        for line in lines:
            if line.startswith("## Table of Contents"):
                break
            result.append(line)
        else:
            result.append("")

        result.append("## Table of Contents")
        result.append("")
        result += [f"- {self.get_link(id)}" for id in self.titles.keys()]
        result.append("")

        with open("README.md", "w") as fp:
            fp.write("\n".join(result))

    def update_instruction(self, id: int):
        index_md = f"p{id:03}/index.md"
        with open(index_md, "r") as fp:
            lines = fp.read().splitlines()

        result = []
        for line in lines:
            if line.startswith("Next up: "):
                break
            result.append(line)
        else:
            result.append("")

        result.append(f"Next up: {self.get_link(id + 1)}")
        result.append("")

        with open(index_md, "w") as fp:
            fp.write("\n".join(result))

    def update_instructions(self):
        for id in self.titles.keys():
            if id + 1 in self.titles:
                self.update_instruction(id)


def main():
    link_manager = LinkManager.create()
    link_manager.update_readme()
    link_manager.update_instructions()


if __name__ == "__main__":
    main()
