# Microservice architecture with Django & Flask
<hr>

<div>
    <p>
        In this repository i implement a microservice with django and flask.<br>
        this app is a very simple ecommerce feature app.

here there are two side:
* admin side
* client side

in admin side, I used django. here we could modify our products. e.g create a new product, update or delete one.

in client side, user could see these products and interact with them, e.g like a product.

* both services use own `mysql` database.    
* services communication do with `rabbitmq` message broker.
* project is `dockerized`. 
* for using `rabbitmq` i used a serverless rabbitmq platform: `www.cloudamqp.com`

there are two `.env` file in project, real .`env` file should not put in `github` for real products.

</p>
</div>