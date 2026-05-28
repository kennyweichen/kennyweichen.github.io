#!/usr/bin/env python3
"""
Migration script: Convert Jekyll posts to Quarto format
This script converts front matter and moves posts from _posts/ to blog/
"""

import os
import re
import shutil
import sys
from pathlib import Path
from datetime import datetime

def convert_front_matter(content):
    """Convert Jekyll front matter to Quarto format"""
    if not content.startswith('---'):
        return content

    # Extract front matter
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return content

    jekyll_fm = match.group(1)
    body = match.group(2)

    # Parse Jekyll front matter
    jekyll_dict = {}
    for line in jekyll_fm.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            jekyll_dict[key.strip()] = value.strip()

    # Build Quarto front matter
    quarto_fm = {}

    if 'title' in jekyll_dict:
        quarto_fm['title'] = jekyll_dict['title']

    if 'category' in jekyll_dict:
        quarto_fm['categories'] = [jekyll_dict['category']]

    if 'full_width' in jekyll_dict:
        quarto_fm['full-width'] = jekyll_dict['full_width'].lower() == 'true'

    # Extract date from front matter or filename
    # Will be passed separately

    # Build YAML front matter
    yaml_lines = ['---']
    for key, value in quarto_fm.items():
        if isinstance(value, bool):
            yaml_lines.append(f'{key}: {str(value).lower()}')
        elif isinstance(value, list):
            yaml_lines.append(f'{key}:')
            for item in value:
                yaml_lines.append(f'  - {item}')
        else:
            yaml_lines.append(f'{key}: {value}')
    yaml_lines.append('---')

    new_content = '\n'.join(yaml_lines) + '\n' + body
    return new_content

def extract_date_from_filename(filename):
    """Extract date from Jekyll filename format: YYYY-MM-DD-title"""
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-(.+)\.(md|html)$', filename)
    if match:
        return f'{match.group(1)}-{match.group(2)}-{match.group(3)}'
    return None

def migrate_posts(jekyll_posts_dir, quarto_blog_dir):
    """Migrate all posts from Jekyll to Quarto"""

    jekyll_path = Path(jekyll_posts_dir)
    blog_path = Path(quarto_blog_dir)

    if not jekyll_path.exists():
        print(f"Error: {jekyll_posts_dir} does not exist")
        return False

    # Create blog directory if it doesn't exist
    blog_path.mkdir(parents=True, exist_ok=True)

    posts = list(jekyll_path.glob('*'))
    posts.sort()

    print(f"Found {len(posts)} posts to migrate\n")

    migrated = 0
    failed = []

    for post_file in posts:
        if post_file.name.startswith('.'):
            continue

        try:
            print(f"Migrating {post_file.name}...", end=" ")

            # Read content
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Convert front matter
            converted = convert_front_matter(content)

            # Extract date and prepare new filename
            date_str = extract_date_from_filename(post_file.name)
            if date_str:
                # For Quarto, use the pattern: YYYY-MM-DD-title.qmd
                title_part = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', post_file.stem)
                new_filename = f"{date_str}-{title_part}.qmd"
            else:
                # Fallback: just change extension
                new_filename = post_file.stem + '.qmd'

            # Write to blog directory
            new_path = blog_path / new_filename
            with open(new_path, 'w', encoding='utf-8') as f:
                f.write(converted)

            print("✓")
            migrated += 1

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            failed.append((post_file.name, str(e)))

    print(f"\n\nMigration Summary:")
    print(f"  Successfully migrated: {migrated} posts")
    if failed:
        print(f"  Failed: {len(failed)} posts")
        for name, error in failed:
            print(f"    - {name}: {error}")

    return len(failed) == 0

if __name__ == '__main__':
    jekyll_dir = '/Users/kennychen/kennyweichen.github.io/_posts'
    quarto_dir = '/Users/kennychen/kennyweichen.github.io/blog'

    success = migrate_posts(jekyll_dir, quarto_dir)
    sys.exit(0 if success else 1)
