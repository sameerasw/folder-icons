import os

PNGs_DIR = 'PNGs'
README_FILE = 'README.md'
ICON_SIZE = 50  # Define the size of the icons

def generate_icon_markdown(image_path):
    return f'<img src="/{image_path}" width="{ICON_SIZE}" height="{ICON_SIZE}">'

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
                readme_file.write('\n'.join([' '.join(icons[i:i+10]) for i in range(0, len(icons), 10)]))
                readme_file.write('\n<!-- ICONS_GRID_END -->')
                break

if __name__ == '__main__':
    update_readme_with_icons()
