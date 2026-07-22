# Stoichio

#### Video Demo: https://youtu.be/0MEmhTn3feY?si=2VSqPqLemFUp_yNE

## Description
Stoichio is a Flask-based educational chemistry website designed to make
chemistry concepts easier to understand.

The motivation behind the project was to create a platform that explains recent chemistry discoveries and safety-related topics without overwhelming
users with technical language, while still maintaining scientific accuracy. The site is intended to be scalable, allowing new content to be added over
time, and focuses on clarity, structure, and ease of navigation.

The project was built using Python, Flask, HTML, CSS, and Bootstrap.
Navigation between pages is handled using Flask routes and templates.


 Application Structure and Files:

 1. app.py

 The app.py file contains the core backend logic of the application. It configures database access and handles routing between pages.

A helper function, get_db(), is used to connect to the SQLite database (stoichio.db). This function ensures consistent database access and allows rows to be accessed by column name, improving readability and maintainability.

Routes defined in app.py include:
. The homepage
./about
./recently
./archive
./what-to-avoid

The /recently route supports both GET and POST methods. While the current interface focuses on displaying content, POST handling allows for future expansion where new posts could be added dynamically. The /archive route retrieves all stored posts from the database and displays them in chronological order, demonstrating structured data retrieval using S

Stoichio.db

The SQLite database stores chemistry posts using a posts table. Each post contains a title, summary, and date. SQLite was chosen because it is lightweight, easy to integrate with Flask, and well-suited for small to medium-sized educational applications. The database allows Stoichio to scale beyond static pages by separating content from presentation.


templates/

The templates directory contains all HTML templates rendered by flask using Jinga.

. index.html

Acts as the landing page and introduces the purpose of the site. It provides clear navigation to other sections.

. recently.html

This is the core feature of the project. It displays a featured post explaining a recent chemistry discovery. The page uses a card-based layout and includes a “More info” button implemented with Bootstrap’s collapse component. This design choice allows additional scientific context to be revealed without cluttering the interface.


. archive.html

Displays all past posts stored in the database. This page demonstrates how SQLite data is dynamically rendered using Jinja loops and provides a scalable solution for storing weekly or recurring content.


. about.html

Explains the purpose of Stoichio and the motivation behind the project.



. Weeklypoisons.html (renamed it but this is the original that I hadn't changed to avoid mistakes)

Presents information about chemicals and substances to be cautious of, framed in an educational rather than alarmist way. (Hence, the change in name...)



. _nav.html

A shared navigation bar included across pages using Jinja’s {% include %} directive. This avoids repetition and ensures consistent navigation.

. static/

The static directory contains custom styling and assets.


. Styles.css

Contains project-specific CSS used to adjust spacing, typography, and layout beyond default Bootstrap styles. Styling choices were kept minimal to maintain clarity and readability.


Design Choices:

One key design decision was to focus on clarity over quantity. Rather than overwhelming users with many posts or dense text, the Recently page highlights a single discovery with expandable detail. This approach mirrors how students often prefer to engage with new material—starting with a summary and optionally exploring deeper context.

Another important choice was separating recent posts from archived content. This improves usability and mirrors real-world content platforms, where current material is prioritised while older entries remain accessible.

Bootstrap was used to ensure responsiveness across devices, especially tablets, without requiring complex custom CSS. SQLite was chosen instead of a larger database system to keep the project lightweight and appropriate for its educational scope.


Conclusion:

Stoichio demonstrates how Flask, SQLite, and templating can be combined to build a functional, scalable educational web application. The project emphasises clean structure, thoughtful design choices, and clear explanations over unnecessary complexity. Through this project, I gained experience in backend development, database integration, and frontend layout design, as well as a deeper understanding of how these components interact within a full-stack application.
