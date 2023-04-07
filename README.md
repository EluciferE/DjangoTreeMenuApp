# Django Tree Menu App

This Django app allows you to create and display tree menus on your website. The menus are stored in the database and can be edited through the Django admin.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/<username>/<reponame>.git
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Apply the database migrations:
   ```
   python manage.py migrate
   ```

4. Run the Django development server:
   ```
   python manage.py runserver
   ```

## Usage

### Creating Menus

1. Log in to the Django admin panel.

2. Click on "Menus" to access the list of existing menus.

3. Click on "Add Menu" to create a new menu.

4. Enter a name and slug for the menu and click "Save".

5. Click on the menu name to add menu items.

6. Click on "Add MenuBranch" to add a new item.

7. Enter a name for the MenuBranch and select its parent item (if applicable).

8. Click "Save" to add the item to the menu.

### Displaying Menus

To display a menu on your website, use the following template tag:

```
{% draw_menu 'menu_name' %}
```

Replace "menu_name" with the name of the menu you want to display.

The active menu item is determined based on the URL of the current page. The menu will expand to show all parent items of the active item, as well as the first level of nesting under the active item.

### Example

![example](https://i.ibb.co/YPq2mYz/2023-04-08-024004177.png "title")