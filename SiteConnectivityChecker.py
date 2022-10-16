#import urlib
#use urlib.request to get the data from the url
#write a function that takes a url
#return a response


from urllib import response
import urllib.request as urllib

def main(url):
    print("Checking connectivity ")
    response = urllib.urlopen(url)
    print(f"Connected to {url} succesfully")
    print(f"The response code was: {response.getcode()}")


if __name__ == "__main__":
    print("This is a site connectivity checker program")
    input_url = input("Input the url of the site: ")
    main(input_url)