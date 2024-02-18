# **Revforum**

## **Overview**

Cosycoffee is coffee roaster with an e-commerce website aimed to coffee lovers. On the website, the users can find several options of speciality coffee beans roasted by the company to buy and also accessories like filters, different brewing methods and others. Once they are logged in and they make their first purchase, their shipping details are attached to their profile, so they do not need to repeat that step on a second order. They also have the chance to sign up for the newsletter.

![Main screen screenshot]()

## Table of contents

- [**Cosy COffee**](#revforum)
  - [**Overview**](#overview)
  - [Table of contents](#table-of-contents)
  - [**Planning stage**](#planning-stage)
    - [**Target Audiences:**](#target-audiences)
    - [**User Stories:**](#user-stories)
    - [**Site Aims:**](#site-aims)
    - [**Forum Structure:**](#forum-structure)
  - [**Current Features**](#current-features)
      - [*Main Screen:*](#main-screen)
      - [*Products page:*](#products-page)
      - [*Product detail page:*](#product-detail-page)
      - [*Shopping cart page:*](#shopping-cart-page)
      - [*Secure checkout:*](#secure-checkout)
      - [*Profile page:*](#profile-page)
  - [**Future-Enhancements**](#future-enhancements)
  - [**Testing Phase**](#testing-phase)
  - [**Validators**](#validators)
  - [**Bugs**](#bugs)
  - [**Deployment**](#deployment)
  - [**Tech**](#tech)
  - [**Credits**](#credits)
    - [**Honorable mentions**](#honorable-mentions)
    - [**Content:**](#content)

## **Planning stage**

### **Target Audiences:**

- Users interested in coffee.
- Users interested in coffee roasters.
- Users interested in speciality coffee.
- Users interested in a premium experience with coffee.
- Users interested in having good quality coffee at their own property.
- Users interested in making high quality coffee at home.
​

### **User Stories:**

- As a user, I want to sign up.
- As a user, I want to sign in.
- As a user, I want to sign out.
- As a user, I want to reset my password.
- As a user, I want to be able to modify my password if I am logged in.
- As a user, I want to see all the available coffees/accessories.
- As a user, I want to search all the available coffees/accessories.
- As a user, I want to see more details of each coffee/accessory.
- As a user, I want to add the coffee/accessory to the cart.
- As a user, I want to check my current shopping cart.
- As a user, I want to add or remove the quantity of items in the shopping cart.
- As a user, I want to add or remove items of the shopping cart.
- As a user, I want to know how much is order at any specific time.
- As a user, I want to add my shipping and billing addresses.
- As a user, I want to know how much would be the shipping cost.
- As a user, I want to add my payment details.
- As an admin, I want to add coffee/accessories to the website.
- As an admin, I want to update coffee/accessories information on the website.
- As an admin, I want to remove coffee/accessories from the website.
- As an admin, I want the orders made on website.
​

### **Site Aims:**

- To provide an e-commerce website for coffee aficionados.
- To provide the information clients interested in speciality coffee would be interested, such as origin, processing method, producer, etc.
- To provide a safe environment for users to buy coffee or coffee paraphernalia.
- To provide an excellent buying experience with information in all the steps of the buying process.
- To allow users to sign up to the Newsletter so they can be informed of any sales, promotions or new arrivals.

### **Forum Structure:**

![Cosycoffee Structure - Diagram]()

## **Current Features**

​

#### *Main Screen:*

- Main screen of the website. The page is divided in five main areas:
  . Banner with the threshold for free shipping.
  . Navigation bar with a search button for the products and profile access.
  . Quick links to the products: all products, coffee beans or accessories.
  . Carousel with the main products available.
  . Footer with connection to social media profiles.

![Main screen screenshot]()

#### *Products page:*

- Once the user/visitor clicks in one of the products links, the page of the products is shown. It provides the image, name, the price and the rate of the product.

![Product page screenshot]()

#### *Product detail page:*

- When the user clicks at any of the products, they are redirect to the information of the product. They have more details of each product and can choose to add to their shopping cart the quantity they desire of the product.

![Product detail screenshot]()

#### *Shopping cart page:*

- If the user clicks on the shopping cart at the navbar, the user can access their current order. They will have a list of the items, with their quantity, how much each individual item will cost and if they have free shipping or not. If they have not reached the threshold, the website inform the user how much more they need to add to the car to be able to have free delivery.

![Shopping cart screenshot]()

#### *Secure checkout:*

- When the user decides to make the payment, they are taken to the page where they can add their shipping/billing information. If they are not logged in, the website requests them to login or to sign up. They are not able to pay for an order without an account. This is a marketing decision, so that every sell can bring a new lead for the list of users and for the newsletter. Once the payment is finalised, they are informed that the order was made and that they will received an email with the confirmation soon.
 
![Secure checkout screenshot]()
![Order succeeded screenshot]()

#### *Profile page:*

- Once the user makes their first buy, their profile is automatically saved into their profile. However, the users can access and update all the details if necessary. The users also can access their previous order and check what they ordered.

![Profile screenshot]()

​#### *Product Management page:*

- Administradors of the page have access to the product management page. In this page, they can add new products to the website. To edit and delete products, the administrator can do through the products page. Each product has their own update and delete buttons.

![Producers Management screenshot]()

​#### *Product Management page:*

- Like the page below, administradors of the page have access to add new producers to the website. They are connected to the coffee. So, whenever a new coffee product is added, the administrator can choose from one of the producers listed.

![Producers Management screenshot]()

## **Future-Enhancements**

​

- Users could log through their social networks profiles (FB, X).

​

## **Testing Phase**

​

Implementation: Create new category as admin.

Test: Access admin area and created new category.

Result: New category appeared on the website.
***

## **Validators**

. Lighthouse ![Lighthouse screenshot]()
All pages passed the Lighthouse check.

. W3C HTML Validator ![W3C HTML Validator screenshot]()

. W3C CSS Validator ![W3C CSS Validator screenshot]()

. Python Linter ![Python Linter Validator screenshot]()

## **Bugs**

Problem 🐞: 

Cause🛠: 

Resolution✅: 
***

## **Deployment**

## **Tech**

- Python.
- Django.
- Javascript.
- Django-allauth.
- Pillow.
- Crispy-forms.
- Stripe.
​

## **Credits**

### **Honorable mentions**

- Larissa Moura (my wife) - She was my tester and also my design guru.
- Richard Wells (my Code Institute tutor) - Help me throughout the project in all aspects.
​

### **Content:**

- Structure of the project (apps) based on the codealong project "Boutique Ado" from [CodeInstitute] (<https://github.com/Code-Institute-Org/boutique_ado_v1>)
- Search bag based on the simple bar example from [SliderRevolution] (<https://www.sliderrevolution.com/resources/css-search-box/>)
- Images of producers collected from [Freepik] (<https://www.freepik.com>)
- Images of acccessories taken from each company website
- SKUs made with [Zoho] (<https://www.zoho.com/inventory/sku-generator/>)
