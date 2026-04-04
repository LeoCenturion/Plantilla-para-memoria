import argparse
import os
import re
from google import genai
from google.genai import types

def parse_rules(rules_path):
    with open(rules_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rules = re.split(r'\n', content)
    return [rule.strip() for rule in rules if rule.strip()]

def evaluate_document(rules_file, target_file, model_name):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable is not set.")
        return

    client = genai.Client(api_key=api_key)

    rules = parse_rules(rules_file)
    if not rules:
        print("No rules found in the rules file.")
        return

    print(f"Uploading '{target_file}' to Gemini...")
    try:
        uploaded_file = client.files.upload(
            file=target_file,
            config=types.UploadFileConfig(mime_type="text/plain")
        )
    except Exception as e:
        print(f"Failed to upload file: {e}")
        return

    print("Creating Context Cache...")
    try:
        cache = client.caches.create(
            model=model_name,
            config=types.CreateCachedContentConfig(
                contents=[uploaded_file],
                ttl="900s" 
            )
        )
    except Exception as e:
        print(f"Failed to create cache: {e}")
        client.files.delete(name=uploaded_file.name)
        return

    print("Starting evaluation...\n")
    
    generate_config = types.GenerateContentConfig(
        cached_content=cache.name,
        temperature=0.1 
    )

    try:
        for i, rule in enumerate(rules, 1):
            print(f"{'='*50}")
            print(f"Evaluating Rule {i}/{len(rules)}")
            print(f"Rule: {rule}")
            print(f"{'-'*50}")
            
            prompt = f"Please review the cached document and determine if it complies with the following rule.\n\nRule:\n{rule}\n\nState clearly whether the document complies with the rule or not, followed by a brief justification."
            
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config=generate_config
                )
                print("Gemini Output:")
                print(response.text.strip())
            except Exception as e:
                print(f"Failed to evaluate rule {i}: {e}")
            
            print(f"{'='*50}\n")
            
    finally:
        print("Cleaning up resources...")
        try:
            client.caches.delete(name=cache.name)
            client.files.delete(name=uploaded_file.name)
            print("Cleanup complete.")
        except Exception as e:
            print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a document against rules using the new google-genai Context Caching.")
    parser.add_argument("rules_file", help="Path to the rules file")
    parser.add_argument("target_file", help="Path to the document file")
    parser.add_argument("--model", type=str, default="gemini-2.5-flash", help="Model name (default: gemini-2.5-flash)")
    
    args = parser.parse_args()
    evaluate_document(args.rules_file, args.target_file, args.model)
