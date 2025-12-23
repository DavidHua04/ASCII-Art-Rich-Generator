# ASCII-Art-Rich-Generator

1. **Text To Image Converter**: Take in texts and convert it into Image. There should be one parameter for each dimensions to control the output image:
      1. Rendering Properties (How ASCII is rendered when converting to image)
          - Font family
          - Character spacing
          - Line spacing
          - Canvas width and height (e.g., 40 / 80 / 120 chars*10 / 20 / 30 lines)
          - background color


2. **ASCII Art Rich Generator**: Take in an Image and convert it into ASCII art of selected type. There should be one parameter for each dimensions to control the output ASCII Art text. All dimensions are:
      1. Character Semantics (What characters are made of)
          - Meaningless symbols (#$%&)
            - L1: Solid blocks (█) — pure shape, no semantics
            - L2: Symbols ($ @ #) — non-alphabetic, still meaningless
          - Random neutral words
            - L3: Digits (0–9) — neutral, readable but emotionless
            - L4: Capital letters (A–Z) — readable letters, still no sentiment
          - Positive words
            - L5: Positive words (LOVE, GOOD) — explicit positive meaning
            - L6: Positive emojis — emotionally positive symbolic units
            - L7: Positive poem fragments — full meaningful positive text

      2. Language Properties (if we are not choosing Meaningless Symbols in Character Semantics part)
          - English / Chinese (fullwidth characters) / Hebrew (Abjad, write and read  from right to left)
          - Multilingual mixtures

3. **Image Transformer**: Take in an image and transform it by applying one of the follow:
          - Resolution: high / medium / low
          - Non-uniform scaling (stretch/compress)
          - Gaussian blur
          - Grayscale vs RGB
          - Contrast changes
          - Waterprint

4. **pipeline**: