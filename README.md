# _Stubby_

Description: This project is a simple text file creator, used to make Media Stubs for Kodi (formerly called XBMC)

## Project Setup

All you need is Python installed to run the script and following the input questions is fairly straight forward. 

It is built using Python 2 and may or may not work with Python 3.

## Background

I'm a big user of the media center software Kodi and wanted to create empty text files to populate 
the library with movies I had on the shelf. Creating Media Stubs for this kind of offline media is
described on this wiki page:

Media stubs - [http://wiki.xbmc.org/index.php?title=media_stubs](http://wiki.xbmc.org/index.php?title=media_stubs) (via Kodi Wiki)

I had a lot of movies that to go through and instead of doing it manually, I turned this into a learning experience with Python
and created a tool to help me out.

## Configuration

The only bit of configuration is if you want the created text files in a different folder outside of the included 'output' folder. In the
'stub_creator.py' file, change the directory as shown below.

```
#////
    #Change your desired path here
    #\\\\    
    sub_dir = 'output/'
```

