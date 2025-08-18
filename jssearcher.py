import requests
import sys
import pyfiglet
import re

def search_in_file(url, hints, output_file):
    matches_found = 0
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            lines = response.text.splitlines()
           
            patterns = [r'\b' + re.escape(hint.strip()) + r'\b' for hint in hints]
            combined_pattern = '|'.join(patterns)

            for i, line in enumerate(lines):
                if re.search(combined_pattern, line, flags=re.IGNORECASE):
                    start = max(i - 4, 0)
                    end = min(i + 5, len(lines))
                    snippet = lines[start:end]

                  
                    highlighted = snippet[:]
                    for hint in hints:
                        highlighted = [re.sub(r'\b' + re.escape(hint.strip()) + r'\b', 
                                    f"\033[91m{hint.strip()}\033[0m", 
                                    l, flags=re.IGNORECASE) for l in highlighted]

                   
                    print(f"\n[+] Match found in: {url} (line {i+1})")
                    print("\n".join(highlighted))
                    print("=" * 80)

                   
                    with open(output_file, "a") as f:
                        f.write(f"\n[+] Match found in: {url} (line {i+1})\n")
                        f.write("\n".join(snippet) + "\n")
                        f.write("=" * 80 + "\n")

                    matches_found += 1

            return matches_found
        else:
            print(f"[-] Failed to fetch {url}: Status code {response.status_code}")
            with open(output_file, "a") as f:
                f.write(f"[-] Failed to fetch {url}: Status code {response.status_code}\n")
            return 0
    except Exception as e:
        print(f"[-] Error accessing {url}: {str(e)}")
        with open(output_file, "a") as f:
            f.write(f"[-] Error accessing {url}: {str(e)}\n")
        return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 jssearcher.py <js_links_file>")
        return

    # Banner
    ascii_banner = pyfiglet.figlet_format("JSSEARCHER", font="slant")
    print(ascii_banner)
    print("author: adham heinrich\n")

    # Load file
    file_path = sys.argv[1]
    try:
        with open(file_path, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[-] Error reading file {file_path}: {str(e)}")
        return

    print(f"Loaded {len(urls)} JS links.\n")

    # Ask for hints
    hint_input = input("Enter your hints (comma-separated, e.g., promo,coupon,credentials): ").strip()
    hints = [h.strip() for h in hint_input.split(",") if h.strip()]

    if not hints:
        print("[-] No valid hints provided. Exiting...")
        return

    # Ask for output file
    output_file = input("Enter the output file name (e.g., results.txt): ").strip()
    if not output_file:
        print("[-] No valid output file name provided. Exiting...")
        return

    # Clear the output file if it exists
    try:
        with open(output_file, "w") as f:
            f.write(f"JSSEARCHER Results\n")
            f.write(f"Searching for: {', '.join(hints)}\n\n")
    except Exception as e:
        print(f"[-] Error creating output file {output_file}: {str(e)}")
        return

    print(f"\nSearching for: {', '.join(hints)}\n")

    total_matches = 0
    for url in urls:
        matches = search_in_file(url, hints, output_file)
        total_matches += matches

    print(f"\n[+] Done! Total matches found: {total_matches}")
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()
