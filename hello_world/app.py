import json

def lambda_handler(event, context):
    """Sample Lambda function returning a list of donuts."""
    
    donuts = [
        {"name": "Chocolate Glazed", "image_name": "chocolate.avif", "price": 2.49},
        {"name": "Chocolate Sprinkle", "image_name": "chocolate_sprinkle.avif", "price": 2.79},
        {"name": "Cinnamon Sugar", "image_name": "cinnamon.avif", "price": 2.29},
        {"name": "Custard Chocolate", "image_name": "custard_chocolate.avif", "price": 3.49},
        {"name": "Classic Glazed", "image_name": "glazed.avif", "price": 1.99},
        {"name": "Maple Bar", "image_name": "maple.avif", "price": 2.99},
        {"name": "Mini Chocolate", "image_name": "mini_chocolate.avif", "price": 1.49},
        {"name": "Pumpkin Spice", "image_name": "pumpkin_spice.avif", "price": 3.29},
        {"name": "Strawberry Frosted", "image_name": "strawberry.avif", "price": 2.69}
    ]
    
    return {
        "statusCode": 200,
        "body": json.dumps({"donuts": donuts})
    }
