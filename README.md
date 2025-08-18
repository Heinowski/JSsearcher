JSSearcher

JSSearcher is a Python-based tool designed to search for specific keywords within JavaScript files hosted online. It fetches JS files from provided URLs, searches for user-defined keywords, and returns snippets of code (4 lines before and after each match) with highlighted keywords in the terminal output. Results are also saved to a user-specified output file for further analysis.

Features
.Search for multiple keywords (comma-separated) in JavaScript files.
.Display matches with highlighted keywords in red (terminal output).
.Save results to a text file, including the URL, line number, and code snippet.
.Handle errors gracefully (e.g., invalid URLs or failed requests).
.Provide a summary of total matches found.

Prerequisites

Before running JSSearcher, ensure you have the following installed:

Python 3.x

Required Python packages (listed in requirements.txt):

Install the required packages using:

pip install -r requirements.txt


Installation:

Clone the repository:

git clone https://github.com/Heinowski/Jssearcher.git

Navigate to the project directory:

cd jssearcher
Install the required dependencies:

pip install -r requirements.txt

Usage

Prepare a file with JS URLs: Create a text file (e.g., jsfiles.txt) and add URLs of JavaScript files, one per line. Example:

https://example.com/script1.js
https://example.com/script2.js



Run the tool:

python3 jssearcher.py jsfiles.txt



Enter keywords: When prompted, enter the keywords to search for, separated by commas (e.g., promo,coupon,credentials):

Enter your hints (comma-separated, e.g., promo,coupon,credentials): promo,coupon,credentials



Specify output file: Enter the name of the file where results will be saved (e.g., results.txt):

Enter the output file name (e.g., results.txt): results.txt



View results:


The tool will display matches in the terminal with keywords highlighted in red.



Results (including errors) are saved to the specified output file.

Example Output

Terminal Output:

   ____ ___  ___  ____ ___  ___ _          
  / ___/ _ \|  _ \| ___|_ _|___ \ ___  ___ 
 | |  | | | | | | |___ \| |  __) / __|/ __|
 | |__| |_| | |_| |___) | | / __/\__ \ (__ 
  \____\___/|____/|____/___|_____|___/\___|

author: adham heinrich

Loaded 2 JS links.

Enter your hints (comma-separated, e.g., promo,coupon,credentials): promo,coupon
Enter the output file name (e.g., results.txt): results.txt

Searching for: promo, coupon

[+] Match found in: https://example.com/script.js (line 123)
[4 lines before]
function getDiscount() { return promo; }
[4 lines after]
================================================================================

[+] Done! Total matches found: 1
Results saved to: results.txt

Output File (results.txt):

JSSEARCHER Results
Searching for: promo, coupon

[+] Match found in: https://example.com/script.js (line 123)
[4 lines before]
function getDiscount() { return promo; }
[4 lines after]
================================================================================

Notes

Ensure the URLs in your input file are valid and accessible.



Keywords are case-insensitive and must be whole words (e.g., promo won't match promotion).



The output file is overwritten each time the tool runs.



For large lists of URLs, the tool may take some time depending on network speed.

Contributing

Feel free to submit issues or pull requests to improve JSSearcher. Contributions are welcome!

