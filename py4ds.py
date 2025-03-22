import argparse
import os
import random
import re
from dataclasses import dataclass
from string import Template

INDEX_MD_PATTERN = re.compile(r"\[.*?\]\(\.+/+(p\d+)/index\.md\)")


@dataclass
class LinkManager:
    problem_ids: list[str]

    @classmethod
    def create(cls):
        with open("README.md", "r") as fp:
            lines = fp.read().splitlines()

        ids = [
            match.group(1)
            for line in lines[lines.index("## Table of Contents") :]
            if line.startswith("- ") and (match := INDEX_MD_PATTERN.search(line))
        ]

        return cls(ids)

    def get_index_md(self, id: str) -> str:
        return os.path.join(id, "index.md")

    def get_title(self, id: str) -> str:
        if not os.path.exists(id):
            raise Exception(f"Folder for problem {id} is missing")
        with open(self.get_index_md(id)) as fp:
            title = fp.readline().strip()
            if not title.startswith("# "):
                raise Exception(
                    f"Instructions for problem {id} didn't start with a header ('# ') line"
                )
        return title[2:]

    def get_link(self, id: str, relative: str = "."):
        path = os.path.join(relative, self.get_index_md(id))
        return f"[Problem {id} - {self.get_title(id)}]({path})"

    def get_next(self, id: str) -> str | None:
        index = self.problem_ids.index(id)
        if index + 1 < len(self.problem_ids):
            return self.problem_ids[index + 1]
        return None

    def append(self) -> str:
        existing_problems = set(self.problem_ids)
        while True:
            new_problem_id = f"p{random.randint(0, 9999):04}"
            if new_problem_id not in existing_problems:
                break
        self.problem_ids.append(new_problem_id)
        return new_problem_id

    def update_readme(self):
        with open("README.md", "r") as fp:
            lines = fp.read().splitlines()

        result: list[str] = []
        for line in lines:
            if line.startswith("## Table of Contents"):
                break
            result.append(line)
        else:
            result.append("")

        result.append("## Table of Contents")
        result.append("")
        result += [f"- {self.get_link(id)}" for id in self.problem_ids]
        result.append("")

        with open("README.md", "w") as fp:
            fp.write("\n".join(result))

    def replace_link(self, match: re.Match[str]):
        return self.get_link(match.group(1), relative="..")

    def update_instruction(self, id: str):
        with open(self.get_index_md(id), "r") as fp:
            lines = fp.read().splitlines()

        result: list[str] = []
        for line in lines:
            if line.startswith("Next up: "):
                break
            result.append(INDEX_MD_PATTERN.sub(self.replace_link, line))
        else:
            result.append("")

        next_id = self.get_next(id)
        if next_id is not None:
            result.append(f"Next up: {self.get_link(next_id, relative='..')}")
            result.append("")

        with open(self.get_index_md(id), "w") as fp:
            fp.write("\n".join(result))

    def update_instructions(self):
        for id in self.problem_ids:
            self.update_instruction(id)


def update_links():
    link_manager = LinkManager.create()
    link_manager.update_readme()
    link_manager.update_instructions()


INDEX_MD = Template("""
# ${title}

- Problem: [problem.py](problem.py) _(create this file)_
- Template: [template.py](template.py) _(copy starter code from here)_
- Tests: [test_all.py](test_all.py) _(tests that verify your solution)_
- Solution: [solution.py](solution.py) _(our solution)_

**_Note: The [problem.py](problem.py) doesn't exist yet! After clicking the link above, click "Create File"._**
""")

TESTS_PY = Template("""
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING or "PY4DS_PYTEST" in os.environ:
    from .solution import ${func}
else:
    from .problem import ${func}
""")

TEMPLATE_PY = Template("""
def ${func}(): ...
""")


def add_problem(func: str, title: str):
    link_manager = LinkManager.create()
    new_problem_id = link_manager.append()

    os.makedirs(new_problem_id)
    with open(os.path.join(new_problem_id, "__init__.py"), "w") as fp:
        pass
    with open(os.path.join(new_problem_id, "index.md"), "w") as fp:
        fp.write(INDEX_MD.substitute({"title": title}).lstrip())

    substitution = {"func": func}
    with open(os.path.join(new_problem_id, "test_all.py"), "w") as fp:
        fp.write(TESTS_PY.substitute(substitution).lstrip())
    with open(os.path.join(new_problem_id, "template.py"), "w") as fp:
        fp.write(TEMPLATE_PY.substitute(substitution).lstrip())
    with open(os.path.join(new_problem_id, "solution.py"), "w") as fp:
        fp.write(TEMPLATE_PY.substitute(substitution).lstrip())

    link_manager.update_readme()


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(title="commands", required=True)

    update_links_parser = subparsers.add_parser("update-links")
    update_links_parser.set_defaults(cmd="update-links")

    add_problem_parser = subparsers.add_parser("add-problem")
    add_problem_parser.set_defaults(cmd="add-problem")
    add_problem_parser.add_argument("func", help="The name of the function")
    add_problem_parser.add_argument("title", help="The title of the problem")

    args = parser.parse_args()

    if args.cmd == "update-links":
        update_links()
        return

    if args.cmd == "add-problem":
        add_problem(args.func, args.title)


if __name__ == "__main__":
    main()
