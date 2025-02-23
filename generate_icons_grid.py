import os

PNGs_DIR = 'PNGs'
README_FILE = 'README.md'

def generate_icon_markdown(image_path):
    return f'![{os.path.basename(image_path)}](/{image_path})'

def update_readme_with_icons():
    icons = []
    for root, _, files in os.walk(PNGs_DIR):
        for file in files:
            if file.endswith('.png'):
                icons.append(generate_icon_markdown(os.path.join(root, file)))

    with open(README_FILE, 'r') as readme_file:
        lines = readme_file.readlines()

    with open(README_FILE, 'w') as readme_file:
        for line in lines:
            readme_file.write(line)
            if line.strip() == '<!-- ICONS_GRID_START -->':
                for icon in icons:
                    readme_file.write(icon + ' ')
                readme_file.write('\n<!-- ICONS_GRID_END -->')
                break

if __name__ == '__main__':
    update_readme_with_icons()
