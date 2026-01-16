POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":0}}

POST /product
{"id":"P1","name":"Prod","benefits":[],"variants":[{"id":"A","sku":"A","price":26000,"stock":10},{"id":"B","sku":"B","price":4000,"stock":10}]}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}]}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":30000,"benefitDiscount":0,"couponDiscount":0,"pointsUsed":0,"shippingFee":0,"totalAmount":30000}

POST /refund
{"orderId":"O1","variantId":"B","quantity":1}

GET /refund?orderId=O1
>>> {"orderId":"O1","itemRefundAmount":4000,"shippingAdjustment":5000,"calculatedRefundAmount":-1000,"finalRefundAmount":0,"flooredToZero":true,"remainingSubtotalBeforeDiscount":26000,"newShippingFee":5000}
