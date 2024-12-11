**Farmers Market (fMarket) Project**

# **Foreword**
FMarket is a Django project, created for the final exam of the SoftUni Python Web course.

The project was developed using Postgres DB, but switched to SQLite just before the final commit for convenient project run and testing of all functionalities by the exam masters.
# **Project Brief Description**
FMarket is an online marketplace platform project where EU farmers could offer their products to EU customers.

The current application is designed to function only as a virtual market stand, where farmers and customers meet. There is no an ordering system and payment gateways, the farmers list their products, the customers contact the farmers by a mean they choose form the ones the farmer offers and arrange all details for the deal privately by phone, email or some messaging system.

# **Run the project**
To run the project, after you’ve cloned the repo, you have to create a virtual environment and install the requirements using the requirements.txt file (pip install -r requirements.txt ).

You can use these test profiles credentials to test the website functions, **all the test users have currently the same password: ‘qwer’**(for easier testing):

super@mail.bg – superuser
user@mail.bg – user with completed profile that is not a seller 
seller1@mail.bg – approved seller with products uploaded, also a Site admin (is\_staff=True)
seller2@mail.bg –  approved seller with products uploaded
seller3@mail.bg – seller that is pending approval

You must add an .env file on the root of the project. You can copy the .env file content from this document:
https://docs.google.com/document/d/1cj4ZSzFL3viT4Vx_ib7QPbKbTkRuos-cLB6RCxSEZUA/edit?usp=sharing

All the credentials in the file are not and will not be used in production, sothere is no a problem to expose them here for a couple of days. The file will be deleted right after the end of the exam.
# **User Roles**
### **Unauthenticated users**
Can browse the products, see the product details page and read the product reviews, if any.
Can browse the farmers list page. Cannot see the farmer details page and the farmer’s contact info.
### **Authenticated Users**
Have full CRUD operations on their content.
Can browse the products, see the product details page and read the product reviews, if any.
Can browse the farmers page. Can see the farmer details page and the farmer’s contact info.
Can apply for seller. To apply for a seller, the user account must be complete – all the fields must have values. After submitting the seller application form, the user have “UNAPPROVED” status, until a Seller Admin or a Superuser changes the approval status to “APPROVED” (seller.approved=True).
### **Sellers (Farmers)**
Have full CRUD operations on their content and all the rights of the authenticated users, plus seller-specific rights:
Can create, edit and delete products. Can use the “My products” dashboard with quick links to create, view, edit or delete products.
### **Site Admins**
An Admin group with rights to view and edit Profiles, Products, Reviews and Sellers models. Site admins can approve seller applications and edit the site help Topics model (full CRUD rights).
### **Site Owners (Superusers)**
Have full CRUD right for all the site content + the Admin groups and the corresponding rights.
Have exclisive CRUD rights for the site Terms model.
