# My Garden
## About
My Garden is a blog portal where garden lovers can meet and share nice pictures and experiences with other garden lovers. Currently the site contains these categories dahlias, vegetables and fruits, geraniums and pelargoniums, fuchsias, roses and finally others. 
When you visit My Garden you will first see a page with all the latest posts and from there you are free to explore the different categories so that you can find posts that you like. When you are ready to create your own blog you can sign up and then you can access your own blog page. 

## UX
### User stories
[#3](https://github.com/MartinaB91/project4-my-blog/issues/3) Epic: Sign in with username
-   [#19](https://github.com/MartinaB91/project4-my-blog/issues/19) As a **Admin** I want to **sign-in with my username** so that I can **manage the blog content**.
-   [#28](https://github.com/MartinaB91/project4-my-blog/issues/28) As a **Blogger** I want to **sign in with my username** so that I can **manage my blog content**.


[#37](https://github.com/MartinaB91/project4-my-blog/issues/37) Epic: Ability to CRUD blog posts as Blogger:
-   [#38](https://github.com/MartinaB91/project4-my-blog/issues?38) As a **Blogger** I want to **create posts** so that I can **fill my blog with content that I like**
-   [#25](https://github.com/MartinaB91/project4-my-blog/issues/25) As a **Admin/Blogger/Visitor** I want to **search for posts** so that I can **find the topics that I wan't to read about faster**.
-	[#39](https://github.com/MartinaB91/project4-my-blog/issues/39) As **Blogger** I want to **update my posts** so that I can **make corrections if needed**.
-	[#29](https://github.com/MartinaB91/project4-my-blog/issues/29) As a **Blogger** I want to **delete posts I have posted** so that **my blog only contains the content I selected**.

[#6](https://github.com/MartinaB91/project4-my-blog/issues/6) Epic: Ability to CRUD blog posts as Admin
-   [#23](https://github.com/MartinaB91/project4-my-blog/issues/23) As a **Admin** I want to **create posts** so that I can **give** the bloggers useful information.
-   [#25](https://github.com/MartinaB91/project4-my-blog/issues/25) As a **Admin/Blogger/Visitor** I want to **search for posts** so that I can **find the topics that I wan't to reed about faster**.
-   [#26](https://github.com/MartinaB91/project4-my-blog/issues/26) As **Admin** I want to **update posts** so that I can **change the content in bloggers posts when needed**.
-   [#27](https://github.com/MartinaB91/project4-my-blog/issues/27) As a **Admin** I want to **delete posts** so that **the blog only contains the content I selected**.
-   [#45](https://github.com/MartinaB91/project4-my-blog/issues/45) As a **Admin** I want to **review all posts before they are published** so that I can **verify that no inappropriate content is published**.

[#7](https://github.com/MartinaB91/project4-my-blog/issues/7) Epic: Display blog post properties timestamp & category
-   [#24](https://github.com/MartinaB91/project4-my-blog/issues/24) As a **Admin/Blogger/Visitor** I want to **see which time and date the post was posted** so that I can **follow the posts timeline**.
-   [#22](https://github.com/MartinaB91/project4-my-blog/issues/22) As a **Blogger/Admin/Visitor** I want to **to see which category the post is posted in** so that I can **publish/view other posts in the same category**.
-   [#36](https://github.com/MartinaB91/project4-my-blog/issues/36) As a **Admin** I want to **be able to create blog categories** so that **the users can better organize their posts and the visitors easier can find content of interest**.

[#5](https://github.com/MartinaB91/project4-my-blog/issues/5) Epic: Implement functionality for comment and like
-   [#21](https://github.com/MartinaB91/project4-my-blog/issues/21) As a **Blogger** I want to **comment on posts** so that I can **can interact with the publisher and other readers**.
-   [#20](https://github.com/MartinaB91/project4-my-blog/issues/20) As a **Blogger** I want to **like/unlike posts** so that I can **show my appreciation**.
-   [#12](https://github.com/MartinaB91/project4-my-blog/issues/12) As a **Admin** I want to **view all unhandled comments** so that I can **see which status a comment has**.
-   [#18](https://github.com/MartinaB91/project4-my-blog/issues/18) As a **Admin** I want to **approve or disapprove comments** so that I can **control the content of my blog**.
-   [#16](https://github.com/MartinaB91/project4-my-blog/issues/16) As a **Blogger/Visitor** I want to **view comments on each post** so that I can **follow other people’s opinions**.

[#46]() Epic: View Bloggers personal posts & post status
-   [#47](https://github.com/MartinaB91/project4-my-blog/issues/47) As a **Blogger** I want to **view all posts I have created** so that I can **quickly  find, update or follow user interaction on my posts**.
- [#48](https://github.com/MartinaB91/project4-my-blog/issues/48) As a **Blogger** I want to **see if my post is published or not** so that I can **know if the Admin has approved my post**


## Technologies used
### Languages
- [Python (3.8.11)](https://www.python.org/)
- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
- [JavaScript](https://www.javascript.com/)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/css)

### Frameworks and libraries
- [Bootstrap (5.0)](https://getbootstrap.com/) - Used for styling and make site responsive
- [Django (4.0.4) ](https://www.djangoproject.com/) - Used for core functionality 
- [Django Allauth (0.50.0)](https://django-allauth.readthedocs.io/en/latest/installation.html) - Used for authentication and registration
- [Crispy Bootstrap5 (0.6)](https://pypi.org/project/crispy-bootstrap5/) - Used for make forms look nicer
- [JQuery](https://jquery.com/) - Used for making user interaction more lively 
- [Font Awesome](https://fontawesome.com/) - Used for adding icons to website
- [Google Fonts](https://fonts.google.com/) - Used for fonts

### Databases
- [SQLite](https://www.sqlite.org/index.html) - Used as development database 
- [PostgreSQL](https://www.postgresql.org/) - Used as production database

### Storage
- [Cloudinary](https://cloudinary.com/) - Used for storing pictures

### Other tools
- [Gunicorn (20.1.0)](https://gunicorn.org/)
- [Pyscopg2 (2.9.3)](https://pypi.org/project/psycopg2/) - Used for connect PostgreSQL to Python 
- [Heroku](https://id.heroku.com/login) - Used to deploy app
- [GitHub Issues](https://github.com/features/issues) - Used for project planning 
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used for debugging
- [Coolors](https://coolors.co/) - Used for choosing colors

## Features
## Design 
### Color scheme
<img src="readme-images/color-scheme.PNG">

- Green(#8aaa79): Used for edit buttons.
- Dark red(#830a48 ): Used for delete buttons.
- Secondary(Bootstrap): Used for all other buttons
- Pink(#dc758f): Used for text in quotes, author name in blog posts and for some links. 

### Typography
### Wireframes
### Flowcharts 
## Testing
## Deployment
## Credits
### Code
### Content and media
