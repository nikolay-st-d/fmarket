**Farmers Market (fMarket) Project**

# **Foreword**
FMarket is a Django project, created for the final exam of the SoftUni Python Web course. Since it is  created for educational purposes, it does not have full functionality required for a real application.

The project was developed using Django and Postgres DB, but switched to SQLite just before the final commit for convenient project run and testing with initial data of the functionalities by the exam masters. A Postres SQL dump file is included in the repo for those wishing to run the application with PostgresSQL (The data slightly differ from the included SQLite3 DB).

Everything in this project is created from scratch, including the design, the graphics, the HTML and the CSS, no templates or libraries were used.
# **Project Brief Description**
FMarket is an online marketplace platform project where farmers could offer their products to customers. The application targets users in EU countries only, sellers could select within the EU countries only and the currency is EUR.

The application is designed to function only as a virtual market stand, where farmers and customers meet. There is no ordering system and payment gateways, the farmers list their products, the customers contact the farmers by a mean they choose form the ones the farmer offers and arrange all details for the deal privately by phone, email or some messaging system.

The app has also a Help section and a Terms of Usage section, publicly visible.

# **Run the project**
The project is not deployed and could be run only locally. To run the project, after you’ve cloned the repo, you have to create a virtual environment and install the requirements using the requirements.txt file (pip install -r requirements.txt ).

You must add an .env file on the root of the project. You can copy the .env file content from this document:
https://docs.google.com/document/d/1cj4ZSzFL3viT4Vx_ib7QPbKbTkRuos-cLB6RCxSEZUA/edit?usp=sharing

*The credentials in the above file are not and will not be used in production, so there is no a problem to expose them here for a couple of days. The file will be deleted right after the end of the exam.*

You can use the following test profile credentials to test the website functions, **all the test users have currently the same password: ‘qwer’**(for easier testing):

*super@mail.bg – superuser*

*user@mail.bg – user with completed account that is not a seller*

*seller1@mail.bg – approved seller with products uploaded, also a Site admin (is\_staff=True)*

*seller2@mail.bg –  approved seller with products uploaded*

*seller3@mail.bg – seller that is pending approval*

# **User Roles**
### **Regulat (Unauthenticated) users**
Can browse the products, see the product details page and read the product reviews, if any.
Can browse the farmers list page. Cannot see the farmer details page and the farmer’s contact info.
### **Authenticated Users**
Users register and authenticate with an email and a password.

The User has an associated User Profile, where additional info is provided – first name, last name, country and phone number. When all the Profile fields have values, the user account is “completed” (this is handled by a context processor function).

Have full CRUD operations on their content.
Can browse the products, see the product details page and write  product reviews. One user can write only one review for a product.
Can browse the farmers page. Can see the farmer details page and the farmer’s contact info.
Can apply for seller, if their Account is “completed”.  After submitting the seller application form, the user have “UNAPPROVED” status, until an Admin or a Superuser changes the approval status to “APPROVED” (seller.approved=True).

Authenticated users could see the “My reviews” buttons in the site menu, where they could manage the reviews they have wrote for products.
### **Sellers (Farmers)**
Have full CRUD operations on their content and all the rights of the authenticated users, plus seller-specific rights:
Can create, edit and delete products.
Can use the “My products” dashboard with quick links to create, view, edit or delete products.

Approved farmers could see the “My Farmer Profile” and “My Products” buttons in the site menu, where they could manage their seller profile and their products..
### **Site Admins**
An Admin group with rights to view and edit Profiles, Products, Reviews and Sellers models. Site admins can approve seller applications and edit the site help Topics model (full CRUD rights).
### **Site Owners (Superusers)**
Have full CRUD right for all the site content + the Admin groups and the corresponding rights.
Have exclusive CRUD rights for the site Terms model. The website Terms model is managed exclusively in the Django Admin.
# **Main site sections**
### **Home page**
The home page shows some general info about the website and a section with the most popular products - the ones that have most views. There is also a “How it works” section, that is visible only for regular (non-logged) users.

### **User/Account**
This section is accessed from the header buttons. Users could manage their accounts.
Authenticated users could see an additional “My Reviews” button n the menu to manage their product reviews.

### **Products**
A list of products with pagination. When a product is clicked, a page with all details is shown to the user. If the user is authenticated, he could see a button to go to the seller details and see their contact info to start dealing.

### **Farmers**
The farmers list is visible to everyone, but only logged-in users could see their full details. Approved farmers could see proprietary buttons in the menu.

### **Help Topics**
A list of help topics. If the authenticated user is staff or superuser, he could see Edit and Delete buttons, as well as a “New topic” button to add new records to the DB.

### **Site terms**
A list of legal terms, required by laws.
###
### **Contact**
Contact page to contact a website admin via email using a form.

# **Technologies used:**
Django 5.1.4
Python 3.12
PostgreSQL
Django ORM
HTML5
CSS3
Git

# **Screenshots**
![image](https://github.com/user-attachments/assets/203e540b-7174-477e-ab8d-c6abde3442a2)

![image](https://github.com/user-attachments/assets/80d286bc-97df-45e5-9120-74b56dc47a14)

![image](https://github.com/user-attachments/assets/30c7965e-9a50-4bc8-aa91-8ce012bd1d83)

![image](https://github.com/user-attachments/assets/cb171797-1978-46ad-8d88-f9ba8b4c0d6c)

![image](https://github.com/user-attachments/assets/ebfde911-b38f-4f44-a630-faf36231c90e)

![image](https://github.com/user-attachments/assets/e5b9a219-812a-4ef9-b677-d8c9ce3869ea)





