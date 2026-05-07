import json
from pathlib import Path

def run_mock_inference(image_id: str) -> dict:
    return {
        "image_id": image_id,
        "screening_result": "possible visible health concern",
        "confidence": 0.72,
        "recommended_action": "human review",
        "note": "Educational demo output. Not a diagnosis."
    }

if __name__ == "__main__":
    result = run_mock_inference("sample_bird_001.jpg")
    output_path = Path("demo/sample-output.json")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
