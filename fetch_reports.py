import requests
import argparse
import sys

# Function to check the status code of URLs and print verbose status and completion percentage
def check_urls(start, end):
    total_urls = end - start + 1
    processed_urls = 0
    
    # Open a file to save URLs with a 200 status code
    with open("urls_with_200_status.txt", "w") as file:
        for i in range(start, end + 1):
            url = f"https://hackerone.com/reports/{i}"
            processed_urls += 1
            try:
                # Send a GET request to the URL
                response = requests.get(url)
                
                # Check if status code is 200 (OK)
                if response.status_code == 200:
                    file.write(url + "\n")  # Save the URL to the text file only if status is 200
                    print(f"URL: {url} - Status: 200 OK")
                else:
                    print(f"URL: {url} - Status: {response.status_code}")
            
            except requests.exceptions.RequestException as e:
                # Handle any exception that occurs during the request
                print(f"Error with URL {url}: {e}")
            
            # Calculate and print the percentage of completion
            percent_complete = (processed_urls / total_urls) * 100
            sys.stdout.write(f"\rProgress: {processed_urls}/{total_urls} ({percent_complete:.2f}%)")
            sys.stdout.flush()
        
        # Ensure to print the completion message once the loop finishes
        print("\nProcessing complete. Check 'urls_with_200_status.txt' for the results.")

# Set up argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description="Check the status codes of URLs and save those with status 200.")
    parser.add_argument("start", type=int, help="The starting number in the URL")
    parser.add_argument("end", type=int, help="The ending number in the URL")
    
    return parser.parse_args()

# Main function
def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Call the function with the provided start and end numbers
    check_urls(args.start, args.end)

if __name__ == "__main__":
    main()
