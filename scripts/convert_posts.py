#!/usr/bin/env python3
"""Convert WordPress-style blog posts to Hugo/Blowfish format."""

import os
import re
import shutil
import glob
import yaml

BLOG_DIR = "/mnt/c/Users/lionelgurret/projects/website/blog"
HUGO_POSTS = "/mnt/c/Users/lionelgurret/projects/website/thedevopsrunner/content/posts"
IMAGES_DIR = os.path.join(BLOG_DIR, "_images")

# Mapping of article numbers to approximate dates (from post names + context)
# Articles without explicit post_date need estimated dates
ESTIMATED_DATES = {
    "002": "2023-06-15",  # DevOps Days Zurich 2023
    "003": "2023-06-22",  # KCD Zurich 2023
    "004": "2023-07-15",  # Velero backup
    "005": "2023-10-01",  # Azure Updates September 2023
    "006": "2023-10-15",  # AKS FinOps
    "007": "2023-11-01",  # Azure Updates October 2023
    "008": "2023-11-15",  # AKS Workload Identities
    "009": "2023-12-01",  # Azure Updates November 2023
    "010": "2024-01-01",  # Azure Updates December 2023
    "011": "2024-01-15",  # New YouTube Channel
    "012": "2024-01-20",  # MCT Summit 2024
    "013": "2024-02-01",  # Azure Updates January 2024
    "014": "2024-03-01",  # Azure Updates February 2024
    "015": "2024-04-01",  # Azure Updates March 2024
    "016": "2024-05-01",  # Azure Updates April 2024
    "017": "2024-05-15",  # AZ-900 Series
    "018": "2024-06-01",  # Azure Updates May 2024
    "019": "2024-07-01",  # Azure Updates June 2024
    "020": "2024-08-01",  # Azure Updates July 2024
    "021": "2024-08-15",  # AI-900 Series
    "022": "2024-09-01",  # Azure Updates August 2024
    "023": "2024-10-01",  # Azure Updates September 2024
    "024": "2024-10-15",  # VMware Azure Migration
    "025": "2024-11-01",  # Azure Updates October 2024 (has post_date)
    "026": "2024-11-15",  # Azure AI Tour Bern
    "027": "2024-12-01",  # Azure Updates November 2024
    "028": "2024-12-03",  # OCP Cloud Business Breakfast (has post_date)
    "029": "2025-01-01",  # Azure Updates December 2024
    "030": "2025-02-01",  # Azure Updates January 2025
    "031": "2025-03-01",  # Azure Updates February 2025
    "032": "2025-03-15",  # Azure AI Tour Zurich
    "033": "2025-04-01",  # Azure Updates March 2025
    "034": "2025-05-01",  # Azure Updates April 2025
    "035": "2025-06-01",  # Azure Updates May 2025
    "036": "2025-06-15",  # Azure AI Tour Lausanne
    "037": "2025-07-01",  # Azure Updates June 2025
    "038": "2025-08-01",  # Azure Updates July 2025
    "039": "2025-09-01",  # Azure Updates August 2025
    "040": "2025-10-01",  # Azure Updates September 2025
    "041": "2025-11-01",  # Azure Updates October 2025
    "042": "2025-12-01",  # Azure Updates November 2025
    "043": "2026-01-01",  # Azure Updates December 2025
}


def find_content_file(article_dir):
    """Find the actual content .md file (not index.md)."""
    md_files = glob.glob(os.path.join(article_dir, "*.md"))
    content_files = [f for f in md_files if os.path.basename(f) != "index.md"]
    if not content_files:
        return None
    # If multiple, pick the largest one
    if len(content_files) > 1:
        content_files.sort(key=lambda f: os.path.getsize(f), reverse=True)
    return content_files[0]


def parse_front_matter(content):
    """Parse YAML front matter and return (metadata_dict, body)."""
    if not content.startswith("---"):
        return {}, content
    
    end = content.find("---", 3)
    if end == -1:
        return {}, content
    
    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()
    
    # Remove comment lines from front matter for YAML parsing
    fm_lines = []
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        # Keep the line
        fm_lines.append(line)
    
    fm_clean = "\n".join(fm_lines)
    
    try:
        metadata = yaml.safe_load(fm_clean) or {}
    except yaml.YAMLError:
        metadata = {}
        # Try to extract title at minimum
        title_match = re.search(r'title:\s*"(.+?)"', fm_clean)
        if title_match:
            metadata["title"] = title_match.group(1)
    
    return metadata, body


def slugify(title):
    """Create a URL-friendly slug from a title."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug


def convert_body(body, article_num, dest_dir):
    """Convert WordPress HTML patterns to clean Hugo markdown."""
    
    # Remove author attribution line
    body = re.sub(
        r'By\s*<span[^>]*>\[.*?\]\(https?://(?:www\.)?linkedin\.com/[^)]*\)</span>\.?\s*\n?',
        '', body
    )
    body = re.sub(
        r'By\s*<span[^>]*>\[.*?\]\(https?://(?:www\.)?linkedin\.com/[^)]*\)\s*(?:and\s*<span[^>]*>\[.*?\]\(https?://(?:www\.)?linkedin\.com/[^)]*\)</span>)?\.?\s*\n?',
        '', body
    )
    
    # Remove commented-out HTML img tags
    body = re.sub(r'<!--\s*<img[^>]*>\s*-->\s*\n?', '', body)
    
    # Convert centered image spans to plain markdown images
    # Pattern: <span style="display:block;text-align:center">![alt](path)</span>
    def convert_image(match):
        alt = match.group(1) or ""
        img_path = match.group(2)
        # Convert image path
        new_path = remap_image_path(img_path, article_num, dest_dir)
        return f"![{alt}]({new_path})"
    
    body = re.sub(
        r'<span[^>]*style="display:block;text-align:center"[^>]*>!\[([^\]]*)\]\(([^)]+)\)</span>',
        convert_image,
        body
    )
    
    # Also handle images not in spans but with /_images paths
    def convert_standalone_image(match):
        full = match.group(0)
        alt = match.group(1)
        img_path = match.group(2)
        if "/_images/" in img_path or "_images/" in img_path:
            new_path = remap_image_path(img_path, article_num, dest_dir)
            return f"![{alt}]({new_path})"
        return full
    
    body = re.sub(
        r'!\[([^\]]*)\]\((/_images/[^)]+)\)',
        convert_standalone_image,
        body
    )
    
    # Convert YouTube thumbnail links to Hugo shortcode
    def convert_youtube(match):
        video_id = match.group(1)
        return f'{{{{< youtube {video_id} >}}}}'
    
    body = re.sub(
        r'\[!\[.*?\]\(https://img\.youtube\.com/vi/([^/]+)/[^)]*\)\]\(https://(?:www\.)?youtube\.com/watch\?v=\1\)',
        convert_youtube,
        body
    )
    
    # Clean up excessive blank lines
    body = re.sub(r'\n{3,}', '\n\n', body)
    
    return body.strip()


def remap_image_path(img_path, article_num, dest_dir):
    """Remap image path from WordPress to local and copy the file."""
    # Normalize path
    img_path = img_path.lstrip("/")
    
    # Determine source path
    source_path = os.path.join(BLOG_DIR, img_path)
    
    if not os.path.exists(source_path):
        # Try alternate patterns
        # e.g., _images/002_lionel.jpg (flat) vs _images/002/002_lionel.jpg
        print(f"  WARNING: Image not found: {source_path}")
        return os.path.basename(img_path)
    
    # Copy to destination
    filename = os.path.basename(img_path)
    dest_path = os.path.join(dest_dir, filename)
    
    if not os.path.exists(dest_path):
        shutil.copy2(source_path, dest_path)
    
    return filename


def convert_article(article_dir, article_num):
    """Convert a single article to Hugo format."""
    content_file = find_content_file(article_dir)
    if not content_file:
        print(f"  SKIP: No content file found in {article_dir}")
        return False
    
    with open(content_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    metadata, body = parse_front_matter(content)
    
    if not metadata.get("title"):
        print(f"  SKIP: No title found in {content_file}")
        return False
    
    title = metadata["title"]
    slug = slugify(title)
    
    # Truncate slug if too long
    if len(slug) > 80:
        slug = slug[:80].rstrip('-')
    
    dest_dir = os.path.join(HUGO_POSTS, slug)
    os.makedirs(dest_dir, exist_ok=True)
    
    # Extract metadata
    date = ESTIMATED_DATES.get(article_num, "2024-01-01")
    
    # Check for explicit post_date
    if metadata.get("post_date"):
        date_str = str(metadata["post_date"])
        date_match = re.match(r'(\d{4}-\d{2}-\d{2})', date_str)
        if date_match:
            date = date_match.group(1)
    
    categories = []
    tags = []
    if isinstance(metadata.get("taxonomy"), dict):
        cats = metadata["taxonomy"].get("category", [])
        if isinstance(cats, list):
            categories = cats
        tag_list = metadata["taxonomy"].get("post_tag", [])
        if isinstance(tag_list, list):
            tags = tag_list
    
    description = metadata.get("description", "")
    if isinstance(description, type(None)):
        description = ""
    
    # Handle featured image
    featured_image = metadata.get("featured_image", "")
    if featured_image:
        feat_filename = remap_image_path(featured_image, article_num, dest_dir)
        # Rename to featured.xxx for Blowfish theme
        ext = os.path.splitext(feat_filename)[1]
        featured_dest = os.path.join(dest_dir, f"featured{ext}")
        feat_source = os.path.join(dest_dir, feat_filename)
        if os.path.exists(feat_source) and not os.path.exists(featured_dest):
            shutil.move(feat_source, featured_dest)
    
    # Convert body
    converted_body = convert_body(body, article_num, dest_dir)
    
    # Build Hugo front matter
    hugo_fm = f"""---
title: "{title.replace('"', '\\"')}"
date: {date}
draft: false
description: "{description.replace('"', '\\"') if description else ''}"
tags: {tags}
categories: {categories}
showAuthor: true
authors:
  - "lionelgurret"
---"""
    
    # Write Hugo post
    output = f"{hugo_fm}\n\n{converted_body}\n"
    
    index_path = os.path.join(dest_dir, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(output)
    
    print(f"  OK: {title[:60]}... -> {slug}/")
    return True


def main():
    # Skip 001 (already converted)
    dirs = sorted(glob.glob(os.path.join(BLOG_DIR, "[0-9][0-9][0-9]_*")))
    
    converted = 0
    skipped = 0
    
    for article_dir in dirs:
        dirname = os.path.basename(article_dir)
        article_num = dirname[:3]
        
        # Skip 001 (already done manually)
        if article_num == "001":
            print(f"[{article_num}] SKIP (already converted)")
            skipped += 1
            continue
        
        print(f"[{article_num}] Converting...")
        
        if convert_article(article_dir, article_num):
            converted += 1
        else:
            skipped += 1
    
    print(f"\nDone! Converted: {converted}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
