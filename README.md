Farmers Market (fMarket) Project

Overview
FMarket is a marketplace platform project where EU farmers offer their products to EU customers.
The current application is designed to function only as a market stand or place, where farmers and customers meet, there is no an ordering system and payment gateways, the farmers list their products, the customers contact the farmers with a mean they choose and arrange all details for the deal privately by phone, email or some messaging system.

User Roles
Unauthenticated users
Can browse the products, see the product details page and read the product reviews, if any.
Can browse the farmers page. Cannot see the farmer details page and the farmer’s contact info.
Authenticated Users
Have full CRUD operations on their content.
Can browse the products, see the product details page and read the product reviews, if any.
Can browse the farmers page. Can see the farmer details page and the farmer’s contact info.
Can apply for seller. To apply for a seller, the user account must be complete – all the fields must have values. After submitting the seller application form, the user have “UNAPPROVED” status, until a Seller Admin or a Superuser changes the approval status to “APPROVED” (seller.approved=True).
Sellers (Farmers)
Have full CRUD operations on their content and all the rights of the authenticated users, plus seller-specific rights:
Can create, edit and delete products. Can use the “My products” dashboard with quick links to create, view, edit or delete products.
Site Admins
An Admin group with rights to view and edit Profiles, Products, Reviews and Sellers models. Site admins can approve seller applications.
Site Owners (Superusers)
Have full CRUD right for all the site content + edit the Admin groups and the corresponding rights.
Have CRUD rights for the site help Topics model and the site Terms model.



