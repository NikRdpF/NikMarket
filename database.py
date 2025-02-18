from flask import Flask, request, jsonify

app = Flask(__name__)

# In a real application, you would connect to a database here.
# This is placeholder data for demonstration.
products = {
    "123": {"name": "Product ghhhfA", "description": "Description of Product A"},
    "456": {"name": "Product B", "description": "Description of Product B"}
}

@app.route('/product/<order_id>')
def get_product(order_id):
    product = products.get(order_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
  
