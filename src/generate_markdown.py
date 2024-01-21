def generate_markdown(feature_name, description, usage_examples):
    markdown_code = f"## {feature_name}\n\n"
    markdown_code += f"{description}\n\n"
    markdown_code += "#### Usage Examples:\n\n"

    for example in usage_examples:
        markdown_code += f"- {example}\n"

    return markdown_code

# Example usage
feature_name = "Autonomous Image Recognition"
description = "This feature allows the AI system to autonomously recognize and categorize images using advanced computer vision algorithms."
usage_examples = [
    "Identifying objects in real-time from a live video stream",
    "Classifying images into different categories",
    "Detecting and analyzing facial expressions"
]

markdown_output = generate_markdown(feature_name, description, usage_examples)
print(markdown_output)
