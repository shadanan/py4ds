import json
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Problem:
    id: str
    index: int
    title: str

    @property
    def instructions(self) -> str:
        return os.path.join(self.id, "index.md")

    def link(self, relative="."):
        path = os.path.join(relative, self.instructions)
        return f"[Problem {self.index} - {self.title}]({path})"


@dataclass
class LinkManager:
    problems: list[Problem]

    @staticmethod
    def create() -> "LinkManager":
        with open("problems.json", "r") as fp:
            ids: list[str] = json.load(fp)

        problems: list[Problem] = []
        for index, id in enumerate(ids):
            if not os.path.exists(id):
                raise Exception(f"Folder for problem {id} is missing")
            index_md = os.path.join(id, "index.md")
            with open(index_md) as fp:
                title = fp.readline().strip()
                if not title.startswith("# "):
                    raise Exception(
                        f"Instructions for problem {id} didn't start with a header ('# ') line"
                    )
                problems.append(Problem(id, index, title[2:]))

        return LinkManager(problems)

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
        result += [f"- {problem.link()}" for problem in self.problems]
        result.append("")

        with open("README.md", "w") as fp:
            fp.write("\n".join(result))

    def update_instruction(self, curr: Problem, next: Problem):
        with open(curr.instructions, "r") as fp:
            lines = fp.read().splitlines()

        result = []
        for line in lines:
            if line.startswith("Next up: "):
                break
            result.append(line)
        else:
            result.append("")

        result.append(f"Next up: {next.link(relative='..')}")
        result.append("")

        with open(curr.instructions, "w") as fp:
            fp.write("\n".join(result))

    def update_instructions(self):
        for curr, next in zip(self.problems[0:-1], self.problems[1:]):
            self.update_instruction(curr, next)


def main():
    link_manager = LinkManager.create()
    link_manager.update_readme()
    link_manager.update_instructions()


if __name__ == "__main__":
    main()
