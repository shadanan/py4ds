import os

if "PY4DS_PYTEST" in os.environ:
    from .solution import read_csv
else:
    from .problem import read_csv  # type: ignore

example_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "example.csv")


def test_example():
    expected = [
        {"name": "Alice Smith", "phone_number": "555-0123"},
        {"name": "Bob Jones", "phone_number": "555-4567"},
        {"name": "Carol Wu", "phone_number": "555-8901"},
    ]
    actual = read_csv(example_csv)
    assert actual == expected


def test_salaries():
    expected = [
        {
            "name": "John Smith",
            "title": "Software Engineer",
            "industry": "Technology",
            "salary": "95000",
        },
        {
            "name": "Emily Johnson",
            "title": "Marketing Manager",
            "industry": "Advertising",
            "salary": "78500",
        },
        {
            "name": "Michael Chen",
            "title": "Financial Analyst",
            "industry": "Finance",
            "salary": "82000",
        },
        {
            "name": "Sarah Williams",
            "title": "HR Director",
            "industry": "Human Resources",
            "salary": "110000",
        },
        {
            "name": "David Rodriguez",
            "title": "Product Manager",
            "industry": "Technology",
            "salary": "115000",
        },
        {
            "name": "Jessica Lee",
            "title": "Graphic Designer",
            "industry": "Media",
            "salary": "65000",
        },
        {
            "name": "Robert Taylor",
            "title": "Sales Director",
            "industry": "Retail",
            "salary": "92500",
        },
        {
            "name": "Amanda Brown",
            "title": "Research Scientist",
            "industry": "Pharmaceuticals",
            "salary": "105000",
        },
        {
            "name": "James Wilson",
            "title": "Operations Manager",
            "industry": "Manufacturing",
            "salary": "88000",
        },
        {
            "name": "Olivia Garcia",
            "title": "Legal Counsel",
            "industry": "Legal",
            "salary": "125000",
        },
        {
            "name": "Daniel Kim",
            "title": "Data Scientist",
            "industry": "Technology",
            "salary": "108000",
        },
        {
            "name": "Sophia Martinez",
            "title": "Account Executive",
            "industry": "Finance",
            "salary": "76000",
        },
        {
            "name": "Thomas Jackson",
            "title": "Project Manager",
            "industry": "Construction",
            "salary": "85000",
        },
        {
            "name": "Natalie Wong",
            "title": "Marketing Coordinator",
            "industry": "Advertising",
            "salary": "62000",
        },
        {
            "name": "Christopher Evans",
            "title": "Chief Technology Officer",
            "industry": "Technology",
            "salary": "185000",
        },
        {
            "name": "Samantha Miller",
            "title": "Content Strategist",
            "industry": "Media",
            "salary": "72000",
        },
        {
            "name": "Ryan Patel",
            "title": "Business Analyst",
            "industry": "Consulting",
            "salary": "79000",
        },
        {
            "name": "Jennifer Moore",
            "title": "UX Designer",
            "industry": "Technology",
            "salary": "89000",
        },
        {
            "name": "Matthew Clark",
            "title": "Investment Banker",
            "industry": "Finance",
            "salary": "150000",
        },
        {
            "name": "Elizabeth Harris",
            "title": "Clinical Researcher",
            "industry": "Healthcare",
            "salary": "93000",
        },
        {
            "name": "Anthony Nguyen",
            "title": "Supply Chain Manager",
            "industry": "Logistics",
            "salary": "84000",
        },
        {
            "name": "Grace Thompson",
            "title": "Public Relations Specialist",
            "industry": "Media",
            "salary": "67500",
        },
        {
            "name": "Joseph White",
            "title": "Systems Administrator",
            "industry": "Technology",
            "salary": "78000",
        },
        {
            "name": "Madison Lewis",
            "title": "Compliance Officer",
            "industry": "Banking",
            "salary": "96000",
        },
        {
            "name": "Brandon Scott",
            "title": "Civil Engineer",
            "industry": "Engineering",
            "salary": "91000",
        },
        {
            "name": "Ava Robinson",
            "title": "Social Media Manager",
            "industry": "Advertising",
            "salary": "68000",
        },
        {
            "name": "Kevin Adams",
            "title": "Executive Chef",
            "industry": "Hospitality",
            "salary": "72500",
        },
        {
            "name": "Rachel Young",
            "title": "Elementary Teacher",
            "industry": "Education",
            "salary": "58000",
        },
        {
            "name": "Justin Ross",
            "title": "Insurance Agent",
            "industry": "Insurance",
            "salary": "65500",
        },
        {
            "name": "Michelle Bennett",
            "title": "Pharmacy Manager",
            "industry": "Healthcare",
            "salary": "112000",
        },
    ]
    actual = read_csv("data/salaries.csv")
    print(actual)
    assert actual == expected
