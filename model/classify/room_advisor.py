import random

def analyze_room(image_path):
    """
    Mock analyzer for now – later you can integrate a Vision API or ML model.
    This function simply returns a random cleanup + decor suggestion.
    """
    cleanup_tips = [
        "Start by sorting clothes and books into separate piles.",
        "Use labeled bins for waste, recyclables, and donation items.",
        "Wipe surfaces and vacuum corners for a neat look.",
        "Fold blankets and arrange your bed for an instant refresh."
    ]

    decor_tips = [
        "Add a small indoor plant for a fresh vibe.",
        "Use warm fairy lights or LED strips for cozy lighting.",
        "Hang minimal wall art or photos for a personal touch.",
        "Try arranging furniture to maximize floor space."
    ]

    return {
        "cleanup": random.choice(cleanup_tips),
        "decor": random.choice(decor_tips)
    }
