# Lore-Api
An API for allowing multiple developers to create baseline NPCs for the game Lore.

##What it uses
This API uses Django-Rest-Framework and Django, a Unity based demo of the game Lore (not required for it to work, but it is what the whole thing is for)

##How it works/Seeing it Work
First get the project files for Lore off of GitHub (coming soon!)<br><br>
Open up the game and in the script (temp) change the location of the database (db3(temp)) to the location the db created by the API is in.<br><br>
Open up Lore-API and run 'python manage.py createsuperuser' to create an account.<br><br>
You can start the server for this locally using python manage.py runserver<br><br>
Follow the server link in terminal.<br><br>
You'll need to log in, and then you should be able to create any NPC by including a name(only letters) and a class (only letters).<br><br>

##What will be added in the future:
For NPC creation an assortment of selectable features for the NPC when game development is further along.<br><br>
A basic search function to search for an NPC by class, name, feature, or creator.
