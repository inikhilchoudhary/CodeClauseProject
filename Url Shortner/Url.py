import pyshorteners

# Create a Shortener object
s = pyshorteners.Shortener()

# Input the long URL
long_url = input("Enter the long URL: ")

# Shorten the URL
short_url = s.tinyurl.short(long_url)

# Display the shortened URL
print("Shortened URL:", short_url)
