import json

with open("./config/stratus-docs-pages.json") as pages_config:
    pages_config_json = json.loads(pages_config.read())

for p in pages_config_json["pages"]:
    new_hugo_lines = [
        '---\n',
        'title: "{}"\n'.format(p['title']),
        'linkTitle: "{}"\n'.format(p['linkTitle']),
        'date: "{}"\n'.format(p['date']),
        'weight: "{}"\n'.format(p['weight']),
        'description: "{}"\n'.format(p['description']),
        '---\n\n'
    ]

    with open(p["path"], "r+") as doc_file:
        original_lines = doc_file.readlines()
        new_lines = new_hugo_lines + original_lines
        doc_file.seek(0)
        doc_file.writelines(new_lines)
