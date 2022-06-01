# SmartBank-

Banking System For GRIP Program

## Technologies Used in educa

### Back-end

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

### Front-end

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

## Features

1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Balance Enquiry
6. Account Status
7. Account Statement
8. Logout

## Installation

```shell
pip install -r requirements.txt 
```

Run the following command in the prject directory.

```shell
python manage.py makemigrations banks
python manage.py migrate
```

## Understanding Task

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

## Research

    Django Framework is suitable for such task (backend) holding the logic for the system.
    Html & CSS With django templating engine (DTE) (frontend).
    Make Use of a template to save time (carrd.co). 

## Planning

I've used django framwork with slqlite database then strated to design the data model.

    Data Model
        Cutomers Table with basic information fields plus their account balance.

        Transfers Table with filed such (sender, receipant, amount) 
            manyTOne relationship with the customers Table
                One Customer can create multiple tranfers and Many Customers can recieve Multiple transfers.

    Create Views holding system logic & Quering which data to display
        Money Transfer Functionality
        Loggin All Customers Tranfers

## Code

    Using Python Programming language
        Writing Programming Objects for Django ORM to create the desired data model then migrate into database.
        Definging Views For quering necessary date which will be displayed in the frontend

## Execute

    Running Django Out Of the Box Developemnt server.
    Creating Users From django admin panel.
    Getting all system functionality into action
        (display all customers - cutomer details - transer money - transfers history - Money Transfer From)

## License

MIT License

Copyright (c) 2022 Yusuf Adel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
