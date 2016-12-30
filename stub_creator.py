#////
#Script to ask a user a few things and then create a media stub for Kodi
#\\\\
import os

def new_stub_or_quit():
    answer = ''
    while (answer != 'y' and answer != 'Y' and answer != 'n' and answer != 'N'):
        answer = input('Create new media stub? (Y or N): ')

    if answer == 'Y' or answer == 'y':
        return True
    elif answer == 'N' or answer == 'n':
        return False

def enter_year():
    year = ''
    while(len(year) != 4):
        year = input('What year was it released? (4 digits): ')

    return year

def enter_movie_type():
    movie_type = ''
    while(movie_type != '1' and movie_type != '2' and movie_type != '3' and movie_type != '4' and movie_type != '5'):
        movie_type = input('DVD (1), BLURAY (2),  HDDVD (3), TV (4), or VHS (5)?: ')

    if movie_type == '1':
        movie_type = 'DVD'
    elif movie_type == '2':
        movie_type = 'BLURAY'
    elif movie_type == '3':
        movie_type = 'HDDVD'
    elif movie_type == '4':
        movie_type = 'TV'
    elif movie_type == '5':
        movie_type = 'VHS'

    return movie_type

def add_message():
    answer = ''
    while (answer != 'y' and answer != 'Y' and answer != 'n' and answer != 'N'):
        answer = input('Add a message to the media stub? (Y or N): ')

    if answer == 'Y' or answer == 'y':
        message = input('Please type your message: ')
        return message
    elif answer == 'N' or answer == 'n':
        return False

def create_stub_content(title, movie_type):
    #<discstub>
    #    <title>Title (year)</title>
    #    <message>Message to be displayed</message>
    #</discstub>
    indent = '    '

    message = add_message()

    stub = '<discstub>\n'
    stub = stub + indent + '<title>' + title + ' (' + movie_type + ')</title>\n'
    if message:
        stub = stub + indent + '<message>' + message + '</message>\n'
    stub = stub + '</discstub>\n'

    return stub

def ask_and_create():
    title = input('What is the movie title?: ')
    year = enter_year()
    movie_type = enter_movie_type()

    stub_content = create_stub_content(title, movie_type)

    filename = title + ' (' + year + ').' + movie_type + '.disc'

    #////
    #Change your desired path here
    #\\\\
    sub_dir = '../Movies/'

    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)

    the_file = open(os.path.join(sub_dir, filename), 'w')
    the_file.write(stub_content)
    the_file.close()

    print('\nCreated file: "' + filename + '\"')
    print(stub_content)

clear = lambda: os.system('cls')
clear()

try:
    input = raw_input
except NameError:
    pass

user_input = new_stub_or_quit()

while user_input:
    ask_and_create()
    user_input = new_stub_or_quit()
    clear()
