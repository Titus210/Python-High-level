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
                # Add more fertilizers and their effects
            },
            # Add more weeks and data as needed
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
    },
    "podFormation": {
        "duration": 45,
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
            "beanWeevil": {
                "risk": "moderate",
                "fertilizer": "nitrophoska",
            },
            # Add more pests and data as needed
        },
        "fertilization": {
            "week1": {
                "granuplus": "Enhances pod development",
                # Add more fertilizers and their effects
            },
            # Add more weeks and data as needed
        },
    },
    "maturation": {
        "duration": 70,
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
            "cutworm": {
                "risk": "low",
                "fertilizer": "nitrophoska",
            },
            # Add more pests and data as needed
        },
        "fertilization": {
            "week1": {
                "nitrophoska": "Improves pod filling",
                # Add more fertilizers and their effects
            },
            # Add more weeks and data as needed
        },
    },
      "harvest": {
        "duration": 14,
        "idealCondition": {
            "temperature": {
                "min": 21,
                "max": 27,
            },
            "wind": "moderate to high",
            "sunshine": "sunny",
        },
        "pest": {
            "harvestBugs": {
                "risk": "low",
                "fertilizer": "granuplus",
            },
            # Add more pests and data as needed
        },
        "fertilization": {
            "week1": {
                "granuplus": "Enhances pod quality",
                # Add more fertilizers and their effects
            },
            # Add more weeks and data as needed
        },
    },
}



def readIdealConditions(data):
    for stage, stage_data in data.items():
        ideal_condition = stage_data.get("idealCondition", {})
        temperature = ideal_condition.get("temperature", {})
        temperature_min = temperature.get("min", "N/A")
        temperature_max = temperature.get("max", "N/A")
        humidity = ideal_condition.get("humidity", "N/A")
        wind = ideal_condition.get("wind", "N/A")
        sunshine = ideal_condition.get("sunshine", "N/A")

        print(f"{stage}:")
        print(f"Temperature: Min {temperature_min}, Max {temperature_max}")
        print(f"Humidity: {humidity}")
        print(f"Wind: {wind}")
        print(f"Sunshine: {sunshine}")
        print("")

# Usage
readIdealConditions(beansData)
