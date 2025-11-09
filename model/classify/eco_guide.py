def eco_suggestions(category):
    tips = {
        "recyclable": "Clean and dry items before recycling. Try reusing jars, boxes, or bottles for storage or crafts.",
        "non-recyclable": "Dispose safely in the right bin. Avoid burning; look for upcycling ideas before throwing away.",
        "wet": "Turn into compost or feed it into a biogas unit. Keep it away from plastics to reduce contamination.",
        "dry": "Reuse if possible. Keep papers or fabrics dry and send them to local recycling centers."
    }
    return tips.get(category, "No suggestion available for this category.")
