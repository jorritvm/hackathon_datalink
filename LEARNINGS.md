# Shiny for Python
## Overview of lessons learned
- nothing interesting / ready to use in the gallery or templates section:
  - https://shiny.posit.co/py/gallery/
  - https://shiny.posit.co/py/templates/

- conctains some widgets out of the box, but has more widgets (specifially jupyter related) in
    - https://github.com/posit-dev/py-shinywidgets?tab=readme-ov-file
    - https://github.com/posit-dev/py-shinywidgets?tab=readme-ov-file

- there is both a core and express
    - shiny (core): This is the core package of Shiny for Python. It provides the fundamental building blocks for creating Shiny applications, including the main App class, UI components, and server logic. It is used for more detailed and customized Shiny applications.
    - shiny.express: This is a higher-level API built on top of the core shiny package. It provides a more concise and expressive syntax for creating Shiny applications, making it easier and faster to build simple applications. It is designed to simplify common tasks and reduce boilerplate code.

- - easily themeable with https://bootswatch.com/ themes
    https://shiny.posit.co/py/docs/ui-customize.html#:~:text=Simply%20choose%20a%20theme%20from,(Shiny%20Core)%20or%20ui.

- datagrid widget provides sorting options and line highlighting

- **terrible developer experience**
  - refresh cycle is slow when developing
  - instead of refreshing uvicorn server crashes a lot/most of the time (you have to 'kill tree' it) 
  - no decent traceback & error messages

- due to the above, rather slow development speed

- there is quite some magic that you need to learn before you understand the shiny code 
  - it relies on functions having the same name as certain string placeholders
  - it requires the use of (sometimes multiple) decorators and functions within functions to work

- you have to resort to writing custom css quite quickly