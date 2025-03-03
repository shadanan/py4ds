import argparse
import json
import os
import random
import re
from dataclasses import dataclass
from string import Template

INDEX_MD_PATTERN = re.compile(r"\[.*?\]\(\.\./+(p\d+)/index\.md\)")


@dataclass(frozen=True)
class Problem:
    id: str
    title: str
    next_id: str | None

    @property
    def instructions(self) -> str:
        return os.path.join(self.id, "index.md")

    def link(self, relative: str = "."):
        path = os.path.join(relative, self.instructions)
        return f"[Problem {self.id} - {self.title}]({path})"


@dataclass
class LinkManager:
    problems: dict[str, Problem]

    @staticmethod
    def create() -> "LinkManager":
        with open("problems.json", "r") as fp:
            ids: list[str] = json.load(fp)

        problems: dict[str, Problem] = {}
        for id, next_id in zip(ids, ids[1:] + [None]):
            if not os.path.exists(id):
                raise Exception(f"Folder for problem {id} is missing")
            index_md = os.path.join(id, "index.md")
            with open(index_md) as fp:
                title = fp.readline().strip()
                if not title.startswith("# "):
                    raise Exception(
                        f"Instructions for problem {id} didn't start with a header ('# ') line"
                    )
                problems[id] = Problem(id, title[2:], next_id)

        return LinkManager(problems)

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
        result += [f"- {problem.link()}" for problem in self.problems.values()]
        result.append("")

        with open("README.md", "w") as fp:
            fp.write("\n".join(result))

    def replace_link(self, match: re.Match[str]):
        return self.problems[match.group(1)].link(relative="..")

    def update_instruction(self, curr: Problem):
        with open(curr.instructions, "r") as fp:
            lines = fp.read().splitlines()

        result: list[str] = []
        for line in lines:
            if line.startswith("Next up: "):
                break
            result.append(INDEX_MD_PATTERN.sub(self.replace_link, line))
        else:
            result.append("")

        if curr.next_id is not None:
            next = self.problems[curr.next_id]
            result.append(f"Next up: {next.link(relative='..')}")
            result.append("")

        with open(curr.instructions, "w") as fp:
            fp.write("\n".join(result))

    def update_instructions(self):
        for problem in self.problems.values():
            self.update_instruction(problem)


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
    with open("problems.json", "r") as fp:
        problem_ids = json.load(fp)
    while True:
        new_problem_id = f"p{random.randint(0, 9999):04}"
        if new_problem_id not in problem_ids:
            break

    problem_ids.append(new_problem_id)
    with open("problems.json", "w") as fp:
        json.dump(problem_ids, fp)

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
