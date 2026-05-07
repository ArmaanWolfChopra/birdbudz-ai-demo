# birdbudz-ai-demo
Public demo of a responsible AI workflow for bird-health image screening

BirdBudz AI Demo is a simplified public prototype showing how computer vision could support bird-health screening workflows.

The goal is not to diagnose disease. The goal is to demonstrate a responsible AI workflow that can flag visible concerns and route uncertain cases for human review.

## What this demo shows

- Image preprocessing concept
- Sample inference-style output
- Confidence-style scoring
- Human-review recommendation
- Responsible AI limitations

## Example output

```json
{
  "image_id": "sample_bird_001.jpg",
  "screening_result": "possible visible health concern",
  "confidence": 0.72,
  "recommended_action": "human review"
}
