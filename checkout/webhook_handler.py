from django.http import HttpResponse
import stripe

class StripeWH_Handler:
    """Handle Stripe webhooks"""
    def __init__(self, request):
        self.request = request
    
    def handle_request(self, event):
        """Handle a generic/unknow/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook event"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        try:
            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=shipping_details.email,
                phone_number__iexact=shipping_details.phone_number,
                country__iexact=shipping_details.country,
                postcode__iexact=shipping_details.postal_code,
                street_address_1__iexact=shipping_details.line1,
                street_address_2__iexact=shipping_details.line2,
                county__iexact=shipping_details.state,
                grand_total=grand_total,
            )
            order_exists =True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:
                for item_id, item_data in bag.items():
                    order = Order.objects.create(
                        full_name__iexact=shipping_details.name,
                        email__iexact=shipping_details.email,
                        phone_number__iexact=shipping_details.phone_number,
                        country__iexact=shipping_details.country,
                        postcode__iexact=shipping_details.postal_code,
                        street_address_1__iexact=shipping_details.line1,
                        street_address_2__iexact=shipping_details.line2,
                        county__iexact=shipping_details.state,
                    )
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR: {e}')            

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook event"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)