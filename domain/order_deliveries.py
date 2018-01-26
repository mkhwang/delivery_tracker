from orator import Model


class OrderDeliveries(Model):
    __table__ = 'order_deliveries'
    __fillable__ = ['id', 'oder_item_id', 'shipper_id', 'tracking_code', 'created_at', 'updated_at']
    __columns__ = ['id', 'oder_item_id', 'shipper_id', 'tracking_code', 'created_at', 'updated_at']
    __casts__ = {'created_at': 'string', 'updated_at': 'string'}

    def __repr__(self):
        return '<order_deliveries %r %r %r>' % (self.id, self.shipper_id, self.tracking_code)
