# SmartBank-

Banking System For GRIP Program

## Understanding Task:

- Create a simple dynamic website which has the following specs.

- Start with creating a dummy data in database for upto 10
customers. Database options: Mysql, Mongo, Postgres, etc.
Customers table will have basic ﬁelds such as name, email,
current balance etc. Transfers table will record all transfers
happened.

- Flow: Home Page > View all Customers > Select and View one
Customer > Transfer Money > Select customer to transfer to >
View all Customers .

- No Login Page. No User Creation. Only transfer of money
between multiple users.

- Host the website at 000webhost, github.io, heroku app or any
other free hosting provider. Check in code in gitlab.

## Research:

    Django Framework is suitable for such task (backend) holding the logic for the system.
    Html & CSS With django templating engine (DTE) (frontend).
    Make Use of a template to save time (carrd.co). 

## Planning:

I've used django framwork with slqlite database then strated to design the data model.

    Data Model
        Cutomers Table with basic information fields plus their account balance.

        Transfers Table with filed such (sender, receipant, amount) 
            manyTOne relationship with the customers Table
                One Customer can create multiple tranfers and Many Customers can recieve Multiple transfers.

    Create Views holding system logic & Quering which data to display
        Money Transfer Functionality
        Loggin All Customers Tranfers

## Code:

    Using Python Programming language
        Writing Programming Objects for Django ORM to create the desired data model then migrate into database.
        Definging Views For quering necessary date which will be displayed in the frontend

## Execute:

    Running Django Out Of the Box Developemnt server.
    Creating Users From django admin panel.
    Getting all system functionality into action
        (display all customers - cutomer details - transer money - transfers history - Money Transfer From)
