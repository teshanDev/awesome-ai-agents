import json
import os
import sys
from datetime import datetime

def add_post(title, content, file_path="posts.json"):
    # Ensure file exists
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([], f)
            
    # Read existing
    try:
        with open(file_path, 'r') as f:
            posts = json.load(f)
    except json.JSONDecodeError:
        posts = []
        
    # Create new post
    new_post = {
        "title": title,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    
    # Append and save
    posts.append(new_post)
    with open(file_path, 'w') as f:
        json.dump(posts, f, indent=4)
        
    print(f"Successfully added post: '{title}' at {new_post['timestamp']}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python add_post.py \"Title\" \"Content\"")
        sys.exit(1)
        
    title = sys.argv[1]
    content = sys.argv[2]
    
    # Run from the correct directory relative to the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "posts.json")
    
    add_post(title, content, json_path)
