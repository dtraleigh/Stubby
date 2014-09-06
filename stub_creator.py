#////
#Script to ask a user a few things and then create a media stub for Kodi
#\\\\
import os

def new_stub_or_quit():
    answer = raw_input('Create new media stub? (Y or N): ')
    
    if answer == 'Y' or answer == 'y':
        return True
    elif answer == 'N' or answer == 'n':
        return False

def enter_year():
    year = ''
    while(len(year) != 4):
        year = raw_input('What year was it released? (4 digits): ')
        
    return year
        
def enter_movie_type():
    movie_type = ''
    while(movie_type != '1' and movie_type != '2' and movie_type != '3'):
        movie_type = raw_input('DVD (1), BLURAY (2), or HDDVD (3)?: ')
        
    if movie_type == '1':
        movie_type = 'DVD'
    elif movie_type == '2':
        movie_type = 'BLURAY'
    elif movie_type == '3':
        movie_type = 'HDDVD'
        
    return movie_type

def create_stub_content(title, movie_type):
    # <discstub><title>Title</title></discstub>
    stub = '<discstub><title>' + title + ' (' + movie_type + ')</title></discstub>'
    
    return stub

def ask_and_create():
    title = raw_input('What is the movie title?: ')
    year = enter_year()
    movie_type = enter_movie_type()
    
    stub_content = create_stub_content(title, movie_type)
    
    filename = title + ' (' + year + ').' + movie_type + '.disc'
    sub_dir = 'output/'
    
    the_file = open(os.path.join(sub_dir, filename), 'w')
    the_file.write(stub_content)
    the_file.close()

user_input = new_stub_or_quit()

while user_input:
    ask_and_create()
    user_input = new_stub_or_quit()