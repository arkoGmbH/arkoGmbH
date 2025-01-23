import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Start')  # Press Ctrl+F8 to toggle the breakpoint.
    url = 'https://pmarko.pythonanywhere.com/create_user'
    payload={'first_name':'Petsdfgaafadaa','last_name':'Psgfaf','save':'save'}
    r=requests.get(url, payload)
    if r.status_code == 200:
        print("Success!")
    elif r.status_code == 404:
        print("Not Found.")
    print(r.request.url)
    print(f'End')

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
