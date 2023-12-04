beansData = {
    "germination": {
        "duration": 7,
        "idealCondition": {
            "temperature": {
                "min": 18,
                "max": 24,
            },
            "humidity": {
                "min": 70,
                "max": 85,
            },
        },
        "pest": {
            "aphid": {
                "risk": "high",
                "fertilizer": "syngenta",
            },
            "termite": {
                "risk": "moderate",
                "fertilizer": "miracle-gro",
            },
            # Add more pests and data as needed
        },
        "tasks": {
            "week1": ["Planting", "Fertilize with syngenta"],
            # Add more tasks for each week
        },
    },
    "vegetativeGrowth": {
        "duration": 30,
        "idealCondition": {
            "temperature": {
                "min": 21,
                "max": 27,
            },
            "humidity": {
                "min": 75,
                "max": 85,
            },
        },
        "pest": {
            "whitefly": {
                "risk": "low",
                "fertilizer": "nitrophoska",
            },
            "leafhopper": {
                "risk": "moderate",
                "fertilizer": "granuplus",
            },
            # Add more pests and data as needed
        },
        "fertilization": {
            "week1": {
                "syngenta": "Reduces aphids",
                "nitrophoska": "Promotes growth",
                # Add more fertilizers and their effects
            },
            "week2": ["Fertilize with nitrophoska"],
            # Add more weeks and data as needed
        },
        "tasks": {
            "week1": ["Fertilize with syngenta"],
            "week2": ["Fertilize with nitrophoska"],
            # Add more tasks for each week
        },
    },
    "flowering": {
        "duration": 40,
        "idealCondition": {
            "temperature": {
                "min": 21,
                "max": 27,
            },
            "humidity": {
                "min": 75,
                "max": 85,
            },
        },
        "pest": {
            "podborer": {
                "risk": "high",
                "fertilizer": "granuplus",
            },
            # Add more pests and data as needed
        },
        "fertilization": {
            "week1": {
                "miracle-gro": "Boosts flower development",
                # Add more fertilizers and their effects
            },
            # Add more weeks and data as needed
        },
        "tasks": {
            "week1": ["Inspect for podborer damage", "Fertilize with miracle-gro"],
            # Add more tasks for each week
        },
    },
    # Continue with other growth stages and tasks
}
