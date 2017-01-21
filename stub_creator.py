#////
#Script to ask a user a few things and then create a media stub for Kodi
#\\\\
import os

class new_media_stub():

    def __init__(self):
        self.sub_dir = "../Movies/"
        self.title = ""
        self.year = ""
        self.type = ""
        self.message = ""

    def instructions(self):
        menu = "Stub Creator 'Stubby' | Welcome!\n"
        menu += "   Menu\n"
        menu += "      (s) - Set media stub output path.\n"
        menu += "      (c) - Create new media stub.\n"
        menu += "      (q) - Quit.\n\n"
        menu += "   Output Folder: " + self.sub_dir + "\n"

        return menu

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def change_output_folder(self):
        self.sub_dir = input("Enter output dir (. for current, .. for up one level, etc.): ")
        self.clear_screen()

    def new_stub_or_quit(self):
        print(self.instructions())

        valid_answers = ["S", "s", "C", "c", "Q", "q"]

        answer = ""
        while (answer not in valid_answers):
            answer = input("Talk to me: ")

        if answer == "C" or answer == "c":
            return "c"
        elif answer == "S" or answer == "s":
            return "s"
        elif answer == "Q" or answer == "q":
            return False

    def get_title(self):
        self.title = input("What is the movie title?: ")

    def get_year(self):
        while(len(self.year) != 4):
            self.year = input("What year was it released? (4 digits): ")

    def get_type(self):
        valid_choices = ["1", "2", "3", "4", "5"]

        movie_type = ""
        while(movie_type not in valid_choices):
            movie_type = input("DVD (1), BLURAY (2),  HDDVD (3), TV (4), or VHS (5)?: ")

        if movie_type == "1":
            self.type = "DVD"
        elif movie_type == "2":
            self.type = "BLURAY"
        elif movie_type == "3":
            self.type = "HDDVD"
        elif movie_type == "4":
            self.type = "TV"
        elif movie_type == "5":
            self.type = "VHS"

    def get_message(self):
        valid_choices = ["Y", "y", "N", "n"]

        answer = ""
        while (answer not in valid_choices):
            answer = input("Add a message to the media stub? (Y or N): ")

        if answer == "Y" or answer == "y":
            self.message = input("Please type your message: ")

    def create_stub_content(self):
        #<discstub>
        #    <title>Title (year)</title>
        #    <message>Message to be displayed</message>
        #</discstub>
        indent = "    "

        stub = "<discstub>\n"
        stub = stub + indent + "<title>" + self.title + " (" + self.type + ")</title>\n"
        if self.message != "":
            stub = stub + indent + "<message>" + self.message + "</message>\n"
        stub = stub + "</discstub>\n"

        return stub

    def ask_and_create(self):
        self.get_title()
        self.get_year()
        self.get_type()
        self.get_message()

        stub_content = self.create_stub_content()

        filename = self.title + " (" + self.year + ")." + self.type + ".disc"

        if not os.path.exists(self.sub_dir):
            os.makedirs(self.sub_dir)

        the_file = open(os.path.join(self.sub_dir, filename), "w")
        the_file.write(stub_content)
        the_file.close()

        print('\nCreated file: "' + filename + '\"')
        print(stub_content)


try:
    input = raw_input
except NameError:
    pass

media_stub = new_media_stub()
user_input = media_stub.new_stub_or_quit()

while user_input != False:
    if user_input == "c":
        media_stub = new_media_stub()
        media_stub.ask_and_create()
    elif user_input == "s":
        media_stub.change_output_folder()
    user_input = media_stub.new_stub_or_quit()
    media_stub.clear_screen()