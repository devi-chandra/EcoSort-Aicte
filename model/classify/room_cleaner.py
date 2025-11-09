import random

def analyze_room(items_detected):
    """
    Analyzes detected items in a messy room image and gives cleaning + decor ideas.
    items_detected = list of strings like ["clothes", "books", "trash"]
    """

    cleaning_tips = []
    decor_tips = []

    if "clothes" in items_detected:
        cleaning_tips.append("Fold or hang clothes; keep a small laundry basket for daily use.")
        decor_tips.append("Add a minimalist clothes rack or hidden storage bin for neatness.")

    if "books" in items_detected:
        cleaning_tips.append("Stack or organize books vertically to clear desk space.")
        decor_tips.append("Use a wall shelf or small bookshelf to make your room look smart.")

    if "trash" in items_detected or "waste" in items_detected:
        cleaning_tips.append("Separate dry and wet waste into small bins; dispose responsibly.")
        decor_tips.append("Keep a compact bin beside your desk to maintain cleanliness.")

    if "electronics" in items_detected:
        cleaning_tips.append("Untangle or tie cables together using clips or velcro bands.")
        decor_tips.append("Add a warm desk lamp or LED strip for aesthetic lighting.")

    if "papers" in items_detected:
        cleaning_tips.append("Sort papers into 'important' and 'scrap' folders.")
        decor_tips.append("Use a corkboard or wall grid to pin notes decoratively.")

    # Default if nothing detected
    if not cleaning_tips:
        cleaning_tips.append("Room looks tidy! A quick dusting will keep it fresh.")
        decor_tips.append("Add a plant, fairy lights, or soft colors for coziness.")

    return {
        "cleaning_tips": cleaning_tips,
        "decor_tips": decor_tips,
        "bonus_idea": random.choice([
            "Try adding a small indoor plant for freshness.",
            "Hang a mirror to make your space look bigger.",
            "Use warm-toned lighting for a relaxing vibe."
        ])
    }

# Example usage
# print(analyze_room(["clothes", "books", "trash"]))
