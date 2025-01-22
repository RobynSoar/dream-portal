# DreamPortal
(by Robyn Soar)

DreamPortal is an online site to collate dreams and/or nightmares into written form to be able to share with others, or record them for personal view in the future.

View the live site [here]()

## Key Project Goals

- A website that has a simple user friendly interface, allowing users to use the site even when half-awake.
- To allow users to be able to journal their dream experiences and share with others.
- To allow users to comment on posts.
- To allow users to be able to bookmark their favourite dreams.

## Target Audience

The primary target audience for the site is:

- Ages of 13+ looking for a system to store their dreams/nightmares.
- Those who like to read and gain inspiration for their own writings elsewhere.

## Table of Contents

- [Features](#features)
    - [Site Wide](#site-wide)
    - [Landing Page](#landing-page)
    - [404 Error Page](#404-error-page)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Agile Methodology](#agile-methodology)
    - [User Stories](#user-stories)
    - [Kanban Board](#kanban-board)
- [Design](#design)
    - [Flowchart](#flowchart)
    - [Colour Palette](#terminal-sizing)
    - [Google Fonts](#google-fonts)
    - [Technologies Used](#technologoies-used)
- [Testing](#testing)
    - [Responsiveness](#responsiveness)
    - [Accessibility](#accessibility)
    - [Lighthouse Testing](#lighthouse-testing)
    - [User Story Testing](#user-story-testing)
    - [Functional Testing](#functional-testing)
    - [Validator Testing](#validator-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Deployment to Heroku](#deployment-to-heroku)
    - [Clone the Repository in GitHub](#clone-the-repository-code-locally)
- [Credits](#credits)
    - [Inspired Code](#inspired-code)
    - [Walkthrough Code](#walkthrough-code)
    - [Acknowledgements](#acknowledgements)
- [Author](#author)

## Features

### Site Wide



### Landing Page



### 404 Error Page



### Existing Features



### Features Left to Implement



[Return to Table of Contents](#table-of-contents)

## Agile Methodology

### User Stories



### Kanban Board



[Return to Table of Contents](#table-of-contents)

## Design

### Flowchart


### Colour Palette


### Google Fonts

[Google Fonts](https://fonts.google.com/) was used to import fonts for the site, these include:

- "Nunito", serif: Used for the site logo and post titles.
- "Raleway", serif: Used for all other text content site wide.

### Technologies Used

- GitHub
    - Hosts the DREAMPORTAL repo, used for version control and project management. (GitHub issues, Kanban board)
- Gitpod
    - Used for development of the site as well as commit and pushing code throughout.
- [Heroku](https://dashboard.heroku.com/apps)
    - Used for deployment of DREAMPORTAL.
- HTML
    - The main language used to provide users with the front-end user interface.
- CSS
    - Used to style the site, working alongside Bootstrap from within a static file.
- Bootstrap
    - CSS framework used for quick and easy styling of site.
- Django 4.2.18
    - Python framework used to implement logic.
- PostgreSQL
    - Database used to store all data.
- Whitenoise
    - Python library for handling static files.
- Django Summernote
    - Used to provide extra editing tools to Django admin panel.
- [Google Fonts]()
    - Used to import fonts to be used within the site.

[Return to Table of Contents](#table-of-contents)

## Testing

### Responsiveness



### Accessibility



### Lighthouse Testing



### User Story Testing



### Functional Testing



### Validator Testing



### Fixed Bugs

__Name change / Deployment Bug__

![Application Error](documentation/application-error.png)

While deploying the app for the first time on Heroku, there was an 'Application' Error.

As Heroku informed, I tried to use `heroku logs --tail` and received the following message:

`›   Error: The following error occurred:
 ›     Missing required flag app
 ›   See more help with --help`

Searching for my app with `heroku logs --tail --app dream-portal-app" I was greeting with a message to follow a link to authorise login via browser. I wasn't able to do this as an error message of "IP address mismatch" showed and I needed to authorise within the terminal rather than the browser.

[Heroku CLI Commands](https://devcenter.heroku.com/articles/heroku-cli-commands)
- List of commands used to export API key and connect it to the project.

API Key was found within the Settings > Accounts section of Heroku personal profile.

Further investigation also showed I'd neglected to insert a blank space between authorised hosts in the settinngs.py file.


### Unfixed Bugs



[Return to Table of Contents](#table-of-contents)

## Deployment

### Version Control

The site was created using the Git editor and pushed to GitHUb to the remote repository 'rpsls-game'

The following git commands were used throughout development to push code to the remote repository:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are commited.

```git commit -m "commit message"``` - This command was used to commit changes to the local repository queue ready to be pushed.

```git push``` - This command was used to push all committed code to the remote repository 'rpsls-game' on GitHub.

### Deployment to Heroku



### Clone the Repository In GitHub



[Return to Table of Contents](#table-of-contents)

## Credits

### Inspired Code



### Walkthrough Code



### Acknowledgements



[Return to Table of Contents](#table-of-contents)

## Author

Robyn Soar
robyn999@hotmail.co.uk