# eco_guide.py
def get_eco_advice(category):
    advice = {
        "recyclable": {
            "reuse": [
                "Turn old plastic bottles into planters or storage containers.",
                "Reuse glass jars for organizing kitchen spices or stationery.",
                "Donate usable items to recycling centers or NGOs."
            ],
            "dispose": [
                "Rinse before recycling.",
                "Separate from wet waste.",
                "Drop at authorized recycling bins."
            ]
        },
        "non-recyclable": {
            "reuse": [
                "Use old cloth for cleaning or DIY crafts.",
                "Try to reduce buying such items in the future."
            ],
            "dispose": [
                "Wrap safely and place in dry waste bins.",
                "Avoid burning plastic or mixed waste."
            ]
        },
        "wet": {
            "reuse": [
                "Use food leftovers for composting.",
                "Use fruit and vegetable peels as fertilizer or DIY scrubs."
            ],
            "dispose": [
                "Use a compost bin.",
                "Keep separate from plastic or metal waste."
            ]
        },
        "dry": {
            "reuse": [
                "Paper can be reused for notes or crafts.",
                "Cardboard boxes can be used for storage."
            ],
            "dispose": [
                "Send to dry waste collection center.",
                "Avoid mixing with wet waste."
            ]
        }
    }

    category = category.lower()
    if category in advice:
        return advice[category]
    else:
        return {"reuse": ["No suggestion available."], "dispose": ["No disposal info found."]}
