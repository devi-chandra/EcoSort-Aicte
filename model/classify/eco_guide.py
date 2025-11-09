def get_eco_guide(label):
    guides = {
        "Recyclable": "Rinse and sort items. Send them to your nearest recycling center. Try reusing jars or bottles creatively.",
        "Non-Recyclable": "Dispose safely in non-recyclable bins. Avoid mixing with food waste. Look for eco-friendly alternatives.",
        "Wet": "Use it for composting. Ideal for garden manure. Keep it separate from plastic and metal waste.",
        "Dry": "Store and send for recycling. Items like plastic or glass can be repurposed for DIY home decor."
    }
    return guides.get(label, "Handle with care and dispose responsibly.")
