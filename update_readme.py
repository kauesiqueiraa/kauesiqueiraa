import requests
import datetime

USERNAME = "kauesiqueiraa"
TEMPLATE_FILE = "README-template.md"
OUTPUT_FILE = "README.md"

def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?sort=updated"
    repos = requests.get(url).json()

    formatted = ""
    count = 0

    for r in repos:
        if r["fork"]:
            continue

        formatted += f"- [{r['name']}]({r['html_url']}) — {r.get('description','No description')}\n"
        count += 1

        if count == 5:
            break

    return formatted


def get_stats():
    stats = f"""
![Profile Views](https://komarev.com/ghpvc/?username={USERNAME})
![GitHub Stats](https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&theme=transparent)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&theme=transparent)
"""
    return stats


def main():
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    projects = get_repos()
    stats = get_stats()

    final = template.replace("{{PROJECTS}}", projects)
    final = final.replace("{{STATS}}", stats)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final)

    print("README.md atualizado!")


if __name__ == "__main__":
    main()
